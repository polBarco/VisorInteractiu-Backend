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
    
class CycloneSedimentTransport(Base):
    __tablename__ = 'cyclone_sediment_transport'
    gid = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry(geometry_type='MULTIPOINT', srid=4326))
    id = Column("id", Integer)
    transport = Column("transport", Float)
    percent = Column("percent", Float)

    def __repr__(self):
        return f"<CycloneSedimentTransport(gid={self.gid})>"
    
class CycloneEra5Node(Base):
    __tablename__ = 'cyclone_era5_node'
    gid = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry(geometry_type='MULTIPOINT', srid=4326))
    id = Column("id", Integer)

    def __repr__(self):
        return f"<CycloneEra5Node(gid={self.gid})>"   
    