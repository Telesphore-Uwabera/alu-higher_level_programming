#!/usr/bin/python3
"""module documentation"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql://root@localhost:3306/mydatabase')
Base.metadata.create_all(engine)
