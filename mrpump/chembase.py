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

class ChemBase(object):
    def __init__(self):
        self.log = logging.getLogger('Handler')
        pass

    def __call__(self, sender_screen_name, message, reply):
        # avoid "Whoops, you already said that!"
        message = message.lstrip('0123456789 ')
        if ' ' in message:
            firstword, rest = message.split(' ', 1)

        else:
            firstword = message
            rest = ''
        try:
            name = '_msg_' + firstword
            method = getattr(self, name)
            self.log.debug('calling %s with %r', name, rest)
        except AttributeError:
            self.log.error('could not handle message %r', message)
            reply('did not understand')
        try:
            method(rest, reply)
        except Exception, e:
            self.log.error('while dealing with message %r', message)
            self.log.error('%r', e)
            reply('error: %r' % e)
