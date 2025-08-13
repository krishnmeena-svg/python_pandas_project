# 🏏 IPL Stats Analyzer

**Author:** Krishn Meena  

## 📌 Description  
This project analyzes an **IPL cricket dataset** using **Pandas** and **Matplotlib** to generate useful insights and visualizations.  
It processes the dataset to find:  
- Total matches played by each team  
- Total runs scored by each team  
- Top 10 highest run-scorers  
- Top 10 highest wicket-takers  
- Distribution of players by country (Pie Chart)  

---

## 📂 Features  
1. **Total Runs by Each Team**  
   - Calculates and exports a CSV file: `teams_runs.csv`  

2. **Top 10 Run-Getters**  
   - Finds top players based on runs scored  
   - Exports results to `top10_runs.csv`  

3. **Top 10 Wicket-Takers**  
   - Finds bowlers with the most wickets  
   - Exports results to `top10_bowler.csv`  

4. **Players by Country (Pie Chart)**  
   - Creates a `country_distribution.png` pie chart  
   - Shows percentage of players from each country  

---

## 📊 Output Files  
| File Name | Description |
|-----------|-------------|
| `teams_runs.csv` | Total runs scored by each team |
| `top10_runs.csv` | Top 10 players by runs |
| `top10_bowler.csv` | Top 10 players by wickets |
| `country_distribution.png` | Pie chart of players by country |

---

## 🛠 Requirements  
- Python 3.x  
- Pandas  
- Matplotlib  

Install dependencies:  
```bash
pip install pandas matplotlib
```
## 🚀 Getting Started
1. **Clone the repository**
 ```bash
git clone https://github.com/krishnmeena-svg/IPL_dataset_final.git
```
2. **Place your dataset files in the project folder**
```text
IPL_dataset_final.csv
```

3.**Run the script**
```bash
python updatesmain.py
```
4.**Check the outputs in the project folder**
## 📜 License
This project is licensed under the MIT License — you can freely use, modify, and share it.
