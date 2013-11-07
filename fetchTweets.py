import json, yaml#, tweetpony

#config = json.load(open('config.json'))

POIs = yaml.load(open("twitter.yaml", 'r'))['POIs']

for POI, areas in POIs.iteritems():
    print POI, areas

for POI in POIs:
    print POI, POIs[POI]

#api = tweetpony.API(consumer_key = config[u'consumer_key'], consumer_secret = config[u'consumer_secret'], access_token = config[u'access_token'], access_token_secret = config[u'access_token_secret'])

#output = api.search_tweets(q='',geocode="45.428629,-75.69311,0.2km")

#print output

