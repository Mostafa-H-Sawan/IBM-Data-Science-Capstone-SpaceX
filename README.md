# IBM Data Science Capstone — SpaceX Falcon 9 First-Stage Landing Prediction

Predicting whether the Falcon 9 first stage will land, so the cost of a launch can be estimated
(SpaceX ≈ $62M per launch vs. $165M+ for other providers, mostly thanks to booster reuse).

## Notebooks (run in this order)

| # | File | What it does |
|---|------|--------------|
| 1 | `1_spacex_data_collection_api.ipynb` | Collect launch data from the SpaceX REST API, keep Falcon 9, impute payload mass |
| 2 | `2_spacex_webscraping.ipynb` | Scrape Falcon 9 launch tables from Wikipedia with BeautifulSoup |
| 3 | `3_spacex_data_wrangling.ipynb` | Explore outcomes and build the 0/1 landing label (`Class`) |
| 4 | `4_spacex_eda_sql.ipynb` | 10 SQL tasks on SQLite |
| 5 | `5_spacex_eda_dataviz.ipynb` | EDA charts and one-hot feature engineering |
| 6 | `6_spacex_launch_site_folium.ipynb` | Folium maps: launch sites, outcomes, distances to coast/rail/highway/city |
| 7 | `7_spacex_dash_app.py` | Plotly Dash dashboard (`python 7_spacex_dash_app.py`, needs `spacex_launch_dash.csv`) |
| 8 | `8_spacex_machine_learning_prediction.ipynb` | Logistic Regression, SVM, Decision Tree, KNN with GridSearchCV |

## Key results

- 67% of 90 Falcon 9 launches landed the first stage; 86% in 2019-2020.
- KSC LC-39A has the best landing rate (77%) and 41.7% of all successful landings.
- GTO is the hardest frequent orbit (52% landing rate).
- All tuned models reach 83.3% test accuracy; the Decision Tree is best in 10-fold CV (87.5%).
- Reused cores land 85-89% of the time vs. 27% for first-flight cores.

## Report

`Data Science Capstone Project Report.pdf` — full slide report.

## Tools

Python, pandas, NumPy, requests, BeautifulSoup, SQLite / ipython-sql, matplotlib, seaborn, Folium, Plotly Dash, scikit-learn.
