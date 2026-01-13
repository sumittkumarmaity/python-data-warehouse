-- Products Data Load into DTL_DW_HOP1_Products Table --
INSERT INTO TBL_DTL_DW_HOP1_Products
(
    ProductKey,
    ProductSubcategoryKey,
    ProductSKU,
    ProductName,
    ModelName,
    ProductDescription,
    ProductColor,
    ProductSize,
    ProductStyle,
    ProductCost,
    ProductPrice
)
SELECT
    sp.ProductKey,
    sp.ProductSubcategoryKey,
    sp.ProductSKU,
    sp.ProductName,
    sp.ModelName,
    sp.ProductDescription,
    sp.ProductColor,
    sp.ProductSize,
    sp.ProductStyle,
    ROUND(sp.ProductCost, 2) AS ProductCost,
    ROUND(sp.ProductPrice, 2) AS ProductPrice
FROM TBL_Staging_Products sp
WHERE sp.ProductKey IS NOT NULL;
