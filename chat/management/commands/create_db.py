import sys
import logging
import MySQLdb

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

rds_host = 'sendbird-cluster.cluster-c79s4ys8xz06.ap-northeast-2.rds.amazonaws.com'
db_name = 'mysql'
user_name = 'member'
password = 'tsod2527'
port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Command(BaseCommand):
    help = 'Creates the initial database'

    def handle(self, *args, **options):
        print('Starting db creation')
        try:
            db = MySQLdb.connect(
                host=rds_host, user=user_name,
                password=password, db='mysql', connect_timeout=5
            )
            c = db.cursor()
            print("connected to db server")
            c.execute("""CREATE DATABASE mysql;""")
            c.execute(
                """GRANT ALL PRIVILEGES ON db_name.* TO 'member' IDENTIFIED BY 'member';"""
            )
            c.close()
            print("closed db connection")
        except:
            logger.error(
                "ERROR: Unexpected error : Could not connect to Mysql instance." 
            )
            sys.exit()