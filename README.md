Bottawa
=======

sudo apt-get install python-pip python-yaml python-mysqldb

sudo pip install tweetpony

edited /usr/local/lib/python2.7/dist-packages/tweetpony/api.py to remove q is None business.


## Database setup

### Twitter

    USE <dbname>;
    
    # Tables

    CREATE TABLE Tweets
    (
    id BIGINT PRIMARY KEY NOT NULL,
    usr_id INT NOT NULL,
    coordinates GEOGRAPHY NULL,
    text VARCHAR(160) NOT NULL,
    created DATETIME NULL,
    imported DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    
    CREATE TABLE TwitterUsers
    (
    id INT PRIMARY KEY NOT NULL,
    screen_name VARCHAR(32) NOT NULL,
    name  VARCHAR(32) NULL,
    location VARCHAR(32) NULL,
    protected BIT NULL,
    verified BIT NULL,
    followers_count INT NULL,
    friends_count INT NULL,
    statuses_count INT NULL,
    time_zone VARCHAR(32) NULL,
    utc_offset FLOAT NULL,
    profile_image_url VARCHAR(128) NULL,
    created_at DATETIME,
    imported_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    
    CREATE TABLE TweetsAnatomize
    (
    tweet_id BIGINT NOT NULL,
    term VARCHAR(32) NOT NULL,
    CONSTRAINT pk_TweetsAnatomize PRIMARY KEY (tweet_id,term)
    )
    
    CREATE TABLE TweetUserMentions
    (
    tweet_id BIGINT NOT NULL,
    usr_id INT NOT NULL,
    CONSTRAINT pk_TwitterUserMentions PRIMARY KEY (tweet_id,usr_id)
    )
    
    CREATE TABLE TweetHashtags
    (
    tweet_id BIGINT NOT NULL,
    hashtag VARCHAR(32) NOT NULL,
    CONSTRAINT pk_TweetHashtags PRIMARY KEY (tweet_id,hashtag)
    )
    
    CREATE TABLE TweetUrls
    (
    tweet_id BIGINT NOT NULL,
    url VARCHAR(256) NOT NULL,
    CONSTRAINT pk_TweetUrls PRIMARY KEY (tweet_id,url)
    )
    
    CREATE TABLE TweetRegions
    (
    tweet_id BIGINT NOT NULL,
    region VARCHAR(32) NOT NULL,
    CONSTRAINT pk_TweetRegion PRIMARY KEY (tweet_id,region)
    )
