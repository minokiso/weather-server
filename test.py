from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from loggers import http_server_logger
import django
import os

from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from loggers import http_server_logger

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

django.setup()

if __name__ == '__main__':
    def test():
        now = datetime.now()
        print(now)
        http_server_logger.debug(now)


    scheduler = BlockingScheduler()
    scheduler.add_job(test, 'interval', seconds=2)
    try:
        print("scheduler start")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
