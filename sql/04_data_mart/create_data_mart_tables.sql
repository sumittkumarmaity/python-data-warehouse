-- =========================
-- DATA MART : CUSTOMERS
-- =========================
CREATE TABLE IF NOT EXISTS FL_DM_Customers LIKE DTL_DW_HOP2_Customers;

-- =========================
-- DATA MART : PRODUCTS
-- =========================
CREATE TABLE IF NOT EXISTS FL_DM_Products LIKE DTL_DW_HOP1_Products;

-- =========================
-- DATA MART : PRODUCT CATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS FL_DM_Product_Categories LIKE DTL_DW_HOP1_Product_Categories;

-- =========================
-- DATA MART : PRODUCT SUBCATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS FL_DM_Product_Subcategories LIKE DTL_DW_HOP1_Product_Subcategories;

-- =========================
-- DATA MART : TERRITORY
-- =========================
CREATE TABLE IF NOT EXISTS FL_DM_Territory LIKE DTL_DW_HOP1_Territory;

-- =========================
-- DATA MART : SALES YEARS
-- =========================
CREATE TABLE IF NOT EXISTS FL_DM_Sales_Years LIKE DTL_DW_HOP1_Sales_Years;

-- =========================
-- DATA MART : SALES
-- =========================
CREATE TABLE IF NOT EXISTS FL_DM_Sales LIKE DTL_DW_HOP2_Sales;


-- =========================
-- DATA MART PRIMARY KEYS
-- =========================
-- ALTER TABLE FL_DM_Customers
-- ADD PRIMARY KEY (id);

-- ALTER TABLE FL_DM_Products
-- ADD PRIMARY KEY (id);

-- ALTER TABLE FL_DM_Product_Categories
-- ADD PRIMARY KEY (id);

-- ALTER TABLE FL_DM_Product_Subcategories
-- ADD PRIMARY KEY (id);

-- ALTER TABLE FL_DM_Territory
-- ADD PRIMARY KEY (id);

-- ALTER TABLE FL_DM_Sales
-- ADD PRIMARY KEY (id);

-- =========================
-- DATA MART FOREIGN KEYS
-- =========================
-- ALTER TABLE FL_DM_Sales
-- ADD CONSTRAINT fk_dm_sales_customer
-- FOREIGN KEY (CustomerKey)
-- REFERENCES FL_DM_Customers (CustomerKey);

-- ALTER TABLE FL_DM_Sales
-- ADD CONSTRAINT fk_dm_sales_product
-- FOREIGN KEY (ProductKey)
-- REFERENCES FL_DM_Products (ProductKey);

-- ALTER TABLE FL_DM_Product_Subcategories
-- ADD CONSTRAINT fk_dm_subcat_category
-- FOREIGN KEY (ProductCategoryKey)
-- REFERENCES FL_DM_Product_Categories (ProductCategoryKey);

-- =========================
-- DATA MART INDEXES (REPORTING)
-- =========================
-- CREATE INDEX idx_dm_customerkey ON FL_DM_Customers (CustomerKey);
-- CREATE INDEX idx_dm_productkey ON FL_DM_Products (ProductKey);
-- CREATE INDEX idx_dm_sales_customer ON FL_DM_Sales (CustomerKey);
-- CREATE INDEX idx_dm_sales_product ON FL_DM_Sales (ProductKey);
-- CREATE INDEX idx_dm_sales_date ON FL_DM_Sales (OrderDate);
