# 🚀 Indian Startup Funding Analysis

## 📊 Project Overview
This project analyzes startup funding trends in India using a CSV dataset. It explores yearly startup counts, top-funded industries and cities, sector-wise funding totals, and visualizes investment patterns over time to provide business insights into the Indian startup ecosystem.

## 👤 Author
Krishn Meena

## 📝 Description
The analysis covers:

- Parsing and cleaning date columns to handle dirty or missing data.
- Yearwise startup funding counts.
- Top 10 industries by number of startups funded.
- Top 10 cities by number of startups funded.
- Sector-wise total funding raised (top 10 sectors).
- Yearly funding trends visualized on a logarithmic scale.
- Clear and insightful visualizations using bar and line plots.
- Saving processed summary CSV files and corresponding PNG charts for reproducibility.

## ⭐ Functionalities
1. **Date parsing and cleaning** — robust handling of inconsistent date formats and missing values.
2. **Yearwise startup counts** — total startups funded per year, displayed in a bar chart.
3. **Industry analysis** — ranking the top 10 industries by number of startups funded with visualization.
4. **City analysis** — identifying the top 10 cities with the most startup funding, plotted as a bar chart.
5. **Sector-wise funding totals** — summing funding amounts for top sectors, shown with a horizontal bar chart.
6. **Yearly funding trends** — total funding by year shown with a line plot on a log scale.
7. **Outputs** — saves CSV summary files and PNG charts for all main analyses.

## 📈 Visual Outputs
- Bar charts: Yearwise startup funded, Industry wise startups, Top cities startup funded.
- Horizontal bar chart: Top sectors by funding amount.
- Line plot: Total funding per year on log scale.

## 🛠️ Dependencies
- Python 3.x
- pandas
- matplotlib

Install required packages:
```bash
pip install pandas matplotlib
```

## 🏃 How to Run

1. Place the file `startup_funding.csv` in the same directory as the script.
2. Run the script from the command line:
```bash
python Startup_pandas.py
```

3. The script outputs summary CSV files and PNG images in the working directory.

## 📂 Output Files

- CSV summaries:  
  - group_startup.csv  
  - group_industry.csv  
  - group_cities.csv  
  - group_sector.csv  
  - group_year.csv  

- Chart images:  
  - year wise startup funded.png  
  - Industrywise startup funded.png  
  - Top 10 cities with most startup funded.png  
  - Top 10 sector with most funding value.png  
  - Total Funding Per Year.png  

## 📫 Contact
For questions or feedback, please contact **Krishn Meena**.

---
