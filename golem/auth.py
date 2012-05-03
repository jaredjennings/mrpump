import tweepy

def get_api(config):
    consumer_key = config.item('app', 'key')
    consumer_secret = config.item('app', 'secret')

    me = config.item('global', 'screen name')
    me_oauth_token = config.item(me, 'token')
    me_oauth_secret = config.item(me, 'secret')

    oa = tweepy.OAuthHandler(consumer_key, consumer_secret)
    oa.set_access_token(developer_oauth_token, developer_oauth_secret)

    api = tweepy.API(oa)
    return api
