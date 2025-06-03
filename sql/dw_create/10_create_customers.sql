-- 10_create_customers.sql

CREATE TABLE IF NOT EXISTS customers (
    Customer_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Region TEXT,
    Join_Date TEXT,
    Preferred_Contact_Method TEXT,
    Loyalty_Points INTEGER
);