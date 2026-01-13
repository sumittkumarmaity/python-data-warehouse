-- Populate the DW_HOP1 Product Sub Categories table from the staging area --
INSERT INTO TBL_DTL_DW_HOP1_Product_Subcategories
(
    ProductSubcategoryKey,
    SubcategoryName,
    ProductCategoryKey
)
SELECT
    sps.ProductSubcategoryKey,
    sps.SubcategoryName,
    sps.ProductCategoryKey
FROM TBL_Staging_Product_Subcategories sps
WHERE sps.ProductSubcategoryKey IS NOT NULL;