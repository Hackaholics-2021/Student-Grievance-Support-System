class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    # format : mysql://username:password@locahost/dbname
     DATABASE_URI = 'mysql://root:admin@127.0.0.1:3306/student'
    
	
class DevelopmentConfig(Config):
    DEBUG = True

class SECRET_KEY(Config):
    SECRET_KEY = 'student'