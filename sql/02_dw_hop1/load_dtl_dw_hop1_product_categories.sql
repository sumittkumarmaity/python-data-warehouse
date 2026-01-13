-- Populate the DW_HOP1 Product Categories table from the staging area --
INSERT INTO TBL_DTL_DW_HOP1_Product_Categories
(
    ProductCategoryKey,
    CategoryName
)
SELECT
    spc.ProductCategoryKey,
    spc.CategoryName
FROM TBL_Staging_Product_Categories spc
WHERE spc.ProductCategoryKey IS NOT NULL;