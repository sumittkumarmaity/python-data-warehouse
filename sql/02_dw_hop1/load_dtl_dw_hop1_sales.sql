-- Sales Data Load for DW HOP1 --
INSERT INTO TBL_DTL_DW_HOP1_Sales
(
    CustomerKey,
    OrderDate,
    StockDate,
    OrderNumber,
    ProductKey,
    TerritoryKey,
    OrderLineItem,
    OrderQuantity,
    SalesYear,
    Sales,
    Profit
)
SELECT
    ss.CustomerKey,
    ss.OrderDate,
    ss.StockDate,
    ss.OrderNumber,
    ss.ProductKey,
    ss.TerritoryKey,
    ss.OrderLineItem,
    ss.OrderQuantity,
    ss.SalesYear,
    ROUND(p.ProductPrice * ss.OrderQuantity, 2) AS Sales,
    ROUND((p.ProductPrice - p.ProductCost) * ss.OrderQuantity, 2) AS Profit
FROM TBL_Staging_Sales ss
JOIN TBL_DTL_DW_HOP1_Products p
    ON ss.ProductKey = p.ProductKey
WHERE ss.CustomerKey IS NOT NULL
    AND ss.ProductKey IS NOT NULL;