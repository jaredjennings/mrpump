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

class Forehead(object):
    """On or in a golem's forehead is written what he is to do."""
    
    def __init__(self):
        self.log = logging.getLogger('Forehead')
        self.chems = []

    def add(self, chem):
        self.chems.append(chem)

    def __call__(self, sender_screen_name, text, reply):
        # avoid "Whoops, you already said that!"
        text = text.lstrip('0123456789 ')
        done = False
        for c in self.chems:
            if not done and c.appliesTo(text):
                self.log.info('%r gets message %s', c, text)
                try:
                    c(sender_screen_name, text, reply)
                    done = True
                except Exception, e:
                    self.log.error('while dealing with message %r', message)
                    self.log.exception(e)
        if not done:
            reply('did not understand %s', text)
