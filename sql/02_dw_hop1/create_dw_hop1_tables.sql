-- =========================
-- HOP1 : CUSTOMERS
-- =========================
CREATE TABLE IF NOT EXISTS TBL_DTL_DW_HOP1_Customers (
    CustomerKey INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    BirthDate DATE,
    Age INT,
    MaritalStatus VARCHAR(20),
    EmailAddress VARCHAR(255),
    AnnualIncome DECIMAL(12,2),
    TotalChildren INT,
    EducationLevel VARCHAR(100),
    Occupation VARCHAR(100),
    HomeOwner VARCHAR(10)
);

-- =========================
-- HOP1 : PRODUCTS
-- =========================
CREATE TABLE IF NOT EXISTS TBL_DTL_DW_HOP1_Products (
    ProductKey INT PRIMARY KEY,
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
-- HOP1 : PRODUCT CATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_DTL_DW_HOP1_Product_Categories (
    ProductCategoryKey INT ,
    CategoryName VARCHAR(100)
);

-- =========================
-- HOP1 : PRODUCT SUBCATEGORIES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_DTL_DW_HOP1_Product_Subcategories (
    ProductSubcategoryKey INT PRIMARY KEY,
    SubcategoryName VARCHAR(100),
    ProductCategoryKey INT
);

-- =========================
-- HOP1 : TERRITORY
-- =========================
CREATE TABLE IF NOT EXISTS TBL_DTL_DW_HOP1_Territory (
    SalesTerritoryKey INT PRIMARY KEY,
    Region VARCHAR(50),
    Country VARCHAR(50),
    Continent VARCHAR(50)
);

-- =========================
-- HOP1 : SALES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_DTL_DW_HOP1_Sales (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerKey INT,
    OrderDate DATE,
    StockDate DATE,
    OrderNumber VARCHAR(50),
    ProductKey INT,
    TerritoryKey INT,
    OrderLineItem INT,
    OrderQuantity INT,
    SalesYear INT,
    Sales DECIMAL(12,2),
    Profit DECIMAL(12,2)
);
