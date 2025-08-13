# 📊 COVID Trends Visualizer

## 📌 Project Description
Analyze and visualize global COVID-19 trends using a cleaned country-level dataset.  
This tool calculates key statistics (cases, deaths, recoveries), identifies top-affected countries, shows region-based summaries, and produces polished data visualizations.

**Author:** Krishn Meena

---

## ✨ Features
- Cleans and standardizes the COVID-19 dataset for analysis.
- Calculates global totals for confirmed cases, deaths, and recoveries.
- Ranks countries by:
  - Total deaths
  - Total confirmed cases
  - 1-week % increase in cases
- Saves summary CSV files:
  - `top5_death.csv`
  - `top5_Confirmed.csv`
  - `top5_weekly.csv`
  - `regional_total.csv`
- Visualizes:
  - Top 5 confirmed cases (line chart)
  - Pie charts showing deaths and confirmed cases by WHO region
- Computes and prints global fatality and recovery rates.

---

## 🛠️ Requirements
- Python **3.x**
- pandas
- matplotlib

Recommend:  
```bash
pip install pandas matplotlib
```
---

## 🚀 How to Run

1. Place `country_wise_latest.csv` in the same directory as `updatesmain.py`.
2. Open a terminal or command prompt in the project directory.
3. Run:
```bash
python updatesmain.py
```

---

## 📂 Example Outputs

- **CSV Files**:  
- `top5_death.csv`: Top 5 countries by death count
- `top5_Confirmed.csv`: Top 5 countries by confirmed cases
- `top5_weekly.csv`: Top 5 countries by 1-week % increase
- `regional_total.csv`: Regional case/death totals

- **Charts** (auto-saved):
- `country vs confirmed cases.png`: Line chart
- `Region wise death.png`: Pie chart of deaths
- `Region wise confirmed.png`: Pie chart of confirmed cases

- **Console Output**:
```text
Top 5 Country, deathwise-
Rank Country Deaths
0 1 CountryA 38000
1 2 CountryB 27000
...

Global Fatality rate: 2.1%
Recovery rate: 83.7%
```



---

## 📄 License
This project is available for learning and educational use.  
Feel free to modify and share.

---

## 🤝 Contributing
Pull requests and improvements are welcome.  
If you spot a bug or want to suggest a new feature, please open an issue.


