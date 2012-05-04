import logging
import tweepy
import cPickle
import errno
import time

def loop(api, seconds, already_seen_filename, my_screen_name, handler):
    log = logging.getLogger('drive')
    try:
        already_seen = cPickle.load(file(already_seen_filename))
    except IOError, e:
        if e.errno == errno.ENOENT:
            already_seen = set()
        else:
            raise
    while True:
        log.debug('fetching DMs')
        fetched = api.direct_messages()
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
                        log.error('during reply: %r', e)
        # dms will only ever contain the latest 20 dms; by storing those
        # ids we will not have an ever-growing already_seen list.
        already_seen = set(dms.keys())
        cPickle.dump(already_seen, file(already_seen_filename, 'w'))
        log.debug('sleeping')
        time.sleep(seconds)
