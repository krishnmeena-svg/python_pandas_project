def main():
 """IPL Stats Analyzer
Author: Krishn Meena

Description:
This script performs data analysis on an IPL dataset using pandas and matplotlib. 
It provides useful insights such as:

1. Total matches played by each team
2. Total runs scored by each team
3. Top 10 run-getters
4. Top 10 wicket-takers
5. Distribution of players by country (Pie Chart)

Outputs:
- teams_runs.csv: Total runs scored per team
- top10_runs.csv: Top 10 players by runs
- top10_bowler.csv: Top 10 bowlers by wickets
- country_distribution.png: Pie chart showing number of players by country

Note:
Ensure the input CSV file 'IPL dataset final.csv' is present in the same directory.
Required Libraries: pandas, matplotlib
"""

 import pandas as pd
 import matplotlib.pyplot as plt
 from pathlib import Path

 file_path = Path("IPL_dataset_final.csv")
 df=pd.read_csv(file_path)
 pd.set_option('display.max_columns', None)

 # Team total runs 
 teams_runs=df.groupby('TEAM')['Runs'].sum()
 teams_runs.to_csv("teams_runs.csv")
 print("Total Runs Scored by Each Team:")
 print(teams_runs.sort_values(ascending=False))

 #Top‑10 run‑getters
 top10_runs = (df.sort_values("Runs", ascending=False)
 .reset_index(drop=True)
 .assign(Rank=lambda d:d.index+1)
 .loc[:,['Rank', 'Player','Runs']]
 .head(10))
 top10_runs.to_csv("top10_runs.csv")
 print("\nTop-10 Runs getter" )
 print(top10_runs)

 #Top‑10 Wicket taker
 bowler_wicket= df[df['B_Wkts'].notnull()]
 top10_bowler=(bowler_wicket.sort_values("B_Wkts", ascending=False)
 .reset_index(drop=True)
 .assign(Rank=lambda d:d.index+1)
 .loc[:,['Rank', 'Player','B_Wkts']]
 .head(10))
 top10_bowler.to_csv("top10_bowler.csv")
 print("\nTop-10 wicket taker" )
 print(top10_bowler)

 #pie chart of player countrywise
 group_country=df['COUNTRY'].value_counts()
 plt.figure(figsize=(10,8))
 group_country.plot.pie(
    labels=None,
    autopct=None,
    startangle=90,
    legend=False
  )
 percentages = group_country /  group_country.sum() * 100
 custom_labels = [f"{COUNTRY}: {pct:.2f}%" for COUNTRY, pct in zip( group_country.index, percentages)]
 # Manually add and position the legend
 plt.legend(
    labels=custom_labels,
    title="Countrwise Player percentage",
    bbox_to_anchor=(1,0.5),
    loc='upper left',
    ncol=3,                      
    fontsize='small'
     )
 plt.title("Distribution of Players by Country")
 plt.axis('equal')  # to make it a circle
 plt.ylabel('')
 plt.tight_layout()
 plt.savefig("country_distribution.png")
 plt.show()

if __name__ == "__main__":
    main()


