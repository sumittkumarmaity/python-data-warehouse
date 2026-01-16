-- Load data into DTL_DW_HOP1_Customers from staging_Customers --
INSERT INTO TBL_DTL_DW_HOP1_Customers
(
    CustomerKey,
    CustomerName,
    BirthDate,
    Age,
    MaritalStatus,
    Gender,
    EmailAddress,
    AnnualIncome,
    TotalChildren,
    EducationLevel,
    Occupation,
    HomeOwner
)
SELECT
    sc.CustomerKey,
    CONCAT(
        COALESCE(NULLIF(sc.Prefix, ''), 'NA'), ' ',
        COALESCE(NULLIF(sc.FirstName, ''), 'NA'), ' ',
        COALESCE(NULLIF(sc.LastName, ''), 'NA')
    ) AS CustomerName,
    COALESCE(sc.BirthDate, CURDATE()) AS BirthDate,
    TIMESTAMPDIFF(
        YEAR,
        COALESCE(sc.BirthDate, CURDATE()),
        CURDATE()
    ) AS Age,
    CASE
        WHEN sc.MaritalStatus IS NULL OR sc.MaritalStatus = 'NA' THEN 'Did not Disclose'
        WHEN sc.MaritalStatus = 'S' THEN 'Single'
        ELSE 'Married'
    END AS MaritalStatus,
    CASE
        WHEN sc.Gender IS NULL OR sc.Gender = 'NA' THEN 'Did not Disclose'
        WHEN sc.Gender = 'M' THEN 'Male'
        ELSE 'Female'
    END AS Gender,
    sc.EmailAddress,
    sc.AnnualIncome,
    sc.TotalChildren,
    sc.EducationLevel,
    sc.Occupation,
    CASE
        WHEN sc.HomeOwner = 'Y' THEN 'Yes'
        ELSE 'No'
    END AS HomeOwner
FROM TBL_Staging_Customers sc
WHERE sc.CustomerKey IS NOT NULL;
