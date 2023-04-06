from typing import Optional
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
