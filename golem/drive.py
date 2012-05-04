import logging
import tweepy
import cPickle
import errno
import time

def loop(api, seconds, already_seen_filename, my_screen_name, handler):
    log = logging.getLogger('drive')
    orig_seconds = seconds
    try:
        already_seen = cPickle.load(file(already_seen_filename))
    except IOError, e:
        if e.errno == errno.ENOENT:
            already_seen = set()
        else:
            raise
    while True:
        log.debug('fetching DMs')
        try:
            fetched = api.direct_messages()
        except tweepy.TweepError, e:
            log.error('while fetching DMs: %s', e.reason)
            if 'status code = 503' in e.reason:
                seconds *= 1.2
                log.info('Got 503, now sleeping %.2f seconds', seconds)
        dms = dict([(dm.id, dm) for dm in fetched])
        log.debug('%d DMs', len(dms.keys()))
        new = set(dms.keys()) - already_seen
        log.debug('%d new DMs', len(new))
        for id in new:
            dm = dms[id]
            # prevent infinite loops
            if dm.sender.screen_name == my_screen_name:
                log.debug('ignoring DM %r %r from myself', id, dm.text)
            else:
                log.info('<< %s: %r', dm.sender.screen_name, dm.text)
                reply = handler(dm.sender.screen_name, dm.text)
                # clamp to max length, to avoid one possible error
                reply = reply[:140]
                if reply:
                    try:
                        # avoid "Whoops, you already said that!"
                        unique_nonce = str(int(time.time()))[-3:]
                        api.send_direct_message(
                                screen_name=dm.sender.screen_name,
                                text=unique_nonce + ' ' + reply)
                        log.info('>> %s: %r', dm.sender.screen_name, reply)
                    except tweepy.TweepError, e:
                        log.error('TweepError during reply: %s', e.reason)
        # dms will only ever contain the latest 20 dms; by storing those
        # ids we will not have an ever-growing already_seen list.
        already_seen = set(dms.keys())
        cPickle.dump(already_seen, file(already_seen_filename, 'w'))
        log.debug('sleeping')
        time.sleep(seconds)
