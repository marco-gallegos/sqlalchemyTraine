from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Engine = create_engine('mysql+pymysql://root:@localhost:3306/mysqlalchemy', echo=True)

Session = sessionmaker(bind=Engine)