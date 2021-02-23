class Config(object):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'PRODUCTION'
    TESTING = False


class SitConfig(Config):
    FLASK_ENV = 'SIT'
    
