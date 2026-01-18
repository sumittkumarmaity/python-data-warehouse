import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config.db_connection import get_engine

# Set up the overall aesthetics for the dashboard
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(3, 2, figsize=(16, 20), constrained_layout=True)
fig.suptitle("DESCRIPTIVE ANALYTICS DASHBOARD", fontsize=16, y=1.02 )
fig.canvas.manager.set_window_title("Descriptive Analytics Dashboard")
# Grid positions for subplots
position1 = (0, 0) 
position2 = (0, 1)
position3 = (1, 0)
position4 = (1, 1)
position5 = (2, 0)
position6 = (2, 1)

# Function to fetch data from the database
def fetch_df(query):
    engine = get_engine()
    df = pd.read_sql(query, engine)
    engine.dispose()
    return df

# Function to draw borders around subplots
def draw_bordered_barplot(axes):
    for ax in [axes[position1], axes[position2], axes[position3], axes[position4], axes[position5], axes[position6]]:
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("red")
            spine.set_linewidth(1)

# Function to load and display the Descriptive Analytics Dashboard
def Load_DESCRIPTIVE_ANALYTICS_DASHBOARD():
    
    # Draw borders around subplots
    draw_bordered_barplot(axes)
    
    # ---------------- 1. Customer Demographics ----------------
   
    df = fetch_df("SELECT c.Gender, c.MaritalStatus, SUM(s.Sales) AS TotalSales FROM TBL_FL_DM_Customers c JOIN TBL_FL_DM_Sales s ON c.CustomerKey = s.CustomerKey GROUP BY c.Gender, c.MaritalStatus;")
    sns.barplot(data = df, x = "Gender", y = "TotalSales", hue = "MaritalStatus", ax=axes[position1] )
    axes[position1].set_xlabel("Customer Gender", fontsize=10, fontweight="bold")
    axes[position1].set_ylabel("Total Sales", fontsize=10, fontweight="bold")
    axes[position1].set_title("Customer Demographics vs Sales", fontsize=10, color="#099638")
    axes[position1].tick_params(labelsize=9)
    axes[position1].legend(fontsize=7)
 
    # ---------------- 2. Sales Trend ----------------
    
    df = fetch_df("SELECT YEAR(OrderDate) AS Year, MONTH(OrderDate) AS Month, SUM(Sales) AS TotalSales FROM TBL_FL_DM_Sales GROUP BY Year, Month ORDER BY Year, Month;")
    df["YearMonth"] = df["Year"].astype(str) + "-" + df["Month"].astype(str)
    sns.lineplot(data=df, x="YearMonth", y="TotalSales", marker="o", linewidth=2, ax=axes[position2])
    axes[position2].set_xlabel("Year & Month", fontsize=10, fontweight="bold")
    axes[position2].set_ylabel("Total Sales", fontsize=10, fontweight="bold")
    axes[position2].tick_params(axis="x", rotation=90, labelsize=8)
    axes[position2].set_title("Sales Trend Over Time", fontsize=10, color="#099638")

    # ---------------- 3. Category Popularity ----------------
    
    df = fetch_df("SELECT pc.CategoryName, SUM(s.OrderQuantity) AS ItemsSold FROM TBL_FL_DM_Sales s JOIN TBL_FL_DM_Products p ON s.ProductKey = p.ProductKey  JOIN TBL_FL_DM_Product_Subcategories ps ON p.ProductSubcategoryKey = ps.ProductSubcategoryKey JOIN TBL_FL_DM_Product_Categories pc ON ps.ProductCategoryKey = pc.ProductCategoryKey GROUP BY pc.CategoryName;")
    wedges = axes[position3].pie(df["ItemsSold"], labels=df["CategoryName"], autopct="%1.1f%%", startangle=90, radius=2, labeldistance=0.55, pctdistance=0.75, textprops={"fontsize": 9, "color": "white", "fontweight": "bold"} )
    axes[position3].legend( wedges, df["CategoryName"], title="Category", loc="center right", fontsize=8, frameon=True)
    axes[position3].set_title("Product Category Wise Sales", fontsize=10, fontweight="bold", color="#099638")
    axes[position3].axis("equal") 
    

    # ---------------- 4. Geographic Sales ----------------
    
    df = fetch_df("SELECT t.Region, t.Country, SUM(s.Sales) AS TotalSales FROM TBL_FL_DM_Sales s JOIN TBL_FL_DM_Territory t ON s.TerritoryKey = t.SalesTerritoryKey GROUP BY t.Region, t.Country;")
    sns.barplot( data=df, x="Region", y="TotalSales", hue="Country", ax=axes[position4] )
    axes[position4].set_xlabel("Region", fontsize=10, fontweight="bold")
    axes[position4].set_ylabel("Total Sales", fontsize=10, fontweight="bold")
    axes[position4].set_title("Geographical Sales", fontsize=10, color="#099638")
    axes[position4].tick_params(axis="x", rotation=45, labelsize=8)
    axes[position4].legend(fontsize=6)

    # ---------------- 5. Profit per Product ----------------

    df = fetch_df("SELECT p.ProductName, SUM(s.Profit) AS TotalProfit FROM TBL_FL_DM_Sales s JOIN TBL_FL_DM_Products p ON s.ProductKey = p.ProductKey GROUP BY p.ProductName ORDER BY TotalProfit DESC LIMIT 10;")
    sns.barplot(data=df, x="TotalProfit", y="ProductName", ax=axes[position5])
    axes[position5].set_xlabel("Total Profit", fontsize=10, fontweight="bold")
    axes[position5].set_ylabel("Products", fontsize=10, fontweight="bold")
    axes[position5].set_title("Top Profitable Products", fontsize=10, color="#099638")
    axes[position5].tick_params(labelsize=8)

    # ---------------- 6. Top Customers ----------------

    df = fetch_df("SELECT c.CustomerName, SUM(s.Profit) AS TotalProfit FROM TBL_FL_DM_Customers c JOIN TBL_FL_DM_Sales s ON c.CustomerKey = s.CustomerKey GROUP BY c.CustomerName ORDER BY TotalProfit DESC LIMIT 5")
    sns.barplot(data=df, x="TotalProfit", y="CustomerName", ax=axes[position6])
    axes[position6].set_xlabel("Total Profit", fontsize=10, fontweight="bold")
    axes[position6].set_ylabel("Customers", fontsize=10, fontweight="bold")
    axes[position6].set_title("Top 5 Profitable Customers", fontsize=10, color="#099638")
    axes[position6].tick_params(labelsize=8)

    plt.show() # Display the dashboard


   

