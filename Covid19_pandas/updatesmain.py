def main():
 """
📊 Project: COVID Trends Visualizer
🧑‍💻 Author: Krishn Meena

🔎 Description:
This project analyzes global COVID-19 trends using a cleaned dataset (`country_wise_latest.csv`). 
It calculates key statistics such as total confirmed cases, deaths, and recoveries, identifies top-affected countries, 
visualizes regional data, and computes overall fatality and recovery rates.

🎯 Functionalities:
1. Clean dataset and rename columns
2. Calculate global totals for confirmed, deaths, and recoveries
3. Identify top 5 countries by:
   - Total deaths
   - Total confirmed cases
   - 1-week % increase
4. Visualize:
   - Line chart of confirmed cases by country
   - Pie charts of deaths and confirmed cases by WHO Region
5. Compute:
   - Regional totals
   - Global fatality and recovery rates

📂 Outputs:
- CSV files: `top5_death.csv`, `top5_Confirmed.csv`, `top5_weekly.csv`, `regional_total.csv`
- Charts: `Region wise death.png`, `Region wise confirmed.png`, etc.

📦 Dependencies:
- pandas
- matplotlib

▶️ How to Run:
Make sure `country_wise_latest.csv` is in the same directory and run:
    python covid_visualizer.py
"""
 import pandas as pd 
 import matplotlib.pyplot as plt
 from pathlib import Path

 file_path = Path("country_wise_latest.csv")
 df=pd.read_csv(file_path)
 pd.set_option('display.max_columns', None)
 new_df=df.dropna()
 new_df.rename(columns={'Country/Region':'Country'},inplace=True)
 
 #Top 5 Country,deathwise
 top5_death = (new_df.sort_values("Deaths", ascending=False)
 .reset_index(drop=True)
 .assign(Rank=lambda d:d.index+1)
 .loc[:,['Rank','Country','Deaths']]
 .head(5))
 top5_death.to_csv("top5_death.csv")
 print("\nTop 5 Country,deathwise-" )
 print(top5_death)

 #Top 5 Total confirmed Cases & line graph & bar chart
 top5_Confirmed = (new_df.sort_values("Confirmed", ascending=False)
 .reset_index(drop=True)
 .assign(Rank=lambda d:d.index+1)
 .loc[:,['Rank','Country','Confirmed']]
 .head(5))
 top5_Confirmed.to_csv("top5_Confirmed.csv")
 print("\nTop 5 Total confirmed Cases -" )
 print(top5_Confirmed)

 plt.figure(figsize=(10, 6))
 plt.plot(top5_Confirmed["Country"], top5_Confirmed["Confirmed"],marker='o', linestyle='-', color='green'
  )
 plt.xlabel("country")
 plt.ylabel("confirmed cases")
 plt.title("Top 5 Countries by Confirmed COVID-19 Cases")
 plt.tight_layout()
 plt.show()
 plt.savefig("country vs confirmed cases.png")

 #Top 5 Country,1 week % increase
 top5_weekly = (new_df.sort_values("1 week % increase", ascending=False)
 .reset_index(drop=True)
 .assign(Rank=lambda d:d.index+1)
 .loc[:,['Rank','Country','1 week % increase']]
 .head(5))
 top5_weekly.to_csv("top5_weekly.csv")
 print("\nTop 5 Country,weekly bases-" )
 print(top5_weekly)

 #Region wise detail & pie chart
 regional_total=df.groupby("WHO Region") [["Confirmed","Deaths"]].sum()
 regional_total.to_csv("regional_total.csv")
 print("Total Regional cases")
 print(regional_total.sort_values("Confirmed", ascending=False))

 regionaldeath_total=df.groupby("WHO Region") ["Deaths"].sum()
 plt.figure(figsize=(16,16))      # make it square
 regionaldeath_total.plot.pie(
    autopct='%1.1f%%',         # show percentages
    startangle=90,             # rotate so first slice starts at 12 o'clock
    legend=False               # turn off the legend (labels will be on slices)
 )

 plt.ylabel('')                 # hidey‑label
 plt.title('regional total death cases')     # add a title
 plt.tight_layout()  # better spacing
 plt.show()     
 plt.savefig("Region wise death.png")

 regionalconfirmed_total=df.groupby("WHO Region") ["Confirmed"].sum()
 plt.figure(figsize=(16,16))      # make it square
 regionalconfirmed_total.plot.pie(
    autopct='%1.1f%%',         # show percentages
    startangle=90,             # rotate so first slice starts at 12 o'clock
    legend=False               # turn off the legend (labels will be on slices)
 )

 plt.ylabel('')                 # hidey‑label
 plt.title('regional total confirmed cases')     # add a title
 plt.tight_layout()             # better spacing
 plt.show()
 plt.savefig("Region wise confirmed.png")

 #global fatality and recovery rate
 total_death=df["Deaths"].sum()
 total_recovered=df["Recovered"].sum()
 total_confirmed=df["Confirmed"].sum()
 print(f"\nToatl death:{total_death},\nTotal confirmed:{total_confirmed} \nTotal recovered :{total_recovered}")

 print(f"Global Fatality rate:{total_death*100/total_confirmed}\nRecovery rate:{total_recovered*100/total_confirmed}")

if __name__ == "__main__":
    main()
