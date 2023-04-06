from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from .database import Base


class MainPageBanner(Base):
    __tablename__ = "banner"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    link = Column(Text)
    description = Column(Text)
    image_right = Column(String(255))

    def media_root(self):
        if self.image_right != "":
            self.image_right = "https://dev.ufaelectro.ru/media/" + self.image_right


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    short_description = Column(Text)
    image = Column(String(255))
    date = Column(TIMESTAMP)

    def media_root(self):
        if self.image != "":
            self.image = "https://dev.ufaelectro.ru/media/" + self.image


class Phones(Base):
    __tablename__ = "footer_phones"

    id = Column(Integer, primary_key=True)
    phone = Column(String(20))


class HeaderPhones(Base):
    __tablename__ = "header_phones"

    id = Column(Integer, primary_key=True)
    phone = Column(String(20))


class Addresses(Base):
    __tablename__ = "footer_addresses"

    id = Column(Integer, primary_key=True)
    address = Column(Text)


class Objects(Base):
    __tablename__ = "footer_objects"

    id = Column(Integer, primary_key=True)
    icon = Column(String(255))
    link = Column(String(255))

    def media_root(self):
        if self.icon != "":
            self.icon = "https://dev.ufaelectro.ru/media/" + self.icon


class Promotions(Base):
    __tablename__ = "current_promotions"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    image = Column(String(255))
    date = Column(TIMESTAMP)

    def media_root(self):
        if self.image != "":
            self.image = "https://dev.ufaelectro.ru/media/" + self.image


class MetaTags(Base):
    __tablename__ = 'meta_tags'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    tag = Column(Text)
