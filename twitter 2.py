import tweepy
 
# personal details
consumer_key =
consumer_secret =
access_token =
access_token_secret = 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="my python tweet !")

