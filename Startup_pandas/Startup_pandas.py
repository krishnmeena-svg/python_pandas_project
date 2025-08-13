def main(): 
 """
📊 Project: Indian Startup Funding Analysis
🧑‍💻 Author: Krishn Meena

🔍 Description:
This project analyzes startup funding trends in India using a CSV dataset.
It explores yearly startup counts, top-funded industries and cities, 
sector-wise funding totals, and visualizes time-based investment patterns.

🎯 Functionalities:
1. Cleans and parses date columns accurately (handles dirty or missing data).
2. Analyzes:
   - Startup funding counts by year
   - Top 10 industries and cities by number of startups
   - Sector-wise total funding raised
   - Yearly funding trends (visualized on log scale)
3. Generates insightful visualizations using bar and line plots.
4. Saves CSV summaries and PNG plots to support reproducibility.

📂 Outputs:
- CSVs:
    - group_startup.csv
    - group_industry.csv
    - group_cities.csv
    - group_sector.csv
    - group_year.csv
- Charts:
    - year wise startup funded.png
    - Industrywise startup funded.png
    - Top 10 cities with most startup funded.png
    - Top 10 sector with most Value funded.png
    - Total Funding Per Year.png

📦 Dependencies:
- pandas
- matplotlib

▶️ How to Run:
Ensure 'startup_funding.csv' is available in the script directory, then run:
    python startup_funding_analysis.py
"""
 import pandas as pd 
 import matplotlib.pyplot as plt
 from pathlib import Path

 file_path = Path(r"C:\Users\krish\Desktop\IT Skill\IT Skill\personal\Numphy & Pandas\Startup_pandas\startup_funding.csv")
 df=pd.read_csv(file_path)
 pd.set_option('display.max_columns', None)

 #1.parse DateTime
 df["Date dd/mm/yyyy"] = df["Date dd/mm/yyyy"].astype(str).str.strip().str.replace(r'\\xc2\\xa0', '', regex=True)
 df["Date dd/mm/yyyy"] = pd.to_datetime(df["Date dd/mm/yyyy"], dayfirst=True,errors="coerce")
 df["month"]=df["Date dd/mm/yyyy"].dt.month
 df["year"]=df['Date dd/mm/yyyy'].dt.year
 print(df['Date dd/mm/yyyy'].isna().sum(), "rows couldn't be parsed")

 #2.yearwise startupcount
 group_startup=df.groupby("year")["Startup Name"].count()
 group_startup.to_csv("group_startup.csv")
 print(f"year wise startup funded:\n{group_startup.sort_values(ascending=False)}")
 plt.figure(figsize=(10, 8))
 group_startup.plot.bar(
    color='yellow',
    edgecolor='black',
    title="year wise startup funded")

 plt.xlabel("year")
 plt.ylabel("Number of startup")
 plt.xticks(rotation=45, ha='right')  # rotate labels if long
 plt.tight_layout()
 plt.savefig("year wise startup funded.png")
 plt.show()

 #3.industrywise startup of top 10 industry
 df['Industry Vertical']=df["Industry Vertical"].str.strip()
 group_industry=df.groupby("Industry Vertical")["Startup Name"].count().sort_values(ascending=False).head(10)
 group_industry.to_csv("group_industry.csv")
 print(f"Top 10 Industrywise startup funded:\n{group_industry}")
 plt.figure(figsize=(10, 8))
 group_industry.plot.bar(
    color='red',
    edgecolor='black',
    title="Industrywise startup funded")

 plt.xlabel("Industry")
 plt.ylabel("Number of startup")
 plt.xticks(rotation=45, ha='right')  # rotate labels if long
 plt.tight_layout()
 plt.savefig("Industrywise startup funded.png")
 plt.show()

 #4. cities with most startup
 df["City  Location"]=df["City  Location"].str.strip()
 group_cities=df.groupby("City  Location")["Startup Name"].count().sort_values(ascending=False).head(10)
 group_cities.to_csv("group_cities.csv")
 print(f"Top 10 cities with most startup funded:\n{group_cities}")
 plt.figure(figsize=(10, 8))
 group_cities.plot.bar(
    color='skyblue',
    edgecolor='black',
    title="Top 10 cities with most startup funded")

 plt.xlabel("City  Location")
 plt.ylabel("Number of startup")
 plt.xticks(rotation=45, ha='right')  # rotate labels if long
 plt.tight_layout()
 plt.savefig("Top 10 cities with most startup funded.png")
 plt.show()

 #5.sector wise funding
 df["Amount in USD"]=pd.to_numeric(df["Amount in USD"]
      .astype(str)
      .replace('undisclosed', pd.NA)
     .replace('N/A', pd.NA)
     .str.replace(',', '', regex=False), errors='coerce'
     )
 group_sector=df.groupby("Industry Vertical")["Amount in USD"].sum().sort_values(ascending=False).head(10)
 group_sector.to_csv("group_sector.csv")
 print(f"Top 10 sector with most funding value:\n{group_sector}")
 plt.figure(figsize=(10, 8))
 group_sector.plot.barh(
    color='orange',
    edgecolor='black',
    title="Top 10 sector with most funding value")

 plt.xlabel("Amount funded in USD")
 plt.ylabel("City  Location")
 plt.xticks(rotation=45, ha='right')  # rotate labels if long
 plt.tight_layout()
 plt.savefig("Top 10 sector with most funding value.png")
 plt.show()

 #6.yearly funding pattern
 group_year=df.groupby("year")["Amount in USD"].sum()
 group_year.to_csv("group_year.csv")
 print(f"Yearly Funding Pattern:\n{group_year}")
 plt.figure(figsize=(10, 5))
 plt.plot(group_year.index,group_year.values, marker='o')

 plt.yscale('log')
 plt.xlabel("Year")
 plt.ylabel("Total Funding")
 plt.title("Total Funding Per Year")
 plt.grid(True)
 plt.savefig("Total Funding Per Year.png")
 plt.show()

if __name__ == "__main__":
    main()
 


