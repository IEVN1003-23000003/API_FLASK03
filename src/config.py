##para base de datos

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'Localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'api_utl'

config={
    'development':DevelopmentConfig
}