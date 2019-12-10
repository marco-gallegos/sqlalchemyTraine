from Models import *
from Models.conexion import Engine, Session
# la conexion a la db
# ahora en archivo conexion

# objeto que heredara la capacidad de orm
# se mueve a user.py
# ORM_Base = declarative_base()

# aqui va el codigo del modelo

# crear los schema
# se debe usar la misma instancia del engine que define los modelos
User.ORM_Base.metadata.create_all(Engine)

# instanciar un objeto user solo instancia no se guarda aun pero valida datos
marco = User.User(nombre="Marco Gallegos", email="ma_galeza@hotmail.com", password="no sea chismoso :v")

# la session es el objeto responsable de llevar/traer a la bd
# la sesion se movio a conexion
# Session = sessionmaker(bind=Engine)
ORM = Session()

ORM.add(marco)
# guardar cambios
ORM.commit()

# cerrar la instancia del ORM
ORM.close()