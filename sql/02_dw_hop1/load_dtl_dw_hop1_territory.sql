-- Territory Data Load into DTL_DW_HOP1_Territory Table --
INSERT INTO TBL_DTL_DW_HOP1_Territory
(
    SalesTerritoryKey,
    Region,
    Country,
    Continent
)
SELECT
    st.SalesTerritoryKey,
    st.Region,
    st.Country,
    st.Continent
FROM TBL_Staging_Territory st
WHERE st.SalesTerritoryKey IS NOT NULL;