from sqlalchemy import Column, Integer, Float, Text, Numeric
from geoalchemy2 import Geometry
from .database import Base   

class Cartography(Base):
    __tablename__ = 'cartography_1_5000'
    gid = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry(geometry_type='MULTIPOLYGON', srid=4326))
    element = Column("element", Text)
    area_m2 = Column("Área m2", Float)
    area_km2 = Column("Área km2", Float)
    longitud = Column("longitud", Float)
    perimet_km = Column("perimet km", Numeric(10, 3))

    def __repr__(self):
        return f"<Cartography(gid={self.gid}, element={self.element})>"

class d50(Base):
    __tablename__ = 'd50'
    gid = Column(Integer, primary_key=True, index=True)
    # id = Column("id", Integer)
    geom = Column(Geometry(geometry_type='MULTIPOINT', srid=4326))
    name = Column("name", Text)
    d50 = Column("d50", Float)

    def __repr__(self):
        return f"<d50(gid={self.gid}, name={self.name})>"
    
class LitoralCells(Base):
    __tablename__ = 'litoral_cells'
    gid = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry(geometry_type='MULTILINESTRING', srid=4326))
    length = Column("length", Float)
    name = Column("name", Text)
    length_km = Column("length_km", Float)
    coord_xfin = Column("coord_xfin", Float)
    coord_yfin = Column("coord_yfin", Float)
    coord_yini = Column("coord_yini", Float)
    coord_xini = Column("coord_xini", Float)
    par_impar = Column("par/impar", Text)

    def __repr__(self):
        return f"<LitoralCells(gid={self.gid}, element={self.element})>"