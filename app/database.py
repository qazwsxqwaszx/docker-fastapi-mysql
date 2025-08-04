import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from .models import Base

# 載入環境變數
load_dotenv()

# 資料庫連接字串
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/jshine_logistics")

# 建立引擎
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # 檢查連接是否活躍
    pool_recycle=300,    # 每 5 分鐘回收連接池
    echo=False           # 生產環境設為 False
)

# 建立 SessionLocal 類別
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """取得資料庫 session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """建立所有資料表"""
    Base.metadata.create_all(bind=engine)

def init_sample_data():
    """初始化範例資料"""
    db = SessionLocal()
    try:
        from .models import NavLink, Service, Feature, News, ExternalLink, PartnerLogo
        
        # 檢查是否已有資料
        if db.query(NavLink).count() > 0:
            return
            
        # 插入導航選單
        nav_items = [
            NavLink(title="首頁", url="/", sort_order=1),
            NavLink(title="關於杰鑫", url="/about", sort_order=2),
            NavLink(title="最新訊息", url="/news", sort_order=3),
            NavLink(title="杰鑫服務", url="/services", sort_order=4),
            NavLink(title="物流設施", url="/facilities", sort_order=5),
            NavLink(title="加值服務", url="/value-added", sort_order=6),
            NavLink(title="員工專區", url="/staff", sort_order=7),
            NavLink(title="業務聯絡", url="/contact", sort_order=8),
        ]
        
        # 插入服務項目
        services = [
            Service(name="運輸承攬業務", description="提供全方位的運輸承攬服務", sort_order=1),
            Service(name="倉儲整合服務", description="現代化倉儲管理系統", sort_order=2),
            Service(name="報關相關服務", description="專業報關代理服務", sort_order=3),
            Service(name="國際物流服務", description="跨國物流解決方案", sort_order=4),
            Service(name="其他物流服務", description="客製化物流服務", sort_order=5),
        ]
        
        # 插入網站特色
        features = [
            Feature(description="具海關執照", icon_class="fas fa-certificate", sort_order=1),
            Feature(description="ISO-9001 品質認證", icon_class="fas fa-award", sort_order=2),
            Feature(description="強大運輸車隊", icon_class="fas fa-truck", sort_order=3),
            Feature(description="安全寬敞倉儲空間", icon_class="fas fa-warehouse", sort_order=4),
            Feature(description="資訊系統完整", icon_class="fas fa-computer", sort_order=5),
            Feature(description="彈性合理收費", icon_class="fas fa-dollar-sign", sort_order=6),
        ]
        
        # 插入新聞
        news_items = [
            News(title="杰鑫國際物流新大樓落成", content="本公司新建大樓正式啟用，提供更優質的服務環境。", date="2019-11-06"),
            News(title="ISO-9001 認證通過", content="本公司順利通過 ISO-9001 品質認證。", date="2019-08-15"),
            News(title="新增國際物流服務", content="擴大服務範圍，新增多項國際物流服務項目。", date="2019-05-20"),
        ]
        
        # 插入外部連結
        external_links = [
            ExternalLink(name="海關通關資料庫", url="https://web.customs.gov.tw", category="政府機關"),
            ExternalLink(name="保稅稽核系統", url="https://fbonded.customs.gov.tw", category="政府機關"),
        ]
        
        # 批量插入資料
        db.add_all(nav_items)
        db.add_all(services)
        db.add_all(features)
        db.add_all(news_items)
        db.add_all(external_links)
        
        db.commit()
        print("範例資料已成功插入！")
        
    except Exception as e:
        print(f"插入範例資料時發生錯誤: {e}")
        db.rollback()
    finally:
        db.close()