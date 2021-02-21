class Config(object):
    DEBUG = True
    TESTING = True
    FLASK_RUN_HOST = "0.0.0.0"
    FLASK_RUN_PORT = 8080


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'PRODUCTION'
    TESTING = False


class SitConfig(Config):
    FLASK_ENV = 'SIT'
    
