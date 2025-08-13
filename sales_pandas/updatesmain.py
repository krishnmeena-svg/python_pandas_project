def main():
 """
Project: Sales Data Dashboard
Author: Krishn Meena
Description:
    This project analyzes a sample monthly sales dataset and visualizes key business metrics.
    It is designed as a portfolio project to demonstrate data analysis using pandas and matplotlib.

Functionalities:
    1. Calculates total orders and revenue per product line.
    2. Identifies the best-selling products based on quantity.
    3. Determines the month with the highest revenue.
    4. Aggregates total orders per month.
    5. Finds the top-earning product lines by sales.
    6. Calculates average sale value across all transactions.
    7. Displays pie chart-city_wise_revenue
                bar chart-Total sales month wise
                line graph-product vs order qty

Outputs:
    - Saves result tables as CSV files.
    - Saves graphs as PNG images .

Dependencies:
    - pandas
    - matplotlib

How to Run:
    python sales_analysis.py

Note:
    Make sure 'sales_data_sample.csv' is in the same directory, or update the file path accordingly.
"""
 import pandas as pd 
 import matplotlib.pyplot as plt
 from pathlib import Path

 file_path = Path('sales_data_sample.csv')
 df=pd.read_csv(file_path)
 pd.set_option('display.max_columns', None)


 #seperating month and year from ORDERDATE
 df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'],format='%m/%d/%Y %H:%M')
 df["MONTH"]=df['ORDERDATE'].dt.month
 df["MONTH"]=df['ORDERDATE'].dt.month_name()
 df["YEAR"]=df['ORDERDATE'].dt.year
 
 #1.Best selling product & Line graph of product vs order qty
 best_selling_product=df.groupby("PRODUCTLINE")["QUANTITYORDERED"].sum()
 best_selling_product.to_csv("best_selling_product.csv")
 print("\nBest Selling Product")
 print(best_selling_product.sort_values(ascending=False).head(1))

 best_selling_product.plot(  
    figsize=(10,5),      # chart size
    title="product vs order qty"
 )
 plt.xlabel("product")
 plt.ylabel("order qty")
 plt.tight_layout()
 plt.savefig("product vs order qty.png")
 plt.show()

 #2.Month with highest revenue & plot them as bar chart 
 df=df.set_index('ORDERDATE')
 monthly_sell=df['SALES'].resample('ME').sum()
 monthly_sell.index = monthly_sell.index.strftime('%b %Y')
 monthly_sell.to_csv("monthly_sell.csv")
 print("\nMonth with highest revenue")
 print(monthly_sell.sort_values(ascending=False).head(1))

 monthly_sell.plot.bar(
    figsize=(8,5),
    color='skyblue',
    edgecolor='black',
    title="Total Sales Month Wise"
 )

 plt.xlabel("Month")
 plt.ylabel("Sales")
 plt.xticks(rotation=45, ha='right')  # rotate labels if long
 plt.tight_layout()
 plt.savefig("Total Sales Month Wise.png")
 plt.show()

 #3.City with highest sales & Plot as pie chart
 city_sell=df.groupby("CITY")["SALES"].sum().sort_values(ascending=False)
 city_sell.to_csv("city_sell.csv")
 print("\nCity with highest sales")
 print(city_sell.head(1))

 plt.figure(figsize=(12,12))
 city_sell.plot.pie(
    labels=None,
    autopct=None,
    startangle=90,
    legend=False
  )
 percentages = city_sell / city_sell.sum() * 100
 custom_labels = [f"{CITY}: {pct:.2f}%" for CITY, pct in zip(city_sell.index, percentages)]
 # Manually add and position the legend
 plt.legend(
    labels=custom_labels,
    title="city sale pct",
    loc="best",
    bbox_to_anchor=(1,1),
    ncol=3,                      
    fontsize='small'
     )
 plt.ylabel('')                 # hide the “SALES” y‑label
 plt.title('Sales by City')     # add a title
 plt.tight_layout()             # better spacing
 plt.savefig("city_wise_revenue.png")
 plt.show()
 
 #4.Top earning product
 top_earn_product=df.groupby("PRODUCTLINE")["SALES"].sum()
 top_earn_product.to_csv("top_earn_product.csv")
 print("\nTop 5 earning product")
 print(top_earn_product.sort_values(ascending=False).head(5))

 #5.Total orders per month
 monthly_order=df['QUANTITYORDERED'].resample('ME').sum()
 monthly_order.to_csv("monthly_order.csv")
 print("\nMonth with highest total orders")
 print(monthly_order.sort_values(ascending=False).head(1))

 #6.Average sale value
 avg=df["SALES"].mean()
 print("\nAverage sale value")
 print(avg)

if __name__ == "__main__":
    main()

