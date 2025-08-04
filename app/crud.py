from sqlalchemy.orm import Session
from .models import NavLink, Service, ExternalLink, PartnerLogo, News, Feature

def get_nav_links(db: Session):
    """取得導航選單"""
    return db.query(NavLink).filter(NavLink.is_active == True).order_by(NavLink.sort_order).all()

def get_services(db: Session):
    """取得服務項目"""
    return db.query(Service).filter(Service.is_active == True).order_by(Service.sort_order).all()

def get_external_links(db: Session, category: str = None):
    """取得外部連結"""
    query = db.query(ExternalLink).filter(ExternalLink.is_active == True)
    if category:
        query = query.filter(ExternalLink.category == category)
    return query.all()

def get_partner_logos(db: Session):
    """取得合作夥伴 Logo"""
    return db.query(PartnerLogo).filter(PartnerLogo.is_active == True).order_by(PartnerLogo.sort_order).all()

def get_news(db: Session, limit: int = 10):
    """取得新聞列表"""
    return db.query(News).filter(News.is_active == True).order_by(News.date.desc()).limit(limit).all()

def get_news_by_id(db: Session, news_id: int):
    """根據 ID 取得特定新聞"""
    return db.query(News).filter(News.id == news_id, News.is_active == True).first()

def get_features(db: Session):
    """取得網站特色"""
    return db.query(Feature).filter(Feature.is_active == True).order_by(Feature.sort_order).all()

# 以下是一些額外的 CRUD 操作，用於後台管理

def create_nav_link(db: Session, title: str, url: str, sort_order: int = 0):
    """建立新的導航連結"""
    db_nav = NavLink(title=title, url=url, sort_order=sort_order)
    db.add(db_nav)
    db.commit()
    db.refresh(db_nav)
    return db_nav

def create_service(db: Session, name: str, description: str = None, icon_url: str = None, sort_order: int = 0):
    """建立新的服務項目"""
    db_service = Service(name=name, description=description, icon_url=icon_url, sort_order=sort_order)
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def create_news(db: Session, title: str, content: str = None, link_url: str = None):
    """建立新聞"""
    db_news = News(title=title, content=content, link_url=link_url)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

def update_news(db: Session, news_id: int, title: str = None, content: str = None, link_url: str = None):
    """更新新聞"""
    db_news = db.query(News).filter(News.id == news_id).first()
    if db_news:
        if title:
            db_news.title = title
        if content:
            db_news.content = content
        if link_url:
            db_news.link_url = link_url
        db.commit()
        db.refresh(db_news)
    return db_news

def delete_news(db: Session, news_id: int):
    """刪除新聞（軟刪除）"""
    db_news = db.query(News).filter(News.id == news_id).first()
    if db_news:
        db_news.is_active = False
        db.commit()
    return db_news