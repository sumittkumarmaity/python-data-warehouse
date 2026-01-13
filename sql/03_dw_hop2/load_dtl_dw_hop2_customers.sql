-- Load data into TBL_DTL_DW_HOP2_Customers from staging_Customers --
INSERT INTO TBL_DTL_DW_HOP2_Customers
(
    CustomerKey,
    CustomerName,
    BirthDate,
    Age,
    MaritalStatus,
    EmailAddress,
    AnnualIncome,
    TotalChildren,
    EducationLevel,
    Occupation,
    HomeOwner,
    CustomerType
)
SELECT
    c.CustomerKey,
    c.CustomerName,
    c.BirthDate,
    c.Age,
    c.MaritalStatus,
    c.EmailAddress,
    c.AnnualIncome,
    c.TotalChildren,
    c.EducationLevel,
    c.Occupation,
    c.HomeOwner,

    CASE
        WHEN s.TotalProfit IS NULL THEN 'Prospects'
        WHEN s.TotalProfit > 4000 THEN 'Platinum'
        WHEN s.TotalProfit BETWEEN 2000 AND 4000 THEN 'Gold'
        WHEN s.TotalProfit >= 1000 AND s.TotalProfit < 2000 THEN 'Silver'
        ELSE 'Bronze'
    END AS CustomerType

FROM TBL_DTL_DW_HOP1_Customers c
LEFT JOIN
(
    SELECT
        CustomerKey,
        SUM(Profit) AS TotalProfit
    FROM TBL_DTL_DW_HOP1_Sales
    GROUP BY CustomerKey
) s
    ON c.CustomerKey = s.CustomerKey;
