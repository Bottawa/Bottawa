import json, yaml, tweetpony

config = json.load(open('config.json'))

POI = yaml.load(open("twitter.yaml", 'r'))['POI']

api = tweetpony.API(consumer_key = config[u'consumer_key'], consumer_secret = config[u'consumer_secret'], access_token = config[u'access_token'], access_token_secret = config[u'access_token_secret'])

output = api.search_tweets(q='',geocode="45.428629,-75.69311,0.2km")

print output

#try:
#    api.update_status(status = text)
#except tweetpony.APIError as err:
#    print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
#else:
#    print "Yay! Your tweet has been sent!"