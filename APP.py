from Models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# la conexion a la db
Engine = create_engine('mysql+pymysql://root:cucei@localhost:3306/mysqlalchemy', echo=True)

# objeto que heredara la capacidad de orm
ORM_Base = declarative_base()

# aqui va el codigo del modelo

# crear los schema
# ORM_Base.metadata.create_all(Engine)

# instanciar un objeto user solo instancia no se guarda aun pero valida datos
marco = User.User(nombre="Marco Gallegos", email="ma_galeza@hotmail.com", password="noseachismoso:v")

# la session es el objeto responsable de llevar/traer a la bd todo
Session = sessionmaker(bind=Engine)
ORM = Session()

ORM.add(marco)
# guardar cambios
ORM.commit()

# cerrar la instancia del ORM
ORM.close()