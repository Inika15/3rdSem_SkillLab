# Applied Data Science Mini-Project Proposal
## Walmart Store Sales Econometric Intelligence & Demand Forecasting

**Academic Year:** 2026–2027  
**Course:** Applied Data Science Skill Lab (3rd Semester)  
**Project Domain:** Retail Analytics, Econometrics & Predictive Supply-Chain Intelligence  
**Dataset:** Walmart Store Sales (45 Stores × 143 Weeks, 6,435 Records)  

---

## 1. Executive Summary & Problem Formulation
In high-volume retail enterprises, supply chain equilibrium depends on the accuracy of weekly store demand forecasts. An inaccurate forecast carries asymmetrical operational penalties:
- **Over-forecasting** induces unnecessary working capital lockup, elevated warehouse holding expenses, and inventory shrink/perishable spoilage.
- **Under-forecasting** leads directly to stock-outs during critical shopping windows, lost revenue, customer disaffection, and brand erosion.

This project investigates the multi-store sales trajectories of 45 Walmart US locations across 143 consecutive weeks (February 2010 to October 2012). We formulate both a continuous sales forecasting regression problem and a binary peak-demand classification alert system to solve real-world retail inventory allocation challenges.

---

## 2. Dataset Description & Acquisition Plan
The dataset is drawn from the historical Walmart store sales records (Kaggle Retail Benchmark). It represents a balanced panel of 45 stores observed across 143 calendar weeks ($45 \times 143 = 6,435$ observations).

| Attribute | Data Type | Role | Description & Physical Units |
|---|---|---|---|
| `Store` | Integer | Categorical Identifier | Unique store location ID (1 to 45) |
| `Date` | Datetime | Temporal Index | Week-ending reporting date (`DD-MM-YYYY`) |
| `Weekly_Sales` | Continuous Numeric | Primary Target (Regression) | Total sales turnover for that store-week (US Dollars) |
| `Holiday_Flag` | Binary (0 / 1) | Indicator | 1 = Statutory federal holiday week; 0 = Normal week |
| `Temperature` | Continuous Numeric | Macro Feature | Average regional temperature (°F) |
| `Fuel_Price` | Continuous Numeric | Macro Feature | Regional automotive fuel price per gallon (US$) |
| `CPI` | Continuous Numeric | Macro Feature | Consumer Price Index (purchasing power metric) |
| `Unemployment` | Continuous Numeric | Macro Feature | Prevailing local unemployment rate (%) |

---

## 3. Core Objectives & Research Hypotheses
1. **Hypothesis 1 (Macro Inelasticity):** Due to Walmart’s core merchandise mix in price-inelastic non-discretionary consumer staples and groceries, regional macroeconomic shifts (CPI, Fuel Price, Unemployment) explain less than 5% of weekly sales variance.
2. **Hypothesis 2 (Annual Seasonality Dominance):** Weekly sales are overwhelmingly anchored by 52-week annual periodicity (`lag_52`), such that sales in week $t$ of year $y$ are strongly correlated with sales in week $t$ of year $y-1$.
3. **Hypothesis 3 (Outlier Preservation Integrity):** Extreme upper sales outliers detected via the 1.5×IQR boundary represent authentic holiday shopping spikes (Thanksgiving/Black Friday, pre-Christmas) rather than data capture errors. Deleting them impairs holiday inventory forecasting.
4. **Hypothesis 4 (Predictive Superiority):** An ensemble tree-based regressor (Random Forest) incorporating domain-specific temporal lags and store categorical encodings will surpass traditional parametric OLS regression and naive historical heuristics, achieving a MAPE under 7.0%.
5. **Hypothesis 5 (Demand Classification):** A classification pipeline can predict peak demand surge weeks (>75th percentile sales) with an accuracy exceeding 90% and ROC-AUC over 0.95.

---

## 4. Methodological Framework: The Six Stages
The project strictly implements the standardized Six-Stage Applied Data Science Lifecycle:

```
[Stage 1: Problem Identification]
       │
       ▼
[Stage 2: Data Acquisition & Validation]
       │
       ▼
[Stage 3: Data Preparation & Integrity Auditing]
  ├─ Type Casting & Datetime Normalization
  ├─ Missing & Duplicate Auditing (0 missing, 0 duplicate)
  ├─ Outlier Auditing (IQR "Investigate, Do Not Delete" policy)
  └─ Feature Engineering (Lags: lag_1, lag_52; Rolling Window: roll_mean_4; Target: High_Demand_Flag)
       │
       ▼
[Stage 4: Exploratory Data Analysis (EDA)]
  ├─ Parametric & Non-Parametric Descriptive Statistics
  ├─ Frequency Distribution Tables & Skewness Analysis
  └─ Store-Level Heterogeneity Auditing (CV, Ranking)
       │
       ▼
[Stage 5: Visualization & Predictive Modelling]
  ├─ 13 Publication-Grade Visualizations (Bar, Line, Box, Scatter, Heatmap, Diagnostics)
  ├─ Regression Modeling (OLS Linear Regression, Ridge, Random Forest Regressor, Naive Baselines)
  ├─ Classification Modeling (Logistic Regression, Random Forest Classifier)
  └─ Model Evaluation (MAE, RMSE, R², MAPE, Confusion Matrix, ROC-AUC)
       │
       ▼
[Stage 6: Interpretation, Limitations & Executive Recommendations]
```

---

## 5. Technology Stack & Environment
- **Core Language:** Python 3.13+
- **Data Manipulation & Computation:** Pandas, NumPy, SciPy
- **Statistical Modeling & Machine Learning:** Scikit-Learn (`sklearn.pipeline`, `sklearn.compose`, `sklearn.ensemble`, `sklearn.metrics`)
- **Visualizations:** Matplotlib, Seaborn
- **Environment & Notebook Execution:** Jupyter Notebook (`nbclient`, `nbformat`, `jupyter`)
- **Interactive Demonstrations:** Modern responsive HTML/CSS/JS Canvas studio, Streamlit (`app.py`), and Python REST Server (`server.py`)

---

## 6. Expected Deliverables
1. **Original & Cleaned Datasets:** `Walmart.csv`, `outputs/walmart_cleaned.csv`, `outputs/walmart_features.csv`.
2. **Standardized Jupyter Notebook:** `Walmart_EDA.ipynb` (clean execution, rich output tables, embedded charts, zero errors).
3. **Data Cleaning Pipeline Notebook:** `walmart_cleaning_pipeline.ipynb`.
4. **Visualization Outputs:** 13 high-resolution plots saved in `outputs/figures/`.
5. **Model Evaluation Outputs:** `outputs/model_metrics.csv`, `outputs/classification_metrics.csv`, and `outputs/test_predictions.csv`.
6. **Project Proposal:** `PROJECT_PROPOSAL.md`.
7. **Comprehensive Technical Report:** `TECHNICAL_REPORT.md`.
8. **Presentation & Viva Defense Guide:** `VIVA_PREPARATION_GUIDE.md`.

---

## 7. Project Work Breakdown Structure & Timeline

| Phase / Sprint | Key Tasks | Expected Deliverable |
|---|---|---|
| **Sprint 1: Initiation & Ingestion** | Problem definition, dataset ingestion, structural auditing, schema validation | Stage 1 & 2 documentation, raw data inspection |
| **Sprint 2: Data Preparation** | Missing value check, duplicate auditing, IQR outlier investigation, lag and rolling feature engineering | Cleaned datasets (`walmart_cleaned.csv`), feature tables |
| **Sprint 3: Exploratory Data Analysis** | Summary statistics, skewness, frequency tables, store variance analysis | Descriptive statistics and frequency distribution tables |
| **Sprint 4: Visual Analytics** | Bar charts, line time series, box plots, scatter plots with regression lines, correlation heatmaps | 8 EDA figures in `outputs/figures/` |
| **Sprint 5: Predictive Modeling** | Chronological 80/20 train-test split, OLS, Ridge, Random Forest regression, classification, confusion matrix, ROC curve | Models (`model_rf.pkl`, `model_lin.pkl`), evaluation leaderboards |
| **Sprint 6: Synthesis & Presentation** | Viva preparation guide, project proposal, technical report, standalone web studio verification | Complete project documentation bundle |

---
*Submitted for evaluation under the RVCE Applied Data Science Skill Lab.*
