# 📊 Data Scientist Job Market Analysis

## 📌 Project Description
This project analyzes a dataset of Data Scientist job listings to uncover market trends, salary insights, and in-demand skills.  
It performs extensive data cleaning, feature engineering, and visualizations to produce actionable insights useful for both job seekers and employers.

**Author:** Krishn Meena

---

## ✨ Key Functionalities
- Clean and process salary data to extract minimum, maximum, and average salaries.
- Identify top 10 entities for:
  - Paying Locations
  - Companies
  - Industries
  - Job Titles
- Analyze salary variation by:
  - Company ownership type
  - Company size
  - Industry
  - Company rating
  - Company age
- Compare job location with company headquarters.
- Count jobs that feature “Easy Apply” option and analyze industry-wise trends.
- Generate visual insights including:
  - Boxplot of Salary by Industry
  - Regression plots of Salary vs Rating, Company Size, and Company Age
  - Pie charts representing Industry Size and Easy Apply jobs distribution
  - Word Cloud displaying most common job description terms
  - Bar chart of skill mentions (Python, SQL, Machine Learning, Tableau/Power BI)

---

## 🛠️ Dependencies
- Python **3.x**
- pandas
- numpy
- matplotlib
- seaborn
- wordcloud
- re (regular expressions module, part of Python’s standard library)

To install the required external libraries, run:
```bash
pip install pandas numpy matplotlib seaborn wordcloud
```
---

## 🚀 How to Run

1. Ensure the dataset `DataScientist.csv` is placed in the same directory as `data_science_pandas_updated.py` (or update the path accordingly).
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the analysis script:
```bash
python data_science_pandas_updated.py
```
4. The script will perform data analysis and generate visualizations, displaying plots inline and saving results and images to the project folder.

---

## 📂 Saved Outputs

- **CSV Files**:
  - `best_location.csv` — Top 10 highest paying locations
  - `best_Company.csv` — Top 10 companies by average salary
  - `best_10_industry.csv` — Top 10 industries by average salary
  - `best_job.csv` — Top 10 job titles by average salary

- **Images (plots)**:
  - `Boxplot of Average Salaries per Industry.png`
  - `Company Rating vs. Average Salary.png`
  - `Distribution of Rating.png`
  - `Job Location vs Number of Jobs.png`
  - `industry size.png`
  - `Company age vs Average Salary.png`
  - `avg. size vs avg. salary.png`
  - `Easy job industrywise.png`
  - `wordcloud.png`
  - `Number of Job Ads Mentioning Each Skill.png`

---

## 📊 Example Console Outputs
```text
Location          Avg.salary
New York,NY       120000
San Francisco,CA  115000
...

Company Name      Avg.salary
Google            135000
Facebook          130000
...

Top skill counts:
python: 2300
sql: 1800
machine learning: 1400
tableau / power bi: 900
```
---

## 💡 Notes on the Analysis
- The project uses string processing, regex extraction, and grouping with Pandas.
- Visualizations with Matplotlib and Seaborn aid in understanding distributions and relationships.
- WordCloud helps identify common job description terms, excluding generic stopwords and business-related filler words.
- Skill frequency is determined via regex matching in job descriptions.

---

## 📄 License
This project is free to use for learning and educational purposes.  
You are welcome to modify and share it.

---

## 🤝 Contributing
Pull requests, suggestions, and bug reports are welcome.  
Please open an issue on GitHub if you would like to suggest improvements.

---

