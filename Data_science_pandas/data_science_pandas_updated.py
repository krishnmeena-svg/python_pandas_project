def main():
 """
 📊 Project: Data Scientist Job Market Analysis
 🧑‍💻 Author: Krishn Meena

🔍 Description:
 This project analyzes a dataset of Data Scientist job listings to uncover market trends, salary insights, and in-demand skills.
 It performs extensive data cleaning, feature engineering, and visualizations to draw insights helpful for both job seekers and employers.

🎯 Key Functionalities:
 1. Clean salary data and extract min, max, and average salary.
 2. Identify top 10:
   - Paying Locations
   - Companies
   - Industries
   - Job Titles
 3. Analyze salary by:
   - Company ownership type
   - Company size
   - Industry
   - Rating
   - Company age
 4. Compare job location with headquarters.
 5. Count easy apply jobs and industry-wise trends.
 6. Generate:
   - Word Cloud of job descriptions
   - Skill frequency analysis (Python, SQL, ML, Power BI, Tableau)

 📈 Visual Outputs:
 - Boxplot: Salary by Industry
 - Bar/Reg Plots: Salary vs Rating, Size, Company Age
 - Pie Charts: Industry Size, Easy Apply Jobs
- Word Cloud: Common job terms
 - Skill bar chart

 📁 Data Input:
 - `DataScientist.csv` (must be in `/content/` directory or update the path)

 📂 Saved Outputs:
 - CSV files: `best_location.csv`, `best_Company.csv`, etc.
 - Images: `Boxplot of Average Salaries.png`, `wordcloud.png`, etc.

 📦 Dependencies:
 - pandas
 - numpy
 - matplotlib
 - seaborn
 - wordcloud
 - re

 ▶️ How to Run:
 Ensure all dependencies are installed and run:
    python job_analysis.py
 """
 import pandas as pd
 import matplotlib.pyplot as plt
 import seaborn as sns
 import numpy as np
 import re
 from wordcloud import WordCloud, STOPWORDS
 from pathlib import Path

 file_path = Path('DataScientist.csv')
 df=pd.read_csv(file_path)
 df.replace([-1,"-1"],np.nan,inplace=True)
 df["Company Name"]=df["Company Name"].str.split("\n").str[0]
 df[["Min. Salary","Max. Salary"]]=df["Salary Estimate"].str.extract(r'\$(\d+)K-\$(\d+)K')
 df[["Min. Salary","Max. Salary"]]=df[["Min. Salary","Max. Salary"]].astype(float) * 1000

 df["Avg.salary"]=(df["Min. Salary"]+df["Max. Salary"])/2    #Avg. Salary column creation

 #best 10 location,industry and company(salarywise) -
 best_location=df.groupby("Location")["Avg.salary"].mean().sort_values(ascending=False).head(10)
 best_location.to_csv("best_location.csv")
 best_Company=df.groupby("Company Name")["Avg.salary"].mean().sort_values(ascending=False).head(10)
 best_Company.to_csv("best_Company.csv")
 best_industry=df.groupby("Industry")["Avg.salary"].mean()
 best_10_industry=best_industry.sort_values(ascending=False).head(10)
 best_10_industry.to_csv("best_10_industry.csv")
 best_job=df.groupby("Job Title")["Avg.salary"].mean().sort_values(ascending=False).head(10)
 best_job.to_csv("best_job.csv")
 print(best_location,best_Company,best_10_industry,best_job)

 ownership_salary=df.groupby("Type of ownership")["Avg.salary"].mean().sort_values(ascending=False)
 print("\nAverage Salary ownershipwise")
 print(ownership_salary)

 plt.figure(figsize=(12, 8))
 sns.boxplot(x="Industry", y="Avg.salary", data=df)
 plt.xticks(rotation=90)
 plt.title("Boxplot of Average Salaries per Industry")
 plt.tight_layout()
 plt.show()
 plt.savefig("Boxplot of Average Salaries per Industry.png")

 #size wise top company
 df[["Min.Size","Max.Size"]]=df["Size"].str.extract(r'(\d+)[+ ]*(?:to)?\s*(\d+)?')
 df[["Min.Size","Max.Size"]]=df[["Min.Size","Max.Size"]].astype(float)
 df.fillna({"Max.Size": df["Min.Size"]}, inplace=True)
 df["Avg.Size"]=(df["Min.Size"] + df["Max.Size"]) / 2   #creation of avg.size column

 best_job_company=df.groupby("Company Name")["Avg.Size"].mean()
 print(best_job_company.sort_values(ascending=False).head(10))

 #regression plot for salary vs rating
 plt.figure(figsize=(8, 6))

 sns.regplot(x='Rating', y='Avg.salary', data=df, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})

 plt.title('Company Rating vs. Average Salary')
 plt.xlabel('Company Rating')
 plt.ylabel('Average Salary')
 plt.grid(True)
 plt.tight_layout()
 plt.show()
 plt.savefig("Company Rating vs. Average Salary.png")

 #histogram of rating of companies
 plt.figure(figsize=(8, 5))
 plt.hist(df['Rating'], bins=50, color='blue', edgecolor='black')
 plt.title('Distribution of Rating')
 plt.xlabel('Rating')
 plt.ylabel('Number of Company')
 plt.grid(True)
 plt.show()
 plt.savefig("Distribution of Rating.png")
 plt.tight_layout()

 #comaparison of job city vs HQ
 df["samecity"]=df["Headquarters"]==df["Location"]
 location_com=df['samecity'].value_counts()
 location_com.plot(kind='bar',color='black')
 plt.title('Job Location vs Number of Jobs')
 plt.xlabel('Job Location')
 plt.ylabel('Number of Jobs')
 plt.xticks(ticks=[0,1], labels=['Different From HQ', 'Same as HQ'], rotation=0)
 plt.grid(True)
 plt.tight_layout()
 plt.show()
 plt.savefig("Job Location vs Number of Jobs.png")

 #industry and sector trend
 big_industry=df.groupby("Industry")["Avg.Size"].mean().sort_values(ascending=False)
 top10big_industry=big_industry.sort_values(ascending=False).head(10)
 top10big_sector=df.groupby("Sector")["Avg.Size"].mean().sort_values(ascending=False).head(10)
 avg_size=round(big_industry.mean(),2)
 print(f"Average size across industry:{avg_size}")
 print(top10big_industry,top10big_sector)

 plt.figure(figsize=(16,16))
 big_industry.plot.pie(
    labels=None,
    autopct=None,
    startangle=90,
    legend=False
  )
 percentages = big_industry / big_industry.sum() * 100
 custom_labels = [f"{industry}: {pct:.2f}%" for industry, pct in zip(big_industry.index, percentages)]
 # Manually add and position the legend
 plt.legend(
    labels=custom_labels,
    title="Industry",
    loc="best",
    bbox_to_anchor=(1,1),
    ncol=3,                      
    fontsize='small'
     )
 plt.ylabel('')
 plt.title('industry size')
 plt.tight_layout()
 plt.show()
 plt.savefig("industry size.png")

 #Experiance and companty size
 df["Company age"]=2025-df["Founded"]

 plt.figure(figsize=(8, 6))
 sns.regplot(x='Company age', y='Avg.salary', data=df, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
 plt.title('Company age vs Average Salary')
 plt.xlabel('Company age')
 plt.ylabel('Average Salary')
 plt.grid(True)
 plt.tight_layout()
 plt.show()
 plt.savefig("Company age vs Average Salary.png")

 size_salary=df.groupby("Avg.Size")["Avg.salary"].mean()
 size_salary.plot.bar(
    figsize=(8,5),
    color='skyblue',
    edgecolor='black',
    title="avg.size vs avg.salary"
  )

 plt.xlabel("avg. size")
 plt.ylabel("avg. salary")
 plt.xticks(rotation=0) 
 plt.tight_layout()
 plt.show()
 plt.savefig("avg. size vs avg. salary.png")

 #easy apply jobs count
 easy_count=df["Easy Apply"].value_counts()
 print (f"Easily Availavle jobs: {easy_count}")
 group_easy=df.groupby("Industry")["Easy Apply"].value_counts().sort_values(ascending=False)

 plt.figure(figsize=(16,16))
 group_easy.plot.pie(
    labels=None,
    autopct=None,
    startangle=90,
    legend=False
  )
 percentages =  group_easy /  group_easy.sum() * 100
 custom_labels = [f"{industry}: {pct:.2f}%" for industry, pct in zip( group_easy.index, percentages)]
 # Manually add and position the legend
 plt.legend(
    labels=custom_labels,
    title="Industry",
    loc="best",
    bbox_to_anchor=(1,0.7),
    ncol=3,                      
    fontsize='small'
     )
 plt.ylabel('')
 plt.title('easy apply job in industary')
 plt.tight_layout()
 plt.show()
 plt.savefig("Easy job industrywise.png") 

 #most require skill count
 df["Job Description"]=df["Job Description"].astype(str).str.replace(r'[!?,.;:]', '', regex=True).str.lower().str.strip().str.split()
 word_freq={}
 for word in df["Job Description"]:
   for i in word:
      if i in word_freq:
        word_freq[i]+=1
      else:
        word_freq[i]=1
 sorted_word=sorted(word_freq.items(),key=lambda x:x[1],reverse=True)
 for i,j in sorted_word[:5]:
    print(f"{i}:{j}")

 all_words = ' '.join(df["Job Description"].sum())
 custom_stops = { 'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any',
  'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between',
  'both', 'but', 'by', 'can', 'did', 'do', 'does', 'doing', 'down', 'during', 'each',
  'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
  'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is',
  'it', 'its', 'itself', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'of',
  'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out',
  'over', 'own', 'same', 'she', 'should', 'so', 'some', 'such', 'than', 'that', 'the',
  'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this',
  'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were',
  'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with',
  'you', 'your', 'yours', 'yourself', 'yourselves', 'job', 'role', 'position', 'team', 'project', 'tasks', 'work', 'working',
  'environment', 'business', 'organization', 'company', 'job', 'office',
  'candidate', 'person', 'individual', 'opportunity', 'requirements',
  'responsibilities', 'skills', 'abilities', 'experience', 'knowledge',
  'background', 'years', 'preferred', 'required', 'excellent', 'strong',
  'understanding', 'proficiency', 'demonstrated', 'ability', 'willingness',
  'communication', 'verbal', 'written', 'interpersonal', 'develop', 'design', 'build', 'create', 'implement', 'maintain', 'support',
  'use', 'using', 'manage', 'lead', 'coordinate', 'analyze', 'provide', 'ensure',
  'assist', 'drive', 'help', 'monitor', 'perform', 'deliver', 'report', 'run',
  'test', 'evaluate', 'plan', 'organize', 'execute', 'identify','etc', 'etc.', 'including', 'among', 'based', 'across', 'within',
  'must', 'should', 'would', 'may', 'could', 'can', 'need', 'looking',
  'highly', 'well', 'best', 'great', 'new', 'future', 'fast', 'paced',
  'dynamic', 'self', 'motivated', 'driven', 'growth', 'collaborative',
  'passionate', 'curious', 'detail', 'oriented'}
 stops = STOPWORDS.union(custom_stops)
 wc = WordCloud(width=1000, height=500,
               background_color="white",
               stopwords=stops,
               colormap="Accent").generate(all_words)

 plt.figure(figsize=(12, 6))
 plt.imshow(wc, interpolation="bilinear")
 plt.axis("off")
 plt.tight_layout()
 plt.show()
 plt.savefig("wordcloud.png")

 skill_patterns = {
    "python"          : r"\bpython\b",
    "sql"             : r"\bsql\b",
    "machine learning": r"\bmachine\s+learning\b",
    "tableau / power bi": r"\b(tableau|power\s*bi)\b"
 }
 skill_counts = {
    i: len(re.findall(j, all_words, flags=re.I))
    for i,j in skill_patterns.items()
 }
 skill_counts = pd.Series(skill_counts).sort_values(ascending=False)
 plt.figure(figsize=(8,5))
 sns.barplot(x=skill_counts.index,
            y=skill_counts.values)

 plt.title("Number of Job Ads Mentioning Each Skill")
 plt.ylabel("Job‑count")
 plt.xlabel("Skill")
 plt.xticks(rotation=0)
 plt.tight_layout()
 plt.show()
 plt.savefig("Number of Job Ads Mentioning Each Skill.png")

if __name__ == "__main__":
    main()







