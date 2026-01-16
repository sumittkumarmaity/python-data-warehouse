-- =========================
-- DW HOP-2 : CUSTOMERS
-- =========================
CREATE TABLE IF NOT EXISTS TBL_DTL_DW_HOP2_Customers (
    CustomerKey INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    BirthDate DATE,
    Age INT,
    MaritalStatus VARCHAR(20),
    Gender VARCHAR(20),
    EmailAddress VARCHAR(255),
    AnnualIncome DECIMAL(12,2),
    TotalChildren INT,
    EducationLevel VARCHAR(100),
    Occupation VARCHAR(100),
    HomeOwner VARCHAR(10),
    CustomerType VARCHAR(20)
);

-- =========================
-- DW HOP-2 : SALES
-- =========================
CREATE TABLE IF NOT EXISTS TBL_DTL_DW_HOP2_Sales (
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
