CREATE TABLE IF NOT EXISTS staging_Sales_Years (
    YearKey INT PRIMARY KEY,
    Year INT
);

INSERT IGNORE INTO staging_Sales_Years VALUES
(1, 2020),
(2, 2021),
(3, 2022);
