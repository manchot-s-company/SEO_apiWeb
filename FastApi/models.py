from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Equipment(Base):
    __tablename__="equipaments"
    
    id=Column(Integer, primary_key=True,index=True)
    name=Column(String)
    avr_hours=Column(Float)
    kwh=Column(Float)