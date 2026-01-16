import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config.db_connection import get_connection

sns.set_theme(style="whitegrid")

def fetch_df(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def draw_bordered_barplot(axes):
    for ax in [axes[0,0], axes[0,1], axes[1,0], axes[1,1], axes[2,0], axes[2,1], axes[3,0]]:
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("red")
            spine.set_linewidth(1)

def Load_DESCRIPTIVE_ANALYTICS_DASHBOARD():

    fig, axes = plt.subplots(4, 2, figsize=(16, 20), constrained_layout=True)
    fig.suptitle("DESCRIPTIVE ANALYTICS DASHBOARD", fontsize=16, y=1.02 )
    draw_bordered_barplot(axes)
    

    # ---------------- 1. Customer Demographics ----------------
    query = """
    SELECT c.Gender, c.MaritalStatus,
           SUM(s.Sales) AS TotalSales
    FROM TBL_FL_DM_Customers c
    JOIN TBL_FL_DM_Sales s
      ON c.CustomerKey = s.CustomerKey
    GROUP BY c.Gender, c.MaritalStatus;
    """
    df = fetch_df(query)
    sns.barplot(data=df, x="Gender", y="TotalSales", hue="MaritalStatus", ax=axes[0, 0] )
    axes[0, 0].set_xlabel("Customer Gender", fontsize=10, fontweight="bold")
    axes[0, 0].set_ylabel("Total Sales (₹)", fontsize=10, fontweight="bold")
    axes[0, 0].set_title("Customer Demographics vs Sales", fontsize=10, color="#1f4e79")
    axes[0, 0].tick_params(labelsize=9)
    axes[0, 0].legend(fontsize=7)
 

    # ---------------- 2. Product Sales Performance ----------------
    query = """
    SELECT p.ProductName,
           SUM(s.OrderQuantity) AS TotalQuantity
    FROM TBL_FL_DM_Sales s
    JOIN TBL_FL_DM_Products p
      ON s.ProductKey = p.ProductKey
    GROUP BY p.ProductName
    ORDER BY TotalQuantity DESC
    LIMIT 10;
    """
    df = fetch_df(query)
    sns.barplot(data=df, x="TotalQuantity", y="ProductName", ax=axes[0, 1])
    axes[0, 1].set_xlabel("Total Quantity", fontsize=10, fontweight="bold")
    axes[0, 1].set_ylabel("Products", fontsize=10, fontweight="bold")
    axes[0, 1].set_title("Top 10 Products", fontsize=10, color="#1f4e79")
    axes[0, 1].tick_params(labelsize=9)
    axes[0, 1].legend(fontsize=8)


    # ---------------- 3. Sales Trend ----------------
    query = """
    SELECT YEAR(OrderDate) AS Year,
           MONTH(OrderDate) AS Month,
           SUM(Sales) AS TotalSales
    FROM TBL_FL_DM_Sales
    GROUP BY Year, Month
    ORDER BY Year, Month;
    """
    df = fetch_df(query)
    df["YearMonth"] = df["Year"].astype(str) + "-" + df["Month"].astype(str)
    sns.lineplot(data=df, x="YearMonth", y="TotalSales", marker="o", linewidth=2, ax=axes[1, 0])
    axes[1, 0].set_xlabel("Year & Month", fontsize=10, fontweight="bold")
    axes[1, 0].set_ylabel("Total Sales", fontsize=10, fontweight="bold")
    axes[1, 0].tick_params(axis="x", rotation=90, labelsize=8)
    axes[1, 0].set_title("Sales Trend Over Time", fontsize=10, color="#1f4e79")

    # ---------------- 4. Category Popularity ----------------
    query = """
    SELECT pc.CategoryName,
           SUM(s.OrderQuantity) AS ItemsSold
    FROM TBL_FL_DM_Sales s
    JOIN TBL_FL_DM_Products p ON s.ProductKey = p.ProductKey
    JOIN TBL_FL_DM_Product_Subcategories ps ON p.ProductSubcategoryKey = ps.ProductSubcategoryKey
    JOIN TBL_FL_DM_Product_Categories pc ON ps.ProductCategoryKey = pc.ProductCategoryKey
    GROUP BY pc.CategoryName;
    """
    df = fetch_df(query)
    sns.barplot( data=df, x="ItemsSold", y="CategoryName", ax=axes[1, 1])
    axes[1, 1].set_xlabel("Items Sold", fontsize=10, fontweight="bold")
    axes[1, 1].set_ylabel("Product Category", fontsize=10, fontweight="bold")
    axes[1, 1].set_title("Product Category Popularity", fontsize=10, color="#1f4e79")
    axes[1, 1].tick_params(labelsize=8)

    # ---------------- 5. Geographic Sales ----------------
    query = """
    SELECT t.Region, t.Country,
           SUM(s.Sales) AS TotalSales
    FROM TBL_FL_DM_Sales s
    JOIN TBL_FL_DM_Territory t
      ON s.TerritoryKey = t.SalesTerritoryKey
    GROUP BY t.Region, t.Country;
    """
    df = fetch_df(query)
    sns.barplot( data=df, x="Region", y="TotalSales", hue="Country", ax=axes[2, 0] )
    axes[2, 0].set_xlabel("Region", fontsize=10, fontweight="bold")
    axes[2, 0].set_ylabel("Total Sales", fontsize=10, fontweight="bold")
    axes[2, 0].set_title("Geographical Sales", fontsize=10, color="#1f4e79")
    axes[2, 0].tick_params(labelsize=8)
    axes[2, 0].legend(fontsize=6)

    # ---------------- 6. Profit per Product ----------------
    query = """
    SELECT p.ProductName,
           SUM(s.Profit) AS TotalProfit
    FROM TBL_FL_DM_Sales s
    JOIN TBL_FL_DM_Products p
      ON s.ProductKey = p.ProductKey
    GROUP BY p.ProductName
    ORDER BY TotalProfit DESC
    LIMIT 10;
    """
    df = fetch_df(query)
    sns.barplot(data=df, x="TotalProfit", y="ProductName", ax=axes[2, 1])
    axes[2, 1].set_xlabel("Total Profit", fontsize=10, fontweight="bold")
    axes[2, 1].set_ylabel("Products", fontsize=10, fontweight="bold")
    axes[2, 1].set_title("Top Profitable Products", fontsize=10, color="#1f4e79")
    axes[2, 1].tick_params(labelsize=8)

    # ---------------- 7. Top Customers ----------------
    query = """
    SELECT c.CustomerName,
           SUM(s.Profit) AS TotalProfit
    FROM TBL_FL_DM_Customers c
    JOIN TBL_FL_DM_Sales s
      ON c.CustomerKey = s.CustomerKey
    GROUP BY c.CustomerName
    ORDER BY TotalProfit DESC
    LIMIT 5;
    """
    df = fetch_df(query)
    sns.barplot( data=df, x="TotalProfit", y="CustomerName", ax=axes[3, 0])
    axes[3, 0].set_xlabel("Total Profit", fontsize=10, fontweight="bold")
    axes[3, 0].set_ylabel("Customers", fontsize=10, fontweight="bold")
    axes[3, 0].set_title("Top 5 Profitable Customers", fontsize=10, color="#1f4e79")
    axes[3, 0].tick_params(labelsize=8)

    # Remove unused subplot
    fig.delaxes(axes[3, 1])

    plt.show()


   

