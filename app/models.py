from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class NavLink(Base):
    """導航選單模型"""
    __tablename__ = "nav_links"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    url = Column(String(200), nullable=False)
    sort_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

class Service(Base):
    """服務項目模型"""
    __tablename__ = "services"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    icon_url = Column(String(300))
    sort_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

class ExternalLink(Base):
    """外部連結模型"""
    __tablename__ = "external_links"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    url = Column(String(500), nullable=False)
    category = Column(String(100))
    is_active = Column(Boolean, default=True)

class PartnerLogo(Base):
    """合作夥伴 Logo 模型"""
    __tablename__ = "partner_logos"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    logo_url = Column(String(500), nullable=False)
    link_url = Column(String(500))
    sort_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

class News(Base):
    """新聞訊息模型"""
    __tablename__ = "news"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    content = Column(Text)
    date = Column(DateTime, default=func.now())
    link_url = Column(String(500))
    is_active = Column(Boolean, default=True)

class Feature(Base):
    """網站特色模型"""
    __tablename__ = "features"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(300), nullable=False)
    icon_class = Column(String(100))  # 用於 CSS icon class
    sort_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)