-- 20_create_products.sql

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    unit_price REAL,
    stock_quantity INTEGER,
    supplier TEXT
);