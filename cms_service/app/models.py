from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
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


class TakePoint(Base):
    __tablename__ = "pick_up_point"

    id = Column(Integer, primary_key=True)
    phone1 = Column(Text)
    phone2 = Column(Text)
    phone3 = Column(Text)
    email1 = Column(Text)
    address = Column(Text)
    coordinate_x = Column(Text)
    coordinate_y = Column(Text)
    email2 = Column(Text)

    time_id = Column(Integer, ForeignKey("pick_up_point_time.id"))
    title_id = Column(Integer, ForeignKey("pick_up_point_stock_title.id"))

    time = relationship("TimePoint", back_populates="pick_up_point")
    title = relationship("TitlePoint", back_populates="pick_up_point")
    desc = relationship("DescPoint", back_populates="pick_up_point")


class TimePoint(Base):
    __tablename__ = "pick_up_point_time"

    id = Column(Integer, primary_key=True)
    mon = Column(Text)
    tue = Column(Text)
    wen = Column(Text)
    thu = Column(Text)
    fri = Column(Text)
    sat = Column(Text)
    sun = Column(Text)

    pick_up_point = relationship("TakePoint", back_populates="time")


class TitlePoint(Base):
    __tablename__ = "pick_up_point_stock_title"

    id = Column(Integer, primary_key=True)
    title = Column(Text)

    pick_up_point = relationship("TakePoint", back_populates="title")


class DescPoint(Base):
    __tablename__ = "pick_up_point_stock_description"

    id = Column(Integer, primary_key=True)
    description = Column(Text)

    take_point_id = Column(Integer, ForeignKey("pick_up_point.id"))
    pick_up_point = relationship("TakePoint", back_populates="desc")


class Requisites(Base):
    __tablename__ = 'requisites'

    id = Column(Integer, primary_key=True)
    text = Column(String)


class PrivacyPolicy(Base):
    __tablename__ = 'privacy_policy'

    id = Column(Integer, primary_key=True)
    text = Column(String)


class CdekDeliveryInfo(Base):
    __tablename__ = 'cdek_delivery_info'

    id = Column(Integer, primary_key=True)
    description = Column(String)


class CourierDeliveryTimeInfo(Base):
    __tablename__ = 'courier_delivery_time_info'

    id = Column(Integer, primary_key=True)
    mon = Column(String(30))
    tue = Column(String(30))
    wen = Column(String(30))
    thu = Column(String(30))
    fri = Column(String(30))
    sat = Column(String(30))
    sun = Column(String(30))

    courier_delivery_info = relationship('CourierDeliveryInfo')


class CourierDeliveryInfo(Base):
    __tablename__ = 'courier_delivery_info'

    id = Column(Integer, primary_key=True)
    description = Column(String)

    courier_delivery_time_info_id = Column(Integer, ForeignKey('courier_delivery_time_info.id'))
