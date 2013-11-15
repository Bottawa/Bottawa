import logging, time, json, yaml, MySQLdb

logger = logging.getLogger('databaseSetup')
hdlr = logging.FileHandler('./log/databaseSetup.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

logger.info('Start time')

config = yaml.load(open('config.yaml'))
logger.debug('loaded config yaml')
db = MySQLdb.connect(host = config['database']['host'], user = config['database']['user'], passwd = config['database']['passwd'], db = config['database']['db'])
logger.debug('db connected')

cur = db.cursor() 
cur.execute("""
SET time_zone = '+0:00';

DROP TABLE IF EXISTS Regions;

CREATE TABLE Regions
(
region_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
name VARCHAR( 64 ) NOT NULL
);

DROP TABLE IF EXISTS Areas;

CREATE TABLE Areas
(
area_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
region_id INT NOT NULL,
lat FLOAT(10,6) NOT NULL,
`long` FLOAT(10,6) NOT NULL,
`range` FLOAT NOT NULL
);

DROP TABLE IF EXISTS Tweets;

CREATE TABLE Tweets
(
tweet_id BIGINT PRIMARY KEY NOT NULL,
usr_id BIGINT NOT NULL,
lat FLOAT(10,6) default NULL,
`long` FLOAT(10,6) default NULL,
text VARCHAR(160) NOT NULL,
retweeted TINYINT(1) NULL,
created_at DATETIME NULL,
updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS TwitterUsers;

CREATE TABLE TwitterUsers
(
usr_id BIGINT PRIMARY KEY NOT NULL,
screen_name VARCHAR(64) NOT NULL,
name  VARCHAR(64) NULL,
location VARCHAR(32) NULL,
followers_count INT NULL,
friends_count INT NULL,
statuses_count INT NULL,
time_zone VARCHAR(32) NULL,
profile_image_url VARCHAR(128) NULL,
created_at DATETIME NULL,
imported_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS TweetUserMentions;

CREATE TABLE TweetUserMentions
(
tweet_id BIGINT NOT NULL,
usr_id BIGINT NOT NULL,
CONSTRAINT pk_TwitterUserMentions PRIMARY KEY (tweet_id,usr_id)
);

DROP TABLE IF EXISTS TweetHashtags;

CREATE TABLE TweetHashtags
(
tweet_id BIGINT NOT NULL,
hashtag VARCHAR(32) NOT NULL,
CONSTRAINT pk_TweetHashtags PRIMARY KEY (tweet_id,hashtag)
);

DROP TABLE IF EXISTS TweetUrls;

CREATE TABLE TweetUrls
(
tweet_id BIGINT NOT NULL,
url VARCHAR(256) NOT NULL,
CONSTRAINT pk_TweetUrls PRIMARY KEY (tweet_id,url)
);

DROP TABLE IF EXISTS TweetRegions;

CREATE TABLE TweetRegions
(
tweet_id BIGINT NOT NULL,
region_id INT NOT NULL,
CONSTRAINT pk_TweetRegion PRIMARY KEY (tweet_id,region_id)
);

DROP VIEW IF EXISTS TweetsView;

CREATE VIEW TweetsView AS
  SELECT
    tu.name AS user_name,
    t.text,
    CONVERT_TZ(t.created_at, 'GMT', 'America/New_York') AS created_at,
    r.name AS region_name,
    t.lat,
    t.long
  FROM
    Tweets AS t
    INNER JOIN TwitterUsers AS tu ON t.usr_id = tu.usr_id
    INNER JOIN TweetRegions AS tr ON t.tweet_id = tr.tweet_id
    INNER JOIN Regions AS r ON tr.region_id = r.region_id
  ORDER BY t.created_at DESC;

-- Insert region data
INSERT INTO Regions (`region_id`, `name`) VALUES ('1', 'Byward Market'), ('2', 'Parliment Hill'), ('3', 'Elgin St'), ('4', 'City Hall'), ('5', 'Confederation Park'), ('6', 'Majors Hill Park'), ('7', 'University of Ottawa'), ('8', 'Dows lake'), ('9', 'Canadian Museum of Nature'), ('10', 'Westboro Beach'), ('11', 'Canadian War Museum'), ('12', 'Ottawa');

INSERT INTO Areas (`area_id`, `region_id`, `lat`, `long`, `range`) VALUES ('1', '1', '45.428629', '-75.69311', '0.2'), ('2', '2', '45.424344', '-75.699259', '0.2'), ('3', '3', '45.413485', '-75.686581', '0.2'), ('4', '4', '45.420624', '-75.69059', '0.2'), ('5', '5', '45.422462', '-75.691706', '0.2'), ('6', '6', '45.427477', '-75.697517', '0.2'), ('7', '7', '45.423877', '-75.684668', '0.3'), ('8', '7', '45.421468', '-75.681041', '0.3'), ('9', '8', '45.395165', '-75.702459', '0.4'), ('10', '9', '45.412784', '-75.688612', '0.1'), ('11', '10', '45.395444', '-75.76112', '0.1'), ('12', '11', '45.416527', '-75.717651', '0.2'), ('13', '12', '45.411', '-75.698', '40');


""")

for row in cur.fetchall() :
    print row[0]