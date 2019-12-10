from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# clase que hereda de base par servivir como "modelo"
# describe la db
# el init viene predefinido se puede hacer explicito pero no es necesario
ORM_Base = declarative_base()


class User(ORM_Base):
    __tablename__ = "users"

    idusuario = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    email = Column(String(200))
    password = Column(String(200))

if __name__ == "__main__":
    from .conexion import Engine


