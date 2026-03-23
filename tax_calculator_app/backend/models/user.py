from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import db

class User(db.Model):
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    tax_records = relationship('TaxRecord', backref='owner', lazy=True)