# Credenciais da base de dados
DB_USER = 'postgres.qrzgccafofrxstlfvozq'
DB_PASSWORD = '8BIR9Zt7GipXKsYj'
DB_HOST = 'aws-0-eu-central-1.pooler.supabase.com'
DB_PORT = '6543'
DB_NAME = 'postgres'

class Config:
    """Base configuration."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'default_secret_key'  # Para sessões e segurança
    DEBUG = False  # Por padrão, o debug está desativado
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )


class DevelopmentConfig(Config):
    """Configuration for development."""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Ativa o log das queries SQL para debug


class TestingConfig(Config):
    """Configuration for testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    DEBUG = True
    SQLALCHEMY_ECHO = False  # Reduz a verbosidade nos testes


class ProductionConfig(Config):
    """Configuration for production."""
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    DEBUG = False


# Selecionando a configuração baseada na variável de ambiente
configurations = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

def get_config(env=None):
    env = env or 'production'
    return configurations.get(env, ProductionConfig)

