def main():
 """
    📊 Project: Netflix Titles Data Analysis
    🧑‍💻 Author: Krishn Meena

    🔍 Description:
    This project analyzes the Netflix Titles dataset to uncover trends in content types, genres,
    geographic distribution, and textual summaries over time. The dataset includes metadata for
    movies and TV shows available on Netflix.

    🎯 Functionalities:
    1. Cleans the dataset (removes nulls, parses dates, splits genres and countries).
    2. Analyzes yearly trends in shows vs. movies added.
    3. Identifies the most common genres using bar charts.
    4. Generates a word cloud from the content descriptions.
    5. Explores country-wise content distribution and visualizes it with a pie chart.

    📂 Outputs:
    - CSVs: 'genre_wise.csv', 'country_type.csv'
    - Charts:
        - 'Number of Shows vs Movies Added per Year.png'
        - 'genre vs type count.png'
        - 'wordcloud.png'
        - 'type by country.png'

    📦 Dependencies:
    - pandas
    - matplotlib
    - seaborn
    - wordcloud

    ▶️ How to Run:
    Make sure 'netflix_titles.csv' is present in the correct path and run:
        python netflix_analysis.py 
"""
 import pandas as pd
 import matplotlib.pyplot as plt
 import seaborn as sns
 from wordcloud import WordCloud, STOPWORDS
 from pathlib import Path

 file_path = Path('netflix_titles.csv')
 df=pd.read_csv(file_path)
 df=df.dropna()
 #datetime and bar plot of year wise movie/show type
 df["date_added"] = pd.to_datetime(df["date_added"],errors="coerce")
 df["month"]=df["date_added"].dt.month
 df["year"]=df['date_added'].dt.year
 year_type_counts = df.groupby(["year", "type"]).size().reset_index(name='count')
 plt.figure(figsize=(12,6))
 sns.lineplot(data=year_type_counts,x="year", y="count", hue="type", marker="o")
 plt.title("Number of Shows vs Movies Added per Year")
 plt.ylabel("Count")
 plt.xlabel("Year")
 plt.grid(True)
 plt.tight_layout()
 plt.savefig("Number of Shows vs Movies Added per Year.png")
 plt.show()

 #genre split,flatten and bar chart of most common genre
 df["listed_in"]=df["listed_in"].str.split(", ")
 df_exploded = df.explode('listed_in')
 word_freq={}
 for i in df_exploded["listed_in"]:
      if i in word_freq:
        word_freq[i]+=1
      else:
        word_freq[i]=1
 sorted_word=sorted(word_freq.items(),key=lambda x:x[1],reverse=True)
 for i,j in sorted_word[:10]:
    print(f"{i}:{j}")

 genre_wise=df_exploded.groupby("listed_in")["type"].value_counts()
 genre_wise.to_csv("genre_wise.csv")
 genre_wise.sort_values(ascending=False).plot.bar(
    figsize=(16,16),
    color='skyblue',
    edgecolor='black',
    title="genre vs type count"
 )

 plt.xlabel("genere")
 plt.ylabel("type count")
 plt.xticks(rotation=45, ha='right')  
 plt.tight_layout()
 plt.savefig("genre vs type count.png")
 plt.show()

 #description world cloud
 df["description"]=df["description"].astype(str).str.replace(r'[!?,.;:]', '', regex=True).str.lower().str.strip().str.split()
 word_freq={}
 for word in df["description"]:
   for i in word:
      if i in word_freq:
        word_freq[i]+=1
      else:
        word_freq[i]=1
 sorted_word=sorted(word_freq.items(),key=lambda x:x[1],reverse=True)
 for i,j in sorted_word[:5]:
    print(f"{i}:{j}")
 all_words = ' '.join(df["description"].sum())
 custom_stops = {"a", "an", "the", "and", "or", "but", "if", "in", "on", "at", "of", "to", "for", "by", "with", "from", "as", "is", "was", "are", "were","be", "been", "being", "can", "could", "should", "would", "shall", "will", "may", "might", "must", "do", "does", "did", "doing", "has", "have", "had","this", "that", "these", "those", "such", "all", "any", "each", "every", "some", "no", "not", "nor", "i", "me", "my", "we", "us", "our", "you", "your", "he", "him", "his", "she", "her", "they", "them", "their", "it", "its", "one","etc", "etc.", "also", "more", "most", "very", "just", "much", "many", "like", "so", "up", "out", "about", "again", "only", "new", "used", "use", "using", "within","job", "role", "position", "experience", "skills", "required", "preferred", "responsibilities", "requirements", "responsibility", "ability", "work", "team", "environment", "candidate", "applicant", "description", "overview", "detail", "knowledge", "understanding", "strong", "good", "well", "must", "will", "need", "looking", "join", "opportunity", "company", "organization", "apply", "year", "years", "per", "cent", "based",
}

 stops = STOPWORDS.union(custom_stops)
 wc = WordCloud(width=1000, height=500,
               background_color="white",
               stopwords=stops,
               colormap="Accent").generate(all_words)

 plt.figure(figsize=(12, 6))
 plt.imshow(wc, interpolation="bilinear")
 plt.axis("off")
 plt.tight_layout()
 plt.savefig("wordcloud.png")
 plt.show()


 #top 10 type countrywise and pie chart of them
 df["country"]=df["country"].str.split(", ")
 df_coun_exploded = df.explode('country')
 country_type=df_coun_exploded.groupby("country")["type"].value_counts()
 country_type.to_csv("country_type.csv")
 print(country_type.sort_values(ascending=False).head(10))

 plt.figure(figsize=(12,12))      # make it square
 country_type.sort_values(ascending=False).head(5).plot.pie(
    autopct='%1.1f%%',         # show percentages
    startangle=90,             # rotate so first slice starts at 12 o'clock
    legend=False               # turn off the legend (labels will be on slices)
    )

 plt.ylabel('')
 plt.title('type by country')     # add a title
 plt.tight_layout()             # better spacing
 plt.savefig('type by country.png')
 plt.show()

if __name__ == "__main__":
    main()







