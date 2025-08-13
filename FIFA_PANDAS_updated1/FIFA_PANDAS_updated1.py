def main(): 
 """
    ⚽ Project: FIFA 21 Career Mode Player Analysis
        Author: Krishn Meena
    🔍 Description:
    This project analyzes player statistics from FIFA 21, focusing on:
    - Top players by position
    - Club-level player value and potential comparisons
    - Correlation analysis between age, rating, skills, and value

    📊 Outputs:
    - Heatmap of correlations
    - Boxplots for top-valued and top-potential clubs

    💾 Dataset: Career Mode Player Dataset - FIFA 15–21 (FIFA 21 Sheet)
    📦 Libraries: pandas, seaborn, matplotlib
 """
 import pandas as pd
 import seaborn as sns
 import matplotlib.pyplot as plt
 from pathlib import Path
 
 file_path = Path("Career Mode player datasets - FIFA 15-21.xlsx")
 df=pd.read_excel(file_path)
 df.info(memory_usage="deep")
 pd.set_option('display.max_columns', None)
 df["club_name"] = df["club_name"].astype(str).str.strip()
 df["age"] = df["age"].astype("int8")
 df["overall"] = df["overall"].astype("int8")
 df["value_eur"] = df["value_eur"].astype("float32")

 #top player by rating,heat map, box plot of top 10 club 
 df["player_positions"]=df["player_positions"].str.split(", ")
 df_exp=df.explode("player_positions")
 df_sorted=df_exp.sort_values(["player_positions","overall"],ascending=[True,False])
 top_5=df_sorted.groupby("player_positions").head(5)
 print(top_5[["player_positions", "short_name", "overall"]])

 corr_mat=df[["age","overall","value_eur","wage_eur","potential","skill_moves"]].corr()

 plt.figure(figsize=(10, 8))
 sns.heatmap(corr_mat, annot=True, cmap='coolwarm', fmt=".2f")
 plt.title('Correlation Heatmap')
 plt.savefig('Correlation Heatmap.png')
 plt.show

 clubv_group=df.groupby("club_name",observed=True)["value_eur"].sum().sort_values(ascending=False)
 clubr_group=df.groupby("club_name",observed=True)["potential"].mean().sort_values(ascending=False)
 print(f"""10 Most valued club:\n{clubv_group.head(10)}\n10 Most player potential club:\n{clubr_group.head(10)}""")
 
 topr_10_clubs = clubr_group.head(10).index
 topr_df=df[df["club_name"].isin (topr_10_clubs)] 
 plt.figure(figsize=(12, 6))
 sns.boxplot(x="club_name", y="potential", data=topr_df)
 plt.xlabel("Club Name")
 plt.ylabel("Potential")
 plt.xticks(rotation=45, ha="right")
 plt.title("10 Most player potential club")
 plt.tight_layout()
 plt.savefig("10 Most player potential club.png")
 plt.show()

 topv_10_clubs = clubv_group.head(10).index
 topv_df=df[df["club_name"].isin (topv_10_clubs)] 
 plt.figure(figsize=(12, 6))
 sns.boxplot(x="club_name", y="value_eur", data=topv_df)
 plt.xlabel("Club Name")
 plt.ylabel("Value")
 plt.xticks(rotation=45, ha="right")
 plt.title("10 Most valued club")
 plt.tight_layout()
 plt.savefig("10 Most valued club.png")
 plt.show()

if __name__ == "__main__":
    main() 
 