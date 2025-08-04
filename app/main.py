from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import os
from contextlib import asynccontextmanager

from .database import get_db, create_tables, init_sample_data
from . import crud

# 生命週期管理
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 啟動時執行
    print("🚀 啟動 FastAPI 應用程式...")
    create_tables()
    init_sample_data()
    print("✅ 資料庫初始化完成！")
    yield
    # 關閉時執行
    print("🛑 關閉 FastAPI 應用程式...")

# 建立 FastAPI 應用程式
app = FastAPI(
    title="杰鑫國際物流",
    description="杰鑫國際物流股份有限公司官方網站",
    version="1.0.0",
    lifespan=lifespan
)

# 模板設定
templates = Jinja2Templates(directory="app/templates")

# 靜態檔案（如果需要）
# app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_index(request: Request, db: Session = Depends(get_db)):
    """首頁"""
    context = {
        "request": request,
        "nav_links": crud.get_nav_links(db),
        "services": crud.get_services(db),
        "news": crud.get_news(db, limit=5),
        "features": crud.get_features(db),
        "external_links": crud.get_external_links(db),
        "partner_logos": crud.get_partner_logos(db),
    }
    return templates.TemplateResponse("index.html", context)

@app.get("/about")
def read_about(request: Request, db: Session = Depends(get_db)):
    """關於我們頁面"""
    context = {
        "request": request,
        "nav_links": crud.get_nav_links(db),
        "external_links": crud.get_external_links(db),
    }
    return templates.TemplateResponse("about.html", context)

@app.get("/news")
def read_news(request: Request, db: Session = Depends(get_db)):
    """新聞頁面"""
    context = {
        "request": request,
        "nav_links": crud.get_nav_links(db),
        "news": crud.get_news(db, limit=20),
        "external_links": crud.get_external_links(db),
    }
    return templates.TemplateResponse("news.html", context)

@app.get("/news/{news_id}")
def read_news_detail(request: Request, news_id: int, db: Session = Depends(get_db)):
    """新聞詳細頁面"""
    news_item = crud.get_news_by_id(db, news_id)
    if not news_item:
        raise HTTPException(status_code=404, detail="新聞不存在")
    
    context = {
        "request": request,
        "nav_links": crud.get_nav_links(db),
        "news_item": news_item,
        "external_links": crud.get_external_links(db),
    }
    return templates.TemplateResponse("news_detail.html", context)

@app.get("/services")
def read_services(request: Request, db: Session = Depends(get_db)):
    """服務頁面"""
    context = {
        "request": request,
        "nav_links": crud.get_nav_links(db),
        "services": crud.get_services(db),
        "external_links": crud.get_external_links(db),
    }
    return templates.TemplateResponse("services.html", context)

@app.get("/facilities")
def read_facilities(request: Request, db: Session = Depends(get_db)):
    """物流設施頁面"""
    context = {
        "request": request,
        "nav_links": crud.get_nav_links(db),
        "external_links": crud.get_external_links(db),
    }
    return templates.TemplateResponse("facilities.html", context)

@app.get("/value-added")
def read_value_added(request: Request, db: Session = Depends(get_db)):
    """加值服務頁面"""
    context = {
        "request": request,
        "nav_links": crud.get_nav_links(db),
        "external_links": crud.get_external_links(db),
    }
    return templates.TemplateResponse("value_added.html", context)

@app.get("/staff")
def read_staff(request: Request, db: Session = Depends(get_db)):
    """員工專區頁面"""
    context = {
        "request": request,
        "nav_links": crud.get_nav_links(db),
        "external_links": crud.get_external_links(db),
    }
    return templates.TemplateResponse("staff.html", context)

@app.get("/contact")
def read_contact(request: Request, db: Session = Depends(get_db)):
    """聯絡我們頁面"""
    context = {
        "request": request,
        "nav_links": crud.get_nav_links(db),
        "external_links": crud.get_external_links(db),
    }
    return templates.TemplateResponse("contact.html", context)

# API 端點（可選，用於前端 AJAX 請求）
@app.get("/api/services")
def api_get_services(db: Session = Depends(get_db)):
    """取得服務列表 API"""
    services = crud.get_services(db)
    return [
        {
            "id": service.id,
            "name": service.name,
            "description": service.description,
            "icon_url": service.icon_url
        }
        for service in services
    ]

@app.get("/api/news")
def api_get_news(limit: int = 10, db: Session = Depends(get_db)):
    """取得新聞列表 API"""
    news = crud.get_news(db, limit=limit)
    return [
        {
            "id": news_item.id,
            "title": news_item.title,
            "content": news_item.content,
            "date": news_item.date.isoformat() if news_item.date else None,
            "link_url": news_item.link_url
        }
        for news_item in news
    ]

@app.get("/health")
def health_check():
    """健康檢查端點"""
    return {"status": "healthy", "message": "杰鑫國際物流系統運行正常"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)