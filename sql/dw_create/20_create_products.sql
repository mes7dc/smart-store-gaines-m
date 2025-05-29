-- 20_create_products.sql

CREATE TABLE IF NOT EXISTS products (
    productid INTEGER PRIMARY KEY,
    productname TEXT NOT NULL,
    category TEXT,
    unitprice REAL,
    stockquantity INTEGER,
    supplier TEXT
);