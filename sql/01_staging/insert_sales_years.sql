CREATE TABLE IF NOT EXISTS TBL_Staging_Sales_Years (
    YearKey INT PRIMARY KEY,
    Year INT
);

INSERT IGNORE INTO TBL_Staging_Sales_Years VALUES
(1, 2020),
(2, 2021),
(3, 2022);
