import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG_MODE = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@127.0.0.1:5432/postgres'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@127.0.0.1:5432/postgres'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@127.0.0.1:5432/postgres'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
