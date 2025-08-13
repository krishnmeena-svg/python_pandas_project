# FIFA 21 Career Mode Player Analysis

## Overview

This project provides an exploratory data analysis (EDA) of player statistics from the FIFA 21 Career Mode dataset. It aims to uncover insights about top-performing players by position, club-level valuation and potential comparisons, and correlations among key player attributes.

## Features

- Identification of the top 5 players for each playing position based on overall rating.
- Club-level analysis including:
  - Total player market value rankings.
  - Average player potential ratings by club.
- Correlation heatmap revealing relationships among age, overall rating, value, wage, potential, and skill moves.
- Boxplots showcasing distributions of player potential and market value for the top 10 clubs by each metric.
- Data cleaning and handling of multi-position players.

## Dataset

- Source: FIFA Career Mode Player Dataset covering FIFA versions 15 through 21.

  link-https://www.kaggle.com/datasets/stefanoleone992/fifa-21-complete-player-dataset
- Sheet: Analyzed data is from the FIFA 21 sheet.
- Format: Excel spreadsheet
```bash
pip install pandas seaborn matplotlib openpyxl
```
2. Place the dataset Excel file in the path specified in the script or update the path accordingly.
3. Run the script:
```bash
python FIFA_PANDAS_updated1.py
```
4. The script prints key player and club data to the console and saves visualizations as PNG files:
- `Correlation Heatmap.png`
- `10 Most player potential club.png`
- `10 Most valued club.png`

## Project Structure & Outputs

- The analysis is encapsulated in a `main()` function that:
- Loads and preprocesses data.
- Extracts and sorts top players by position.
- Computes and visualizes player attribute correlations.
- Aggregates club valuations and potentials and visualizes distributions for top clubs.
- Output plots provide graphical insights for deeper understanding and reporting.

## Insights & Use Cases

- Helps analyze player and club performance characteristics within FIFA 21 Career Mode.
- Assists in strategic decision-making regarding player positions and club focus.
- Supports gaming content development or extended statistical exploration of virtual soccer data.

## Author

Krishn Meena  
