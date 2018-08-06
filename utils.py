import logging
from logging.handlers import RotatingFileHandler
from article_generator.cmb_article_generator.settings import LOGGING_LEVEL
from mysql import connector


def get_logger():
    logger = logging.getLogger('root')
    FORMAT = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)s - " \
             "%(funcName)20s() ] %(message)s"
    logging.basicConfig(format=FORMAT)
    handler = RotatingFileHandler(
        'run.log', maxBytes=1e8, backupCount=10, encoding='utf-8'
    )
    handler.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(handler)
    logger.setLevel(LOGGING_LEVEL)
    return logger


logger = get_logger()