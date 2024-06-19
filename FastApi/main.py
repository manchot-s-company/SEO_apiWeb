from fastapi import FastAPI, HTTPException, Depends
from typing  import Annotated, List 
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models 
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins=[
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']    
) 

class EquipmentBase(BaseModel):
    name: str
    avr_hours: float
    kwh: float
    house_id: int
   

class EquipamentModel(EquipmentBase):
    id:int
    
    class Config:
        orm_model=True

class HouseBase(BaseModel):
    adress: str

class HouseModel(HouseBase):
    id: int
    equipments: list[EquipamentModel]
    
    class Config:
        orm_mode=True
        

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency=Annotated[Session, Depends(get_db)]
models.Base.metadata.create_all(bind=engine)


#equipments
@app.post("/equipament/", response_model=EquipamentModel)
async def create_equipament(equipament:EquipmentBase, db: db_dependency):
    db_equipament=models.Equipment(**equipament.dict())
    db.add(db_equipament)
    db.commit()
    db.refresh(db_equipament)
    return db_equipament

@app.get("/equipament/", response_model=List[EquipamentModel])
async def read_equipament(db:db_dependency,skip:int=0,limit:int=500):
    equipaments=db.query(models.Equipment).offset(skip).limit(limit).all()
    return equipaments

#houses

@app.post("/house/", response_model=HouseModel)
async def create_house(house: HouseBase, db: db_dependency):
    db_house = models.House(**house.dict())
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house
    
@app.get("/house/", response_model=List[HouseModel])
async def read_house(db:db_dependency,skip:int=0,limit:int=100):
    houses=db.query(models.House).offset(skip).limit(limit).all()
    return houses
  
    