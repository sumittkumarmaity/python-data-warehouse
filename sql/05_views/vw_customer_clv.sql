CREATE OR REPLACE VIEW vw_customer_clv AS
SELECT
    s.CustomerKey,
    COUNT(DISTINCT s.OrderNumber) AS TotalOrders,
    SUM(p.ProductPrice * s.OrderQuantity) AS LifetimeValue
FROM TBL_FL_DM_Sales s
JOIN TBL_FL_DM_Products p
ON s.ProductKey = p.ProductKey
GROUP BY s.CustomerKey;
