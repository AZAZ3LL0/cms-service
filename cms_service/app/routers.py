from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from cms_service.app import crud
from .database import get_db
from cms_service.app.schemas import MainPageBannerDTO, BlogDTO, HeaderPhonesDTO, PhonesDTO, AddressesDTO, ObjectsDTO, \
    PromotionsDTO, MetaTagsDTO, Stock, DescPointDTO, Coordinate, Requisites, DataReq, DataPrivacyPolicy, PrivacyPolicy, \
    DataDelInfo, DelInfo

router = APIRouter()

get_db()
path = "/api"


@router.get(path + "/banner", tags=["Get all"], response_model=list[MainPageBannerDTO])
def get_all_banners(db: Session = Depends(get_db)):
    banners = crud.get_banners(db)

    for banner in banners:
        banner.media_root()

    return crud.get_banners(db)


@router.get(path + "/blog", tags=["Get all"], response_model=list[BlogDTO])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db)

    for blog in blogs:
        blog.media_root()

    return crud.get_blogs(db)


@router.get(path + "/footer_phones", tags=["Get all"], response_model=list[PhonesDTO])
def get_all_phones(db: Session = Depends(get_db)):
    return crud.get_phones(db)


@router.get(path + "/header_phones", tags=["Get all"], response_model=list[HeaderPhonesDTO])
def get_all_header_phones(db: Session = Depends(get_db)):
    return crud.get_header_phones(db)


@router.get(path + "/footer_addresses", tags=["Get all"], response_model=list[AddressesDTO])
def get_all_addresses(db: Session = Depends(get_db)):
    return crud.get_addresses(db)


@router.get(path + "/footer_objects", tags=["Get all"], response_model=list[ObjectsDTO])
def get_all_objects(db: Session = Depends(get_db)):
    objs = crud.get_objects(db)

    for obj in objs:
        obj.media_root()

    return crud.get_objects(db)


@router.get(path + "/promotions", tags=["Get all"], response_model=list[PromotionsDTO])
def get_all_promotions(db: Session = Depends(get_db)):
    promts = crud.get_promotions(db)

    for promt in promts:
        promt.media_root()

    return crud.get_promotions(db)


@router.get(path + "/meta_tags", tags=["Get all"], response_model=list[MetaTagsDTO])
def get_all_meta_tags(db: Session = Depends(get_db)):
    return crud.get_meta_tags(db)


@router.get(path + "/requisites/", tags=["Get all"], response_model=list[Requisites])
def get_all_requisites(db: Session = Depends(get_db)):
    requisites = crud.get_requisites(db)
    requisites_schema_list = [Requisites(data=DataReq(body=req.text)) for req in requisites]
    return requisites_schema_list


@router.get(path + "/privacy_policy/", tags=["Get all"], response_model=list[PrivacyPolicy])
def get_all_privacy_policy(db: Session = Depends(get_db)):
    privacy_policy = crud.get_privacy_policy(db)
    privacy_policy_schema_list = [PrivacyPolicy(data=DataPrivacyPolicy(body=pr_pol.text)) for pr_pol in privacy_policy]
    return privacy_policy_schema_list


@router.get(path + "/cdek_delivery_info/", tags=["Get all"], response_model=list[DelInfo])
def get_all_cdek_delivery_info(db: Session = Depends(get_db)):
    del_infos = crud.get_del_info(db)
    del_info_schema_list = [DelInfo(data=DataDelInfo(description=del_info.description)) for del_info in del_infos]
    return del_info_schema_list


@router.get(path + "/pick_up_point/", tags=["Get all"], response_model=dict)
def get_all_pick_up_points(db: Session = Depends(get_db)):
    pick_up_points = crud.get_pick_up_point(db)
    for point in pick_up_points:
        point_titles = crud.get_stock_title_by_id(db, point.title_id)
        c_x = crud.get_coordinate_x(db, point.coordinate_x)
        c_y = crud.get_coordinate_y(db, point.coordinate_y)

        if len(point_titles) != 0:
            desc = list(
                map(lambda x: DescPointDTO(description=x.description), crud.get_stock_desc_by_point_id(db, point.id)))
            stock = Stock(title=point_titles[0].title, description=desc)
            coordinates = Coordinate(coordinate_x=c_x[0].coordinate_x, coordinate_y=c_y[0].coordinate_y)
            point.stock = stock
            point.coordinates = coordinates

    data_dict = [vars(point) for point in pick_up_points]

    for point in data_dict:
        point.pop("coordinate_x", None)
        point.pop("coordinate_y", None)
        point.pop("time_id", None)
        point.pop("title_id", None)
        for point in data_dict:
            for key in point:
                if isinstance(point[key], (int, float)):
                    point[key] = str(point[key])

    return {"data": pick_up_points}


@router.get(path + "/banner/", tags=["Get by id"], response_model=MainPageBannerDTO)
def get_id_banner(main_banner_id: int, db: Session = Depends(get_db)):
    db_banner = crud.get_banner(db, main_banner_id=main_banner_id)
    return db_banner


@router.get(path + "/meta_tags/", tags=["Get by id"], response_model=MetaTagsDTO)
def get_id_promotions(meta_tag_id: int, db: Session = Depends(get_db)):
    db_id_meta_tag = crud.get_meta_tag(db, meta_tag_id=meta_tag_id)
    return db_id_meta_tag


@router.get(path + "/blog/", tags=["Get by id"], response_model=BlogDTO)
def get_id_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id=blog_id)
    return db_blog


@router.get(path + "/footer_phones/", tags=["Get by id"], response_model=PhonesDTO)
def get_id_phones(phone_id: int, db: Session = Depends(get_db)):
    db_phone = crud.get_phone(db, phone_id=phone_id)
    return db_phone


@router.get(path + "/header_phones/", tags=["Get by id"], response_model=HeaderPhonesDTO)
def get_id_header_phones(header_phone_id: int, db: Session = Depends(get_db)):
    db_header_phone = crud.get_header_phone(db, header_phone_id=header_phone_id)
    return db_header_phone


@router.get(path + "/footer_addresses/", tags=["Get by id"], response_model=AddressesDTO)
def get_id_addresses(adress_id: int, db: Session = Depends(get_db)):
    db_adress = crud.get_address(db, adress_id=adress_id)
    return db_adress


@router.get(path + "/footer_objects/", tags=["Get by id"], response_model=ObjectsDTO)
def get_id_objects(object_id: int, db: Session = Depends(get_db)):
    db_object = crud.get_object(db, object_id=object_id)
    return db_object


@router.get(path + "/promotions/", tags=["Get by id"], response_model=PromotionsDTO)
def get_id_promotions(promotion_id: int, db: Session = Depends(get_db)):
    db_promotion = crud.get_promotion(db, promotion_id=promotion_id)
    return db_promotion
