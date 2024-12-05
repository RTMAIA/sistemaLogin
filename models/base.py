from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

USUARIO = 'root'
PASSWORD = ''
HOST = 'localhost'
DB = 'sistema_login'
PORT = '3306'

CONNECTION = f'mysql+pymysql://{USUARIO}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(CONNECTION, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()