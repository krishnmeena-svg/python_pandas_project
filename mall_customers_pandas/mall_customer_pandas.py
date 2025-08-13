def main():
 """
    📊 Project: Mall Customer Segmentation
    🧑‍💻 Author: Krishn Meena

    🔍 Description:
    This project analyzes mall customer data to identify patterns based on income, age, and spending score. 
    It performs statistical profiling, customer segmentation, and visualizes relationships using box plots, 
    scatter plots, and K-means clustering.

    🎯 Functionalities:
    1. Clean and prepare the dataset (drop nulls, rename columns, scale income).
    2. Perform statistical analysis on income and spending score.
    3. Create demographic segments:
       - Age range bins
       - Spending levels
       - Custom customer groups (e.g., spender type, income group)
    4. Visualize:
       - Box plots (income by age, spending by income group)
       - Scatter plots (income vs. spending)
       - K-Means clustering visualization

    📂 Outputs:
    - PNG Charts:
        - 'income by Age group.png'
        - 'spending score by income group.png'
        - 'scatter plot of income and spanding.png'
        - 'K‑Means Clustering of Customers.png'

    📦 Dependencies:
    - pandas
    - matplotlib
    - seaborn
    - scikit-learn

    ▶️ How to Run:
    Ensure 'Mall_Customers.csv' is in the same directory and run:
        python mall_segmentation.py
    """
 import pandas as pd
 import matplotlib.pyplot as plt
 import seaborn as sns
 from sklearn.cluster import KMeans
 from pathlib import Path

 file_path = Path("Mall_Customers.csv")
 df=pd.read_csv(file_path)
 df=df.dropna()
 df=df.rename(columns={"Annual Income (k$)":"income"})
 df["income"]=df["income"]*1000

 #1.statical analysis of data
 anyl=df["income"].describe()
 print(f"Income Analysis of Customers:\n{anyl}")
 score=df["Spending Score (1-100)"].describe()
 print(f"Analysis of spending score:\n{score}")
 df["Age range"]=pd.cut(df["Age"],bins=[0,18, 30, 40, 50, 100],labels=["0-18","18–30", "31–40", "41–50", "51+"])
 df["Spending Level"] = pd.qcut(df["Spending Score (1-100)"], q=3, labels=["Low", "Medium", "High"])
 count_age_range=df["Age range"].value_counts()
 count_spending_range=df["Spending Level"].value_counts()
 print(f"count for age range:\n{count_age_range}\ncount for spending level:\n{count_spending_range}")

 #2.creating groups
 df["Age group"]=pd.cut(df["Age"],bins=[0,18, 60, 100],labels=["Teen","Adult", "Senior"])
 df["income group"]=pd.qcut(df["income"],q=4,labels=["low income","low-middle income","high-middle income","high income"])
 df["spender group"]=pd.qcut(df["Spending Score (1-100)"],q=2,labels=["saver","spender"])

 #3.plotting(box and scatter)
 
 sns.boxplot(x="Age group", y="income", data=df)
 plt.title("income by Age group")
 plt.savefig("income by Age group.png")
 plt.show()

 plt.figure(figsize=(12, 8))
 sns.boxplot(x="income group", y="Spending Score (1-100)", data=df)
 plt.title("spending score by income group")
 plt.savefig("spending score by income group.png")
 plt.show()

 plt.figure(figsize=(12, 8))
 sns.scatterplot(data=df,x='income', y='Spending Score (1-100)',hue="Age range")
 plt.title("scatter plot of income and spending")
 plt.savefig("scatter plot of income and spending.png")
 plt.show()

 X = df[["income", "Spending Score (1-100)"]]
 kmeans = KMeans(n_clusters=5, random_state=42)
 df["Cluster"] = kmeans.fit_predict(X)
 plt.figure(figsize=(10, 6))
 sns.scatterplot(
    x="income",
    y="Spending Score (1-100)",
    hue="Cluster",
    palette="Set1",
    data=df,
    s=60)

 centroids = kmeans.cluster_centers_
 plt.scatter(centroids[:, 0], centroids[:, 1],
            c="black", s=100, marker="X", label="Centroids")

 plt.title("K‑Means Clustering of Customers")
 plt.legend()
 plt.savefig('K‑Means Clustering of Customers.png')
 plt.show()
if __name__ == "__main__":
    main()
