from sqlalchemy import Column, Integer, String, ForeignKey
from . import db

class TaxRecord(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    income = Column(Integer, nullable=False)
    deductions = Column(Integer, nullable=True)
    state = Column(String(2), nullable=False)
    filing_status = Column(String(20), nullable=False)
    tax_due = Column(Integer, nullable=False)