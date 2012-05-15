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
import time

class Waiter(object):
    """Wait in between checking messages.

    We want to be nice to Twitter, but also responsive to the user. So when
    Twitter returns an error, wait longer, and when it doesn't, move back
    toward the configured wait time.
    """

    # When a problem is encountered, the wait time is multiplied by this.
    problem_multiplier = 1.3

    # How quickly our to_wait value returns to the initial_wait.
    # 0.0 means that it goes back in one step; 1.0 means it never goes back.
    # Less than 0 or more than 1 are not useful for our purposes.
    decay_constant = 0.75

    def __init__(self, initial_wait):
        self.initial_wait = initial_wait
        self.to_wait = initial_wait
        self.log = logging.getLogger('Waiter')

    def problem(self):
        self.log.debug('Problem encountered. Increasing wait time.')
        self.to_wait *= self.problem_multiplier

    def wait(self):
        self.log.info('Waiting %.2f seconds.', self.to_wait)
        time.sleep(self.to_wait)
        # decay to_wait toward initial_wait exponentially
        self.to_wait = ((self.to_wait - self.initial_wait) * 
                        self.decay_constant) + self.initial_wait
