
# RUN :: Use Python’s built-in pip
# python -m pip install -r requirements.txt

- python -c "import mysql.connector; print('MySQL OK')" ---- RUN If Required
- python -m pip uninstall mysql-connector-python -y ---- RUN If Required
- python -m pip install mysql-connector-python==8.0.33 ---- RUN If Required

# Project: Python Project - Data Warehouse Development(Language: Python, Database: MySQL)
Context: Implement a Data Warehouse, from source data (Excel) to Staging then Staging to Data Warehouse and then final Data Marts for end users to show analytical reports. 
Architecture: Source System/Source-Data(Excel, CSV) -> Staging(MySQL Database) -> Data Warehouse(HOP-1) -> Data Warehouse(HOP-2) -> Data Marts -> [ Report: End User ] 


----------------------------------------------------------------------------------------------------

# Steps-1 :: Source System:

Source-Data(CSV Files) : Read/Fetch all the source data from csv file with in the project folder and files and columns names mention bellow.
----CSV Files----
Customers - [Columns - CustomerKey,Prefix,FirstName,LastName,BirthDate,MaritalStatus,Gender,EmailAddress,AnnualIncome,TotalChildren,EducationLevel,Occupation,HomeOwner],
Products - [ Columns - ProductKey,ProductSubcategoryKey,ProductSKU,ProductName,ModelName,ProductDescription,ProductColor,ProductSize,ProductStyle,ProductCost,ProductPrice],
Product_Categories - [ Columns - ProductCategoryKey,CategoryName],
Product_Subcategories - [ Columns - ProductSubcategoryKey,SubcategoryName,ProductCategoryKey],
Territory - [ Columns - SalesTerritoryKey,Region,Country,Continent],
Sales_Data_2020 - [ Columns - OrderDate,StockDate,OrderNumber,ProductKey,CustomerKey,TerritoryKey,OrderLineItem,OrderQuantity],
Sales_Data_2021 - [ Columns - OrderDate,StockDate,OrderNumber,ProductKey,CustomerKey,TerritoryKey,OrderLineItem,OrderQuantity],
Sales_Data_2022 - [ Columns - OrderDate,StockDate,OrderNumber,ProductKey,CustomerKey,TerritoryKey,OrderLineItem,OrderQuantity]
----------------------------------------------------------------------------------------------------

# Steps-2 :: Data Staging Layer:

Insert Source-Data(CSV Files) to MySQL Database.
1. Create My SQL Script to create all the tables with autoincrement primary kay (if table is already exist then no need to create table only update data) 
2. Every table name will contain a prefix with Example: staging_Customers
Note: Sales_Data_2020, Sales_Data_2021, Sales_Data_2022 will be merge and inset in a single table Sales. Source Data(csv) dose not have Sales_Years, so create a static Script
and insert static data 2020, 2021, 2022.
----Staging Tables----
Customers - [Columns - CustomerKey,Prefix,FirstName,LastName,BirthDate,MaritalStatus,Gender,EmailAddress,AnnualIncome,TotalChildren,EducationLevel,Occupation,HomeOwner],
Products - [ Columns - ProductKey,ProductSubcategoryKey,ProductSKU,ProductName,ModelName,ProductDescription,ProductColor,ProductSize,ProductStyle,ProductCost,ProductPrice],
Product_Categories - [ Columns - ProductCategoryKey,CategoryName],
Product_Subcategories - [ Columns - ProductSubcategoryKey,SubcategoryName,ProductCategoryKey],
Territory - [ Columns - SalesTerritoryKey,Region,Country,Continent],
Sales_Years - [ Columns - YearKey,Year],
Sales - [ Columns - OrderDate,StockDate,OrderNumber,ProductKey,CustomerKey,TerritoryKey,OrderLineItem,OrderQuantity]
----------------------------------------------------------------------------------------------------

# Steps-3 :: Data Transformation Layer ​:: Data Warehouse:

A. HOP-1

Fetch Source-Data from Staging Tables to HOP-1 tables (Example: staging_Customers -> DTL_DW_HOP1_Customers)
1. Create My SQL Script to create all the tables with autoincrement primary kay (if table is already exist then no need to create table only update data) 
2. Every table name will contain a prefix with Example: DTL_DW_HOP1_Customers
----HOP-1 Tables----
	Customers - [Columns - CustomerKey,Prefix,FirstName,LastName,BirthDate,MaritalStatus,Gender,EmailAddress,AnnualIncome,TotalChildren,EducationLevel,Occupation,HomeOwner],
	Products - [ Columns - ProductKey,ProductSubcategoryKey,ProductSKU,ProductName,ModelName,ProductDescription,ProductColor,ProductSize,ProductStyle,ProductCost,ProductPrice],
	Product_Categories - [ Columns - ProductCategoryKey,CategoryName],
	Product_Subcategories - [ Columns - ProductSubcategoryKey,SubcategoryName,ProductCategoryKey],
	Territory - [ Columns - SalesTerritoryKey,Region,Country,Continent],
	Sales_Years - [ Columns - YearKey,Year],
	Sales - [ Columns - OrderDate,StockDate,OrderNumber,ProductKey,CustomerKey,TerritoryKey,OrderLineItem,OrderQuantity]

B. HOP-2
Fetch Source-Data from HOP-1 Tables to HOP-2 tables (Example: DTL_DW_HOP1_Customers -> DTL_DW_HOP2_Customers)
1. Create My SQL Script to create all the tables with autoincrement primary kay (if table is already exist then no need to create table only update data) 
2. Every table name will contain a prefix with Example: DTL_DW_HOP2_Customers
----HOP-2 Tables----
	Customers - [Columns - CustomerKey,Prefix,FirstName,LastName,BirthDate,MaritalStatus,Gender,EmailAddress,AnnualIncome,TotalChildren,EducationLevel,Occupation,HomeOwner],
	Sales - [ Columns - OrderDate,StockDate,OrderNumber,ProductKey,CustomerKey,TerritoryKey,OrderLineItem,OrderQuantity]

----------------------------------------------------------------------------------------------------

# Steps-4 :: Final Layer :: Data Marts:

Fetch Source-Data from HOP-2 Tables to Data Marts tables (Example: DTL_DW_HOP2_Customers -> FL_DM_Customers)
1. Create My SQL Script to create all the tables with autoincrement primary kay (if table is already exist then no need to create table only update data) 
2. Every table name will contain a prefix with Example: FL_DM_Customers
Note: In HOP-2 there are only 2 tables, but Final Layer/Data Marts Layer 7 tables are available, if HOP-2 data source is not available then data source will be HOP-1 for Final Layer. 
----Data Marts Tables----
	Customers - [Columns - CustomerKey,Prefix,FirstName,LastName,BirthDate,MaritalStatus,Gender,EmailAddress,AnnualIncome,TotalChildren,EducationLevel,Occupation,HomeOwner],
	Products - [ Columns - ProductKey,ProductSubcategoryKey,ProductSKU,ProductName,ModelName,ProductDescription,ProductColor,ProductSize,ProductStyle,ProductCost,ProductPrice],
	Product_Categories - [ Columns - ProductCategoryKey,CategoryName],
	Product_Subcategories - [ Columns - ProductSubcategoryKey,SubcategoryName,ProductCategoryKey],
	Territory - [ Columns - SalesTerritoryKey,Region,Country,Continent],
	Sales_Years - [ Columns - YearKey,Year],
	Sales - [ Columns - OrderDate,StockDate,OrderNumber,ProductKey,CustomerKey,TerritoryKey,OrderLineItem,OrderQuantity]

Notes: 
- We need to create below views and these are the final views which we want in the database
- View for Customer Retention and Churn Analysis: This view helps in understanding customer retention and churn by identifying customers who havent made a purchase in a significant period
- View for Customer Lifetime Value (CLV): This view calculates the lifetime value of each customer based on their total spend and order frequency, providing insights into the most valuable customers.

--------------------------

Steps-5 :: [ Report: End User Module]
We need to create the user specific dashboards and below is the list of dashboards which we need
· Executive Dashboard
· Product Analysis ( Bar Chart, Pie Chart)
· Customer 360 Degree Vie


