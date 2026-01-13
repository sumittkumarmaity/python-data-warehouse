-- =========================
-- DATA MART : CUSTOMERS
-- =========================
CREATE TABLE IF NOT EXISTS TBL_FL_DM_Customers LIKE TBL_DTL_DW_HOP2_Customers;

-- =========================
-- DATA MART : PRODUCTS
-- =========================
CREATE TABLE IF NOT EXISTS TBL_FL_DM_Products LIKE TBL_DTL_DW_HOP1_Products;

-- =========================
-- DATA MART : PRODUCT CATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_FL_DM_Product_Categories LIKE TBL_DTL_DW_HOP1_Product_Categories;

-- =========================
-- DATA MART : PRODUCT SUBCATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_FL_DM_Product_Subcategories LIKE TBL_DTL_DW_HOP1_Product_Subcategories;

-- =========================
-- DATA MART : TERRITORY
-- =========================
CREATE TABLE IF NOT EXISTS TBL_FL_DM_Territory LIKE TBL_DTL_DW_HOP1_Territory;

-- =========================
-- DATA MART : SALES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_FL_DM_Sales LIKE TBL_DTL_DW_HOP2_Sales;


