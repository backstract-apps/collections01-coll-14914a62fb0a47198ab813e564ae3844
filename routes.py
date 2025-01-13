from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/studentdata/')
async def get_studentdata(db: Session = Depends(get_db)):
    try:
        return await service.get_studentdata(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/studentdata/id')
async def get_studentdata_id(id: int, category: str, db: Session = Depends(get_db)):
    try:
        return await service.get_studentdata_id(db, id, category)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/studentdata/')
async def post_studentdata(name: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_studentdata(db, name)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/studentdata/id/')
async def put_studentdata_id(raw_data: schemas.PutStudentdataId, db: Session = Depends(get_db)):
    try:
        return await service.put_studentdata_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/studentdata/id')
async def delete_studentdata_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_studentdata_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/studentsdetails')
async def post_studentsdetails(fisrtname: str, lastname: str, id: int, db: Session = Depends(get_db)):
    try:
        return await service.post_studentsdetails(db, fisrtname, lastname, id)
    except Exception as e:
        raise HTTPException(500, str(e))

