from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Studentdata(BaseModel):
    id: int
    username: str
    password: str


class ReadStudentdata(BaseModel):
    id: int
    username: str
    password: str
    class Config:
        from_attributes = True




class PutStudentdataId(BaseModel):
    id: str
    username: str
    password: str

    class Config:
        from_attributes = True

