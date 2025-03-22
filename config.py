"""Flask application configuration."""
import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    WTF_CSRF_ENABLED = True
    # Default to localhost for security
    HOST = os.environ.get('HOST', '127.0.0.1')
    PORT = int(os.environ.get('PORT', 5000))

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    # In production, still default to localhost unless explicitly configured
    HOST = os.environ.get('HOST', '127.0.0.1')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False
    # In development, still use localhost by default
    HOST = os.environ.get('HOST', '127.0.0.1')

class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False
    SERVER_NAME = 'localhost'
    # Testing should always use localhost
    HOST = '127.0.0.1'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
