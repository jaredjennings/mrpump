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
