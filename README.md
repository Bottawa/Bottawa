Bytown Bot
==========

sudo apt-get install python-pip python-yaml python-mysqldb

install python twitter

    $ git clone https://github.com/sixohsix/twitter.git
    $ cd twitter/
    $ sudo python setup.py install

edited /usr/local/lib/python2.7/dist-packages/tweetpony/api.py to remove q is None business.

Set timezone for view

mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root -p mysql

