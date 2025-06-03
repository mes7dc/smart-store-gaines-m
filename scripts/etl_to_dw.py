import pandas as pd
import sqlite3
import pathlib
import sys

# For local imports, temporarily add project root to sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils.logger import logger  


# Constants
DW_DIR = pathlib.Path("data").joinpath("dw")
DW_DIR.mkdir(parents=True, exist_ok=True)  # Needed to add this line to ensure the data warehouse directory exists
DB_PATH = DW_DIR.joinpath("smart_sales.db")
PREPARED_DATA_DIR = pathlib.Path("data").joinpath("prepared")
PREPARED_DATA_DIR.mkdir(parents=True, exist_ok=True)

def create_schema(cursor: sqlite3.Cursor) -> None:
    """Create tables in the data warehouse if they don't exist."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            region TEXT,
            join_date TEXT,
            loyalty_points INTEGER,
            preferred_contact_method TEXT      
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            unit_price REAL,
            stock_quantity INTEGER,
            supplier TEXT       
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sale (
            sale_id REAL PRIMARY KEY,
            customer_id INTEGER,
            product_id INTEGER,
            store_id REAL,
            campaign_id REAL,
            sale_amount REAL,
            sale_date TEXT,
            discount_percent REAL,
            payment_type TEXT,
            FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
            FOREIGN KEY (product_id) REFERENCES product (product_id)
        )
    """)

def delete_existing_records(cursor: sqlite3.Cursor) -> None:
    """Delete all existing records from the customer, product, and sale table."""
    cursor.execute("DELETE FROM customer")
    cursor.execute("DELETE FROM product")
    cursor.execute("DELETE FROM sale")

def insert_customers(customers_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    """Insert customer data into the customer table."""
    customers_df.to_sql("customer", cursor.connection, if_exists="append", index=False)

def insert_products(products_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    """Insert product data into the product table."""
    products_df.to_sql("product", cursor.connection, if_exists="append", index=False)

def insert_sales(sales_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    """Insert sales data into the sale table."""
    sales_df.to_sql("sale", cursor.connection, if_exists="append", index=False)

def load_data_to_db() -> None:
    try:
        # Connect to SQLite – will create the file if it doesn't exist
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        logger.info(f"Connected to SQLite database at {DB_PATH}")


        # Create schema and clear existing records
        create_schema(cursor)
        delete_existing_records(cursor)
        logger.info("Schema created and existing records deleted.")

        # Load prepared data using pandas
        customers_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("customers_prepared.csv"))
        customers_df = customers_df.rename(columns={
            "Customer_ID": "customer_id",
            "Name": "name",
            "Region": "region",
            "Join_Date": "join_date",
            "Loyalty_Points": "loyalty_points",
            "Preferred_Contact_Method": "preferred_contact_method"
        })
        
        products_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("products_prepared.csv"))
        products_df = products_df.rename(columns={
            "product_id": "product_id",
            "product_name": "product_name",
            "category": "category",
            "unit_price": "unit_price",
            "stock_quantity": "stock_quantity",
            "supplier": "supplier"
        })
        
        sales_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("sales_prepared.csv"))
        sales_df = sales_df.rename(columns={
            "Transaction_ID": "sale_id",
            "Sale_Date": "sale_date",
            "Customer_ID": "customer_id",
            "Product_ID": "product_id",
            "Store_ID": "store_id",
            "Campaign_ID": "campaign_id",
            "Sales_Amount": "sale_amount",
            "Discount_Percent": "discount_percent",
            "Payment_Type": "payment_type"
        })

        print("sales_df columns:", sales_df.dtypes)

        #Delete Exisiting Records first
        #delete_existing_records(cursor)
        #logger.info("Existing records deleted from all tables.")

        # Insert data into the database
        insert_customers(customers_df, cursor)
        logger.info(f"Inserted {len(customers_df)} records into customer table.")
        
        insert_products(products_df, cursor)
        logger.info(f"Inserted {len(products_df)} records into product table.")
        
        insert_sales(sales_df, cursor)
        logger.info(f"Inserted {len(sales_df)} records into sale table.")

        conn.commit()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    load_data_to_db()