# mrpump, a twitter bot
# Copyright (C) 2012 Jared Jennings
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
                def reply(text):
                    # clamp to max length, to avoid one possible error
                    text = text[:140]
                    try:
                        # avoid "Whoops, you already said that!"
                        unique_nonce = str(int(time.time()))[-3:]
                        api.send_direct_message(
                                screen_name=dm.sender.screen_name,
                                text=unique_nonce + ' ' + text)
                        log.info('>> %s: %r', dm.sender.screen_name, text)
                    except tweepy.TweepError, e:
                        log.error('TweepError during reply: %s', e.reason)
                handler(dm.sender.screen_name, dm.text, reply)
        # dms will only ever contain the latest 20 dms; by storing those
        # ids we will not have an ever-growing already_seen list.
        already_seen = set(dms.keys())
        cPickle.dump(already_seen, file(already_seen_filename, 'w'))
        log.debug('sleeping')
        time.sleep(seconds)
