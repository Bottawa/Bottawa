import logging, time, json, yaml, tweetpony

logger = logging.getLogger('fetchTweets')
hdlr = logging.FileHandler('./log/fetchTweets.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

logger.info('Start time')

config = json.load(open('config.json'))

POIs = yaml.load(open("twitter.yaml", 'r'))['POIs']
logger.debug('loaded twitter yaml')

api = tweetpony.API(consumer_key = config[u'consumer_key'], consumer_secret = config[u'consumer_secret'], access_token = config[u'access_token'], access_token_secret = config[u'access_token_secret'])
logger.debug('api loaded')

for POI in POIs:
    print POI
    for area in POIs[POI]['areas']:
        geocode_string = str(area['lat']) + ","+ str(area['long']) + "," + str(area['range'])
    	output = api.search_tweets(q='',geocode=geocode_string)
        print output
        time.sleep(0.5)

