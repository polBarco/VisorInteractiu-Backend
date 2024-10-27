from sqlalchemy import Column, Integer, Float, Text, Numeric
from geoalchemy2 import Geometry
from .database import Base   

class Cartography(Base):
    __tablename__ = 'cartography_1_5000'
    gid = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry(geometry_type='MULTIPOLYGON', srid=4326))
    element = Column(Text)
    area_m2 = Column("Área m2", Float)
    area_km2 = Column("Área km2", Float)
    longitud = Column("longitud", Float)
    perimet_km = Column("perimet km", Numeric(10, 3))

    def __repr__(self):
        return f"<Cartography(gid={self.gid}, element={self.element})>"