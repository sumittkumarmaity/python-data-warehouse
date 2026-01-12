CREATE OR REPLACE VIEW vw_customer_retention AS
SELECT
    c.CustomerKey,
    MAX(s.OrderDate) AS LastPurchaseDate,
    DATEDIFF(CURDATE(), MAX(s.OrderDate)) AS DaysSinceLastPurchase
FROM FL_DM_Customers c
LEFT JOIN FL_DM_Sales s
ON c.CustomerKey = s.CustomerKey
GROUP BY c.CustomerKey;
