from sqlalchemy import Boolean, DateTime, String, Integer, Float, ForeignKey, Text, Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(75), nullable=False)
    lastname = Column(String(75), nullable=False)
    email = Column(String(75), nullable=False, unique=True)
    password = Column(String(75), nullable=False)
    photo = Column(String(255), nullable=True)
    phone_number = Column(String(20), nullable=False)

    card_id = Column(Integer, ForeignKey('cards.id', ondelete='CASCADE'), nullable=True)
    card = relationship("Card", back_populates="user")
    deals = relationship("Deal", back_populates="user")
    seller_houses = relationship("SellerHouse", back_populates="user")


class SellerHouse(Base):
    __tablename__ = 'seller_houses'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    house_id = Column(Integer, ForeignKey('houses.id', ondelete='CASCADE'), nullable=False)

    user = relationship("User", back_populates="seller_houses")
    house = relationship("House", back_populates="seller_houses")


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, index=True)
    card_token = Column(String(75), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    user = relationship("User", back_populates="card")


class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    is_selled = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    address_id = Column(Integer, ForeignKey('addresses.id', ondelete='CASCADE'), nullable=False)
    type_id = Column(Integer, ForeignKey('house_types.id', ondelete='CASCADE'), nullable=False)
    characteristic_id = Column(Integer, ForeignKey('characteristics.id', ondelete='CASCADE'), nullable=False)

    address = relationship("Address", back_populates="houses")
    type = relationship("HouseType", back_populates="houses")
    characteristic = relationship("Characteristic", back_populates="houses")
    deals = relationship("Deal", back_populates="house")
    seller_houses = relationship("SellerHouse", back_populates="house")
    house_photos = relationship("HousePhoto", back_populates="house")


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, index=True)
    house_number = Column(String(20), nullable=False)
    apartment_number = Column(Integer, nullable=True)
    floor = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

    city_id = Column(Integer, ForeignKey('cities.id', ondelete='CASCADE'), nullable=False)
    district_id = Column(Integer, ForeignKey('districts.id', ondelete='CASCADE'), nullable=False)
    street_id = Column(Integer, ForeignKey('streets.id', ondelete='CASCADE'), nullable=False)

    city = relationship("City", back_populates="addresses")
    houses = relationship("House", back_populates="address")


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    district_id = Column(Integer, ForeignKey('districts.id', ondelete='CASCADE'), nullable=False)

    addresses = relationship("Address", back_populates="city")
    district = relationship("District", back_populates="cities")


class District(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    street_id = Column(Integer, ForeignKey('streets.id', ondelete='CASCADE'), nullable=False)

    street = relationship("Street", back_populates="districts")
    cities = relationship("City", back_populates="district")


class Street(Base):
    __tablename__ = 'streets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    districts = relationship("District", back_populates="street")


class HouseType(Base):
    __tablename__ = 'house_types'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    houses = relationship("House", back_populates="type")


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True, index=True)
    photo_link = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    house_photos = relationship("HousePhoto", back_populates="photo")


class HousePhoto(Base):
    __tablename__ = 'house_photos'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

    house_id = Column(Integer, ForeignKey('houses.id', ondelete='CASCADE'), nullable=False)
    photo_id = Column(Integer, ForeignKey('photos.id', ondelete='CASCADE'), nullable=False)

    house = relationship("House", back_populates="house_photos")
    photo = relationship("Photo", back_populates="house_photos")


class Characteristic(Base):
    __tablename__ = 'characteristics'

    id = Column(Integer, primary_key=True, index=True)
    count_room = Column(Integer, nullable=False)
    is_furnished = Column(Boolean, nullable=False)
    year_of_construction = Column(Integer, nullable=False)
    area = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    houses = relationship("House", back_populates="characteristic")


class Deal(Base):
    __tablename__ = 'deals'

    id = Column(Integer, primary_key=True, index=True)
    transaction_time = Column(DateTime(timezone=True), default=func.now())
    final_price = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    house_id = Column(Integer, ForeignKey('houses.id', ondelete='CASCADE'), nullable=False)

    user = relationship("User", back_populates="deals")
    house = relationship("House", back_populates="deals")
