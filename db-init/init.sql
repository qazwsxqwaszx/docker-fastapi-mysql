-- 設定字符集
SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

-- 使用資料庫
USE jshine_logistics;

-- 確保表格使用正確的字符集
ALTER DATABASE jshine_logistics CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 建立資料表（這些會由 SQLAlchemy 自動建立，這裡只是備用）

-- 導航連結表
CREATE TABLE IF NOT EXISTS nav_links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    url VARCHAR(200) NOT NULL,
    sort_order INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 服務項目表
CREATE TABLE IF NOT EXISTS services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    icon_url VARCHAR(300),
    sort_order INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 外部連結表
CREATE TABLE IF NOT EXISTS external_links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    url VARCHAR(500) NOT NULL,
    category VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 合作夥伴 Logo 表
CREATE TABLE IF NOT EXISTS partner_logos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    logo_url VARCHAR(500) NOT NULL,
    link_url VARCHAR(500),
    sort_order INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 新聞表
CREATE TABLE IF NOT EXISTS news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(300) NOT NULL,
    content TEXT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    link_url VARCHAR(500),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 特色功能表
CREATE TABLE IF NOT EXISTS features (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(300) NOT NULL,
    icon_class VARCHAR(100),
    sort_order INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 插入範例資料
INSERT IGNORE INTO nav_links (id, title, url, sort_order) VALUES
(1, '首頁', '/', 1),
(2, '關於杰鑫', '/about', 2),
(3, '最新訊息', '/news', 3),
(4, '杰鑫服務', '/services', 4),
(5, '物流設施', '/facilities', 5),
(6, '加值服務', '/value-added', 6),
(7, '員工專區', '/staff', 7),
(8, '業務聯絡', '/contact', 8);

INSERT IGNORE INTO services (id, name, description, sort_order) VALUES
(1, '運輸承攬業務', '提供全方位的運輸承攬服務，包含海運、空運、陸運等多種運輸方式', 1),
(2, '倉儲整合服務', '現代化倉儲管理系統，提供安全、效率的貨物存放和管理服務', 2),
(3, '報關相關服務', '具備海關執照，提供專業的進出口報關代理服務', 3),
(4, '國際物流服務', '跨國物流解決方案，服務網絡遍及全球主要港口和城市', 4),
(5, '其他物流服務', '客製化物流服務，根據客戶需求提供專業的物流解決方案', 5);

INSERT IGNORE INTO features (id, description, icon_class, sort_order) VALUES
(1, '具海關執照', 'fas fa-certificate', 1),
(2, 'ISO-9001 品質認證', 'fas fa-award', 2),
(3, '強大運輸車隊', 'fas fa-truck', 3),
(4, '安全寬敞倉儲空間', 'fas fa-warehouse', 4),
(5, '資訊系統完整', 'fas fa-desktop', 5),
(6, '彈性合理收費', 'fas fa-dollar-sign', 6);

INSERT IGNORE INTO news (id, title, content, date) VALUES
(1, '杰鑫國際物流新大樓落成', '本公司投資興建的新總部大樓已正式落成啟用，提供更優質的服務環境和辦公空間。新大樓配備現代化設施，將為客戶提供更專業、更便利的服務。', '2019-11-06 00:00:00'),
(2, 'ISO-9001 品質管理系統認證通過', '本公司順利通過 ISO-9001 品質管理系統認證，這標誌著我們在服務品質管理方面達到國際標準，將持續為客戶提供高品質的物流服務。', '2019-08-15 00:00:00'),
(3, '擴大國際物流服務範圍', '為了更好地服務客戶，本公司新增多項國際物流服務項目，包括新的航線和運輸路線，進一步完善我們的全球服務網絡。', '2019-05-20 00:00:00'),
(4, '引進先進倉儲管理系統', '本公司導入最新的倉儲管理系統（WMS），大幅提升倉儲作業效率和準確度，為客戶提供更可靠的倉儲服務。', '2018-12-10 00:00:00'),
(5, '榮獲優良物流業者獎項', '本公司榮獲交通部頒發的優良物流業者獎項，這是對我們多年來專業服務的肯定，我們將持續努力提供更好的服務。', '2018-03-15 00:00:00');

INSERT IGNORE INTO external_links (id, name, url, category) VALUES
(1, '海關通關資料庫', 'https://web.customs.gov.tw', '政府機關'),
(2, '保稅稽核系統', 'https://fbonded.customs.gov.tw', '政府機關'),
(3, '交通部航港局', 'https://www.motcmpb.gov.tw', '政府機關'),
(4, '台灣港務公司', 'https://www.twport.com.tw', '相關機構');

-- 建立索引以提升查詢效能
CREATE INDEX idx_nav_links_active_order ON nav_links (is_active, sort_order);
CREATE INDEX idx_services_active_order ON services (is_active, sort_order);
CREATE INDEX idx_news_active_date ON news (is_active, date DESC);
CREATE INDEX idx_features_active_order ON features (is_active, sort_order);
CREATE INDEX idx_external_links_active_category ON external_links (is_active, category);
CREATE INDEX idx_partner_logos_active_order ON partner_logos (is_active, sort_order);