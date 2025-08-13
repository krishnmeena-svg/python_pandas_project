**Author:** Krishn Meena  

---

## 📌 Description  
This project analyzes **Mall Customer Data** to identify meaningful customer segments based on **income, age, and spending score**.  

It performs:  
- **Statistical profiling** of customers  
- **Segmentation** based on age, income, and spending behavior  
- **K-Means clustering** to discover customer groups  
- **Visualization** of customer demographics and spending habits  

---

## 📂 Features  
1. **Data Cleaning & Preparation**  
   - Remove null values  
   - Rename columns  
   - Scale annual income from k$ to actual $  

2. **Statistical Analysis**  
   - Summary statistics for income and spending score  
   - Distribution of customers by **age range** and **spending level**  

3. **Customer Grouping**  
   - Age groups: Teen, Adult, Senior  
   - Income groups: Low to High  
   - Spender type: Saver or Spender  

4. **Visualizations** (PNG output files)  
   - Box plot: Income by Age Group  
   - Box plot: Spending Score by Income Group  
   - Scatter plot: Income vs. Spending Score  
   - K-Means Clustering plot with centroids  

---

## 📊 Sample Outputs  

**1️⃣ Income by Age Group**  
![Income by Age Group](income%20by%20Age%20group.png)  

**2️⃣ K-Means Clustering**  
![K-Means Clustering](K-Means%20Clustering%20of%20Customers.png)  

---

## 📜 Output Files  
| File Name | Description |
|-----------|-------------|
| `income by Age group.png` | Box plot of income vs. age group |
| `spending score by income group.png` | Box plot of spending score vs. income group |
| `scatter plot of income and spending.png` | Scatter plot with age range as hue |
| `K-Means Clustering of Customers.png` | K-Means cluster visualization |

---

## 🛠 Requirements  
- Python 3.x  
- Pandas  
- Matplotlib  
- Seaborn  
- Scikit-learn  

Install dependencies:  
```bash
pip install pandas matplotlib seaborn scikit-learn
```
## 🚀 Getting Started
1.**Clone the repository**
```bash
git clone https://github.com/krishnmeena-svg/Mall_Customers.git
```
2.**Place the dataset** in the project folder
```bash
Mall_Customers.csv
```
3.**Run** the script
```bash
python mall_customer_pandas.py
```
4.**View outputs in the same folder (PNG charts)**

## 📜 License
This project is licensed under the MIT License — you can freely use, modify, and share it.
