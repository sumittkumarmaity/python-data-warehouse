-- =========================
-- DW HOP-1 : CUSTOMERS
-- =========================
CREATE TABLE IF NOT EXISTS DTL_DW_HOP1_Customers LIKE staging_Customers;

-- =========================
-- DW HOP-1 : PRODUCTS
-- =========================
CREATE TABLE IF NOT EXISTS DTL_DW_HOP1_Products LIKE staging_Products;

-- =========================
-- DW HOP-1 : PRODUCT CATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS DTL_DW_HOP1_Product_Categories LIKE staging_Product_Categories;

-- =========================
-- DW HOP-1 : PRODUCT SUBCATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS DTL_DW_HOP1_Product_Subcategories LIKE staging_Product_Subcategories;

-- =========================
-- DW HOP-1 : TERRITORY
-- =========================
CREATE TABLE IF NOT EXISTS DTL_DW_HOP1_Territory LIKE staging_Territory;

-- =========================
-- DW HOP-1 : SALES YEARS
-- =========================
CREATE TABLE IF NOT EXISTS DTL_DW_HOP1_Sales_Years LIKE staging_Sales_Years;

-- =========================
-- DW HOP-1 : SALES
-- =========================
CREATE TABLE IF NOT EXISTS DTL_DW_HOP1_Sales LIKE staging_Sales;


-- ==================================================
-- -- INDEXES REQUIRED FOR FOREIGN KEYS
-- -- ==================================================
-- -- Customers
-- DROP INDEX IF EXISTS idx_hop1_customerkey
-- ON DTL_DW_HOP1_Customers;

-- CREATE INDEX idx_hop1_customerkey
-- ON DTL_DW_HOP1_Customers (CustomerKey);

-- -- Products
-- DROP INDEX IF EXISTS idx_hop1_productkey
-- ON DTL_DW_HOP1_Products;

-- CREATE INDEX idx_hop1_productkey
-- ON DTL_DW_HOP1_Products (ProductKey);

-- -- Territory
-- DROP INDEX IF EXISTS idx_hop1_territorykey
-- ON DTL_DW_HOP1_Territory;





-- =========================
-- HOP-1 PRIMARY KEYS
-- =========================
-- ALTER TABLE DTL_DW_HOP1_Customers
-- ADD PRIMARY KEY (id);

-- ALTER TABLE DTL_DW_HOP1_Products
-- ADD PRIMARY KEY (id);

-- ALTER TABLE DTL_DW_HOP1_Product_Categories
-- ADD PRIMARY KEY (id);

-- ALTER TABLE DTL_DW_HOP1_Product_Subcategories
-- ADD PRIMARY KEY (id);

-- ALTER TABLE DTL_DW_HOP1_Territory
-- ADD PRIMARY KEY (id);

-- ALTER TABLE DTL_DW_HOP1_Sales
-- ADD PRIMARY KEY (id);

-- =========================
-- HOP-1 FOREIGN KEYS
-- =========================
-- ALTER TABLE DTL_DW_HOP1_Product_Subcategories
-- ADD CONSTRAINT fk_hop1_subcat_category
-- FOREIGN KEY (ProductCategoryKey)
-- REFERENCES DTL_DW_HOP1_Product_Categories (ProductCategoryKey);

-- ALTER TABLE DTL_DW_HOP1_Sales
-- ADD CONSTRAINT fk_hop1_sales_customer
-- FOREIGN KEY (CustomerKey)
-- REFERENCES DTL_DW_HOP1_Customers (CustomerKey);

-- ALTER TABLE DTL_DW_HOP1_Sales
-- ADD CONSTRAINT fk_hop1_sales_product
-- FOREIGN KEY (ProductKey)
-- REFERENCES DTL_DW_HOP1_Products (ProductKey);

-- ALTER TABLE DTL_DW_HOP1_Sales
-- ADD CONSTRAINT fk_hop1_sales_territory
-- FOREIGN KEY (TerritoryKey)
-- REFERENCES DTL_DW_HOP1_Territory (SalesTerritoryKey);





-- =========================
-- HOP-1 INDEXES
-- =========================
-- CREATE INDEX idx_hop1_customerkey ON DTL_DW_HOP1_Customers (CustomerKey);
-- CREATE INDEX idx_hop1_productkey ON DTL_DW_HOP1_Products (ProductKey);
-- CREATE INDEX idx_hop1_sales_customer ON DTL_DW_HOP1_Sales (CustomerKey);
-- CREATE INDEX idx_hop1_sales_product ON DTL_DW_HOP1_Sales (ProductKey);
-- CREATE INDEX idx_hop1_sales_date ON DTL_DW_HOP1_Sales (OrderDate);
