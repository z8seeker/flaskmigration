import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SPIDER_HOST = "qunluo-apis-test-01.guokr.com"
    AUTh_HOST = "qunluo-apis-test-01.guokr.com"
