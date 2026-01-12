-- =========================
-- DW HOP-2 : CUSTOMERS
-- =========================
CREATE TABLE IF NOT EXISTS DTL_DW_HOP2_Customers (
    id INT,
    CustomerKey INT,
    Prefix VARCHAR(10),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE,
    MaritalStatus VARCHAR(10),
    Gender VARCHAR(10),
    EmailAddress VARCHAR(100),
    AnnualIncome DECIMAL(12,2),
    TotalChildren INT,
    EducationLevel VARCHAR(50),
    Occupation VARCHAR(50),
    HomeOwner VARCHAR(10)
);

-- =========================
-- DW HOP-2 : SALES
-- =========================
CREATE TABLE IF NOT EXISTS DTL_DW_HOP2_Sales (
    id INT,
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


-- =========================
-- HOP-2 PRIMARY KEYS
-- =========================
ALTER TABLE DTL_DW_HOP2_Customers
ADD PRIMARY KEY (id);

ALTER TABLE DTL_DW_HOP2_Sales
ADD PRIMARY KEY (id);

-- =========================
-- HOP-2 FOREIGN KEYS
-- =========================
-- ALTER TABLE DTL_DW_HOP2_Sales
-- ADD CONSTRAINT fk_hop2_sales_customer
-- FOREIGN KEY (CustomerKey)
-- REFERENCES DTL_DW_HOP2_Customers (CustomerKey);

-- =========================
-- HOP-2 INDEXES
-- =========================
-- CREATE INDEX idx_hop2_customerkey ON DTL_DW_HOP2_Customers (CustomerKey);
-- CREATE INDEX idx_hop2_sales_customer ON DTL_DW_HOP2_Sales (CustomerKey);
-- CREATE INDEX idx_hop2_sales_product ON DTL_DW_HOP2_Sales (ProductKey);
-- CREATE INDEX idx_hop2_sales_date ON DTL_DW_HOP2_Sales (OrderDate);
