from dataclasses import Field
from datetime import datetime
from typing import Optional
from sqlalchemy import Boolean, DateTime, String, Integer, Float, ForeignKey, Date, func, Text, Column
from sqlalchemy.orm import relationship
from database.db import Base


class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer, nullable=False)
    discription = Column(Text, nullable=False)
    is_selled = Column(Boolean, default=True)

    address_id = Column(Integer, ForeignKey('addresses.id', ondelete='CASCADE'), nullable=False)
    type_id = Column(Integer, ForeignKey('house_types.id', ondelete='CASCADE'), nullable=False)
    character_id = Column(Integer, ForeignKey('characteristics.id', ondelete='CASCADE'), nullable=False)

    address = relationship("Address", back_populates="house")
    type = relationship("HouseType", back_populates="house")
    characteristics = relationship("Characteristic", back_populates="house")
    deals = relationship("Deal", back_populates="house")


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, index=True)
    house_number = Column(Integer, nullable=False)
    apartment_number = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)

    city_id = Column(Integer, ForeignKey('cities.id', ondelete='CASCADE'), nullable=False)
    district_id = Column(Integer, ForeignKey('districts.id', ondelete='CASCADE'), nullable=False)
    street_id = Column(Integer, ForeignKey('streets.id', ondelete='CASCADE'), nullable=False)

    city = relationship("City", back_populates="address")
    district = relationship("District", back_populates="address")
    street = relationship("Street", back_populates="address")
    houses = relationship("House", back_populates="address")


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), nullable=False)

    address = relationship("Address", back_populates="city")


class Dictrict(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), nullable=False)

    address = relationship("Address", back_populates="district")


class Street(Base):
    __tablename__ = 'streets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), nullable=False)

    address = relationship("Address", back_populates="street")


class HouseType(Base):
    __tablename__ = 'house_types'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), nullable=False)

    house = relationship("House", back_populates="type")


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True, index=True)
    photo_link = Column(String(100), nullable=False)

    house_photo = relationship("HousePhoto", back_populates="photo")


class HousePhoto(Base):
    __tablename__ = 'house_photos'

    id = Column(Integer, primary_key=True, index=True)

    house_id = Column(Integer, ForeignKey('houses.id', ondelete='CASCADE'), nullable=False)
    photo_id = Column(Integer, ForeignKey('photos.id', ondelete='CASCADE'), nullable=False)

    house = relationship("House", back_populates="house_photo")
    photo = relationship("Photo", back_populates="house_photo")


class Characteristic(Base):
    __tablename__ = 'characteristics'

    id = Column(Integer, primary_key=True, index=True)
    count_room = Column(Integer, nullable=False)
    is_furnitures = Column(Boolean, nullable=False)
    year_of_construction = Column(Integer, nullable=False)
    area = Column(Float, nullable=False)

    house = relationship("House", back_populates="characteristics")


class Deal(Base):
    __tablename__ = 'deals'

    id = Column(Integer, primary_key=True, index=True)
    transaction_time = Column(DateTime(timezone=True), default=func.now())
    final_price = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    seller_id = Column(Integer, ForeignKey('sellers.id', ondelete='CASCADE'), nullable=False)
    house_id = Column(Integer, ForeignKey('houses.id', ondelete='CASCADE'), nullable=False)

    user = relationship("User", back_populates="deal")
    seller = relationship("Seller", back_populates="deal")
    house = relationship("House", back_populates="deal")