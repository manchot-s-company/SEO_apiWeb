from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float,ForeignKey
from sqlalchemy.orm import relationship

class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True, index=True)
    adress = Column(String)
    equipments=relationship('Equipment', backref='house')
    
    
class Equipment(Base):
    __tablename__="equipaments"
    
    id=Column(Integer, primary_key=True,index=True)
    name=Column(String)
    avr_hours=Column(Float)
    kwh=Column(Float)
    
    house_id=Column(Integer, ForeignKey("houses.id"))
    
    


    
    
    


    
    
    



    



    
    