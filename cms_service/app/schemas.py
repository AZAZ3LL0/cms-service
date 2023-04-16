from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class MainPageBannerDTO_Base(BaseModel):
    title: Optional[str]


class MainPageBannerDTO(MainPageBannerDTO_Base):
    id: int
    description: Optional[str]
    image_right: Optional[str]

    class Config:
        orm_mode = True


class BlogDTOBase(BaseModel):
    title: Optional[str]


class BlogDTO(BlogDTOBase):
    id: int
    description: Optional[str]
    short_description: Optional[str]
    image: Optional[str]
    date: Optional[datetime]

    class Config:
        orm_mode = True


class PromotionsDTOBase(BaseModel):
    title: Optional[str]


class PromotionsDTO(PromotionsDTOBase):
    id: int
    description: Optional[str]
    image: Optional[str]
    date: Optional[datetime]

    class Config:
        orm_mode = True


class PhoneBase(BaseModel):
    id: int


class PhonesDTO(PhoneBase):
    phone: Optional[str]

    class Config:
        orm_mode = True


class HeaderPhonesDTO(PhoneBase):
    phone: Optional[str]

    class Config:
        orm_mode = True


class AddressesBase(BaseModel):
    id: int


class AddressesDTO(AddressesBase):
    address: Optional[str]

    class Config:
        orm_mode = True


class ObjectsBase(BaseModel):
    id: int


class ObjectsDTO(ObjectsBase):
    icon: Optional[str]
    link: Optional[str]

    class Config:
        orm_mode = True


class MetaTagsBase(BaseModel):
    id: int


class MetaTagsDTO(MetaTagsBase):
    '''Мета тэги для index.html'''
    title: Optional[str]
    tag: Optional[str]

    class Config:
        orm_mode = True


class DescPointDTO(BaseModel):
    description: str


class Stock(BaseModel):
    title: str
    description: List[DescPointDTO]


class Time(BaseModel):
    mon: Optional[str] = None
    tue: Optional[str] = None
    wen: Optional[str] = None
    thu: Optional[str] = None
    fri: Optional[str] = None
    sat: Optional[str] = None
    sun: Optional[str] = None

    class Config:
        orm_mode = True


class TakePointBase(BaseModel):
    pass


class Coordinate(TakePointBase):
    coordinate_x: str
    coordinate_y: str


class TakePoint(TakePointBase):
    id: str
    address: Optional[str]
    email1: Optional[str]
    email2: Optional[str]
    phone1: Optional[str]
    phone2: Optional[str]
    phone3: Optional[str]
    time: Optional[Time] = None
    coordinates: Optional[Coordinate] = None
    stock: Optional[Stock] = None

    class Config:
        orm_mode = True


class TakePointsDTO(BaseModel):
    data: List[TakePoint]

    class Config:
        orm_mode = True


class DataReq(BaseModel):
    body: Optional[str]

    class Config:
        orm_mode = True


class Requisites(BaseModel):
    data: Optional[DataReq] = None

    class Config:
        orm_mode = True


class DataPrivacyPolicy(BaseModel):
    body: Optional[str]

    class Config:
        orm_mode = True


class PrivacyPolicy(BaseModel):
    data: Optional[DataPrivacyPolicy] = None

    class Config:
        orm_mode = True


class DataDelInfo(BaseModel):
    description: Optional[str]

    class Config:
        orm_mode = True


class DelInfo(BaseModel):
    data: Optional[DataDelInfo] = None

    class Config:
        orm_mode = True


class Courier_Time_Info(BaseModel):
    mon: Optional[str] = None
    tue: Optional[str] = None
    wen: Optional[str] = None
    thu: Optional[str] = None
    fri: Optional[str] = None
    sat: Optional[str] = None
    sun: Optional[str] = None

    class Config:
        orm_mode = True


class Courier_Info(BaseModel):
    description: Optional[str]
    time: Optional[Courier_Time_Info] = None

    class Config:
        orm_mode = True


class Courier_InfoDTO(BaseModel):
    data: List[Courier_Info]

    class Config:
        orm_mode = True


class DataVacancySchema(BaseModel):
    id: Optional[str]
    first_phone: Optional[str]
    second_phone: Optional[str]
    title: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True


class VacanciesSchema(BaseModel):
    data: List[DataVacancySchema]

    class Config:
        orm_mode = True


class RequestVacancyBase(BaseModel):
    phone: str
    name: str
    lastname: str
    surname: str
    email: str
    comment: str
    vacancy_id: int


class RequestVacancyCreate(RequestVacancyBase):
    pass


class RequestVacancy(RequestVacancyBase):
    pass

    class Config:
        orm_mode = True
