import logging, time, json, yaml, MySQLdb
from twitter import *

logger = logging.getLogger('fetchTweets')
hdlr = logging.FileHandler('./log/fetchTweets.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

logger.info('Start time')

def load_config():
    global config
    config = yaml.load(open('config.yaml'))
    logger.debug('loaded config yaml')

def connect_db():
    global db
    db = MySQLdb.connect(host = config['database']['host'], user = config['database']['user'], passwd = config['database']['passwd'], db = config['database']['db'])
    logger.debug('db connected')

def load_api():
    global POIs
    POIs = yaml.load(open("twitter.yaml", 'r'))['POIs']
    logger.debug('loaded twitter yaml')

def connect_api():
    global api
    api = Twitter(auth=OAuth(config['twitter']['access_token'], config['twitter']['access_token_secret'], config['twitter']['consumer_key'], config['twitter']['consumer_secret']))
    logger.debug('api loaded')

def query_twitter(lat, long, range):
    geocode_string = str(lat) + ","+ str(long) + "," + str(range)
    return api.search.tweets(q='',geocode=geocode_string,count=100)

def to_esc_sql(text):
    return text.replace("'", "''")

def insert_tweet(tweet):
    id = tweet['id']
    usr_id =  tweet['user']['id']
    text = tweet['text'].encode('ascii', 'ignore')
    created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
    coordinates = tweet['coordinates']
    print id
    print usr_id
    print text
    print created_at
    print coordinates


def organise_raw_tweets(raw_tweets, POI):
    print POI
    for tweet in raw_tweets['statuses']:
        insert_tweet(tweet)




load_config()
connect_db()
load_api()
connect_api()


for POI in POIs:
    for area in POIs[POI]['areas']:
        organise_raw_tweets(query_twitter(area['lat'], area['long'], area['range']),POI)
        
        time.sleep(0.5)


'''
cur = db.cursor() 
cur.execute("SELECT '1' AS test")

for row in cur.fetchall() :
    print row[0]
'''