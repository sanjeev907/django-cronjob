import logging

logger = logging.getLogger(__name__)


def my_scheduled_job():
  print("Hello World")
  logger.info("Cron Job")