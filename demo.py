from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base
import sqlalchemy as db

engine = db.create_engine('postgresql+psycopg2://postgres:trangtruong@localhost:5432/ggbenefits')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'clinics'
    name = Column(String, primary_key=True)
    address = Column(String)
    phone = Column(Integer)
    lat = Column(Float)
    lng = Column(Float)

new_customer = Customer(name='D', address='567 RFV', phone = 1234567891, lat=567.789, lng=567.789)
session.add(new_customer)
for i in session.query(Customer):
    print(f'{i.name, i.address, i.phone, i.lat, i.lng}')
