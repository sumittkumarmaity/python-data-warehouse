-- =========================
-- STAGING : CUSTOMERS
-- =========================
CREATE TABLE IF NOT EXISTS TBL_Staging_Customers (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerKey INT,
    Prefix VARCHAR(10),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE,
    MaritalStatus VARCHAR(10),
    Gender VARCHAR(20),
    EmailAddress VARCHAR(100),
    AnnualIncome DECIMAL(12,2),
    TotalChildren INT,
    EducationLevel VARCHAR(50),
    Occupation VARCHAR(50),
    HomeOwner VARCHAR(10)
);

-- =========================
-- STAGING : PRODUCTS
-- =========================
CREATE TABLE IF NOT EXISTS TBL_Staging_Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ProductKey INT,
    ProductSubcategoryKey INT,
    ProductSKU VARCHAR(50),
    ProductName VARCHAR(100),
    ModelName VARCHAR(100),
    ProductDescription TEXT,
    ProductColor VARCHAR(30),
    ProductSize VARCHAR(20),
    ProductStyle VARCHAR(30),
    ProductCost DECIMAL(12,2),
    ProductPrice DECIMAL(12,2)
);

-- =========================
-- STAGING : PRODUCT CATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_Staging_Product_Categories (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ProductCategoryKey INT,
    CategoryName VARCHAR(100)
);

-- =========================
-- STAGING : PRODUCT SUBCATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_Staging_Product_Subcategories (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ProductSubcategoryKey INT,
    SubcategoryName VARCHAR(100),
    ProductCategoryKey INT
);

-- =========================
-- STAGING : TERRITORY
-- =========================
CREATE TABLE IF NOT EXISTS TBL_Staging_Territory (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    SalesTerritoryKey INT,
    Region VARCHAR(50),
    Country VARCHAR(50),
    Continent VARCHAR(50)
);

-- =========================
-- STAGING : SALES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_Staging_Sales (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    OrderDate DATE,
    StockDate DATE,
    OrderNumber VARCHAR(50),
    ProductKey INT,
    CustomerKey INT,
    TerritoryKey INT,
    OrderLineItem INT,
    OrderQuantity INT,
    SalesYear INT
);