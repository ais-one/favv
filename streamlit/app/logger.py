import logging

LOGS_FORMAT="%(levelname)s %(asctime)s %(msecs)03d %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOGS_FORMAT)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(LOGS_FORMAT)

# file_handler = logging.FileHandler('activity.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
