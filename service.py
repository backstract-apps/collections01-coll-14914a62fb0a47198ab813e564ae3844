from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_studentdata(db: Session):

    studentdata_all = db.query(models.Studentdata).order_by(models.Studentdata.id).all()
    res = {
        'studentdata_all': studentdata_all,
    }
    return res

async def get_studentdata_id(db: Session, id: int, category: str):

    studentdata_one = db.query(models.Studentdata).filter(models.Studentdata.id == 'id').first()
    res = {
        'studentdata_one': studentdata_one,
    }
    return res

async def post_studentdata(db: Session, name: UploadFile):

    bucket_name = "backstaract-d"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        's3',
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1"
    )

    # Read file content
    file_content = await file.read()

    name = file.filename
    file_path = file_path  + '/' + name
    # Upload the file to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_path,
        Body=file_content
    )

    # Generate the URL for the uploaded file

    file_type = Path(file.filename).suffix
    file_size = 200
    file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{file_path}"

    students_all = file_url

    bucket_name = "backstaract-d"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        's3',
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1"
    )

    # Read file content
    file_content = await file.read()

    name = file.filename
    file_path = file_path  + '/' + name
    # Upload the file to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_path,
        Body=file_content
    )

    # Generate the URL for the uploaded file

    file_type = Path(file.filename).suffix
    file_size = 200
    file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{file_path}"

    uploaded_file_url = file_url
    res = {
        'studentdata_inserted_record': students_all,
    }
    return res

async def put_studentdata_id(db: Session, raw_data: schemas.PutStudentdataId):
    id:str = raw_data.id
    username:str = raw_data.username
    password:str = raw_data.password


    studentdata_edited_record = db.query(models.Studentdata).filter(models.Studentdata.id == id).first()
    for key, value in {'id': id, 'username': username, 'password': password}.items():
          setattr(studentdata_edited_record, key, value)
    db.commit()
    db.refresh(studentdata_edited_record)
    studentdata_edited_record = studentdata_edited_record

    res = {
        'studentdata_edited_record': studentdata_edited_record,
    }
    return res

async def delete_studentdata_id(db: Session, id: int):

    studentdata_deleted = None
    record_to_delete = db.query(models.Studentdata).filter(models.Studentdata.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        studentdata_deleted = record_to_delete
    res = {
        'studentdata_deleted': studentdata_deleted,
    }
    return res

async def post_studentsdetails(db: Session, fisrtname: str, lastname: str, id: int):

    record_to_be_added = {'id': id, 'username': fisrtname, 'password': lastname}
    new_studentdata = models.Studentdata(**record_to_be_added)
    db.add(new_studentdata)
    db.commit()
    db.refresh(new_studentdata)
    studentsall = new_studentdata
    res = {
        'student_all1': fisrtname,
    }
    return res

