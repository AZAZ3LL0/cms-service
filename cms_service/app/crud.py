from cms_service.app.models import MainPageBanner, Blog, Phones, HeaderPhones, Addresses, Objects, Promotions, MetaTags
from sqlalchemy.orm import Session


def get_blog(db: Session, blog_id: int):
    a = db.query(Blog).filter(Blog.id == blog_id).first()
    a.image = "https://dev.ufaelectro.ru/media/" + a.image if a.image else ''
    return a


def get_meta_tag(db: Session, meta_tag_id: int):
    return db.query(MetaTags).filter(MetaTags.id == meta_tag_id).first()


def get_phone(db: Session, phone_id: int):
    return db.query(Phones).filter(Phones.id == phone_id).first()


def get_header_phone(db: Session, header_phone_id: int):
    return db.query(HeaderPhones).filter(HeaderPhones.id == header_phone_id).first()


def get_address(db: Session, adress_id: int):
    return db.query(Addresses).filter(Addresses.id == adress_id).first()


def get_object(db: Session, object_id: int):
    a = db.query(Objects).filter(Objects.id == object_id).first()
    a.icon = "https://dev.ufaelectro.ru/media/" + a.icon if a.icon else ''
    return a


def get_promotion(db: Session, promotion_id: int):
    a = db.query(Promotions).filter(Promotions.id == promotion_id).first()
    a.image = "https://dev.ufaelectro.ru/media/" + a.image if a.image else ''
    return a


def get_banner(db: Session, main_banner_id: int):
    a = db.query(MainPageBanner).filter(MainPageBanner.id == main_banner_id).first()
    a.image_right = "https://dev.ufaelectro.ru/media/" + a.image_right if a.image_right else ''
    return a


def get_banners(db: Session):
    a = db.query(MainPageBanner).all()
    return a


def get_blogs(db: Session):
    return db.query(Blog).all()


def get_meta_tags(db: Session):
    return db.query(MetaTags).all()


def get_phones(db: Session):
    return db.query(Phones).all()


def get_header_phones(db: Session):
    return db.query(HeaderPhones).all()


def get_addresses(db: Session):
    return db.query(Addresses).all()


def get_objects(db: Session):
    return db.query(Objects).all()


def get_promotions(db: Session):
    return db.query(Promotions).all()
