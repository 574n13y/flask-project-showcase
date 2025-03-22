"""Flask application configuration."""
import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    WTF_CSRF_ENABLED = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False
    SERVER_NAME = 'localhost'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
