-- Sales Data Load for DW HOP2 --
INSERT INTO TBL_DTL_DW_HOP2_Sales
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
FROM TBL_DTL_DW_HOP1_Sales 