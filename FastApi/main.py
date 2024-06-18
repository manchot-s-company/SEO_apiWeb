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
    name:str
    avr_hours: float
    kwh: float

class EquipamentModel(EquipmentBase):
    id:int
    class Config:
        orm_model=True



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency=Annotated[Session, Depends(get_db)]
models.Base.metadata.create_all(bind=engine)

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
    
    