from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone_number = Column(String)
    card_id = Column(Integer)
    
    sellers = relationship("Seller", back_populates="user")

class Seller(Base):
    __tablename__ = 'sellers'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    house_id = Column(Integer)
    photo = Column(String)

    user = relationship("User", back_populates="sellers")
