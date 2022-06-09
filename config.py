
#HOSTNAME = '127.0.0.1'
#PORT     = '3306'
#DATABASE = 'J.A.R.V.I.S'
#USERNAME = 'root'
#PASSWORD = 'hezhenmin2000'
HOSTNAME = 'cheopsmysql01.dev.zbjwork.com'
PORT     = '3306'
DATABASE = 'python9991e24'
USERNAME = 'mysql-rw-python9991e24'
PASSWORD = 'aujc]_??1694PQSH'
DB_URI   = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATION = True

SECRET_KEY = 'hkfafnakiefakfnafafc'


#邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "ilikedietpepsi@qq.com"
MAIL_PASSWORD = "yhiqbxxultptchdh"
MAIL_DEFAULT_SENDER = "ilikedietpepsi@qq.com"
