from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Studentdata(Base):
    __tablename__ = 'studentdata'
    id = Column(Integer, primary_key=True)
    username = Column(String, primary_key=False)
    password = Column(String, primary_key=False)

