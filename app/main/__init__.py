import logging
import logging.handlers
import os

from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name, basedir

db = SQLAlchemy()


def getLogger():
    logdir = os.path.join(basedir, 'logs')
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    logfile = '%s/%s.log' % (logdir, 'think-link-coin-app')
    loglevel = logging.INFO
    logger = logging.getLogger('think-link-coin-app')
    logger.setLevel(loglevel)
    if logger.handlers is not None and len(logger.handlers) >= 0:
        for handler in logger.handlers:
            logger.removeHandler(handler)
        logger.handlers = []
    loghandler = logging.handlers.RotatingFileHandler(logfile, maxBytes=500 * 1024, backupCount=100)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    loghandler.setFormatter(formatter)
    logger.addHandler(loghandler)
    return loghandler


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv('BOILERPLATE_ENV') or 'dev'])
    db.init_app(app)
    app.logger.addHandler(getLogger())
    return app
