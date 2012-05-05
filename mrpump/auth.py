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

import tweepy

def get_api(config):
    consumer_key = config.get('app', 'key')
    consumer_secret = config.get('app', 'secret')

    me = config.get('global', 'screen name')
    me_oauth_token = config.get(me, 'token')
    me_oauth_secret = config.get(me, 'secret')

    oa = tweepy.OAuthHandler(consumer_key, consumer_secret)
    oa.set_access_token(me_oauth_token, me_oauth_secret)

    api = tweepy.API(oa)
    return api
