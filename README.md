# Walmart Store Sales — Econometric Intelligence & Forecasting Studio
**RVCE Applied Data Science Skill Lab — Mini-Project**

An executive retail analytics command center and predictive forecasting suite built on 143 weeks of historical sales across 45 Walmart US Supercenters (2010–2012; 6,435 records).

---

## 🚀 Quick Launch (How to Run for Demonstration)

### Option 1: Standalone Executive Web Studio (Recommended — Zero Installation)
Double-click [`run_app.bat`](file:///d:/Projects/3rdSem_SkillLab/run_app.bat) and choose `[1]`, or simply double-click [`index.html`](file:///d:/Projects/3rdSem_SkillLab/index.html).
- Runs instantly in Chrome, Edge, or Firefox.
- **100% Offline-capable**: Zero server, zero npm, zero Python environment dependency needed at presentation time.
- High-DPI interactive SVG time-series, store explorer, correlation analyzer, what-if live simulation sandbox, and Viva Defense slide deck.

### Option 2: Python Streamlit Interactive Dashboard
Double-click [`run_app.bat`](file:///d:/Projects/3rdSem_SkillLab/run_app.bat) and choose `[2]`, or run:
```bash
streamlit run app.py
```
- Interactive Plotly figures, live model inference querying `outputs/model_rf.pkl`, and store deep-dives.

### Option 3: Python REST Backend Server
Double-click [`run_app.bat`](file:///d:/Projects/3rdSem_SkillLab/run_app.bat) and choose `[3]`, or run:
```bash
python server.py
```
- Serves the executive studio at `http://localhost:8000` with live `/api/predict` REST inference endpoints.

---

## 📊 Key Findings & Empirical Discoveries

1. **Store Footprint & Volume Disparity:**
   - 45 stores span a **7.8× disparity** in weekly sales volume (Store #2 averages \$2.66M/week vs Store #43 at \$342k/week), reflecting store formats (Flagship Megastore vs Compact Regional Market).
2. **The Outlier Policy ("Investigate, Do Not Delete"):**
   - Applying IQR flags 127 weeks (1.97%). All 127 points occur in large stores during Thanksgiving (Black Friday) and Christmas surges. In retail supply chains, deleting peak demand creates severe stock-outs; authentic holiday demand was preserved for modeling integrity.
3. **The Macro Factor Reality:**
   - External economic indicators (CPI, Fuel Price, Unemployment, Temperature) explain <1% of weekly sales variation. Retail groceries and household staples are price-inelastic essentials.
4. **The "Christmas Week" Calendar Anomaly:**
   - The statutory holiday flag (`Holiday_Flag = 1`) falls on Dec 30/31 (post-Christmas), while the **unflagged pre-Christmas week** (Dec 23/24) has the true peak at **1.65× baseline** (> \$1.79M per store).

---

## 🏆 Predictive Modeling Leaderboard

Evaluated strictly on **855 unseen future store-weeks** (chronological split at June 22, 2012):

### A. Continuous Sales Forecasting (Regression Leaderboard)
| Rank | Model Architecture | Type | MAE (US$) | RMSE (US$) | R² Score | MAPE (%) |
|:---:|---|---|:---:|:---:|:---:|:---:|
| **#1 🏆** | **Random Forest (300 Trees)** | **Ensemble ML** | **,897** | ,056 | **0.977** | **5.93%** |
| **#2** | **Ridge Regression (L2 Regularized)** | **Parametric ML** | **,216** | **,154** | **0.978** | **6.41%** |
| **#3** | **Linear Regression (OLS + OneHot)** | **Parametric ML** | **,353** | ,172 | **0.978** | **6.68%** |
| **#4** | **Naive: Prior Year Same Week (lag_52)** | **Heuristic** | **,416** | ,156 | **0.970** | **6.81%** |
| **#5** | **Naive: Prior Week (lag_1)** | **Heuristic** | **,423** | ,038 | **0.945** | **8.42%** |

- **Feature Importance:** lag_52 (sales of the same week in the prior calendar year) accounts for **97.12%** of Random Forest feature importance.

### B. Peak Demand Surge Detection (Classification Leaderboard)
| Metric | Normal Demand (Class 0) | High Demand Surge (Class 1) | Overall Chain Score |
|---|:---:|:---:|:---:|
| **Classification Accuracy** | — | — | **98.25%** |
| **Precision** | 98.17% | **98.51%** | 98.25% (Weighted) |
| **Recall (Sensitivity)** | 99.53% | **94.29%** | 98.25% (Weighted) |
| **F1-Score** | 98.85% | **96.35%** | 98.23% (Weighted) |
| **ROC-AUC Score** | — | — | **0.9854** |

---

## 📚 Deliverables & File Structure
`
├── Walmart_EDA.ipynb            # Primary Jupyter Notebook (All 6 Stages, fully executed, zero errors)
├── walmart_cleaning_pipeline.ipynb # Raw data cleaning demonstration pipeline
├── PROJECT_PROPOSAL.md          # Applied Data Science Project Proposal Document
├── TECHNICAL_REPORT.md          # Formal 6-Stage Technical Academic Report
├── VIVA_PREPARATION_GUIDE.md    # 60s pitch, 12 viva defense questions & rubric scoring answers
├── Walmart.csv                  # Original dataset (45 stores × 143 weeks, 6,435 records)
├── index.html                   # Standalone Executive Web Studio (Zero installation required)
├── app.py                       # Interactive Python Streamlit Dashboard
├── server.py                    # Lightweight Python REST API & Static Server
├── run_app.bat                  # One-click Windows launcher
└── outputs/
    ├── walmart_cleaned.csv      # Cleaned baseline dataset
    ├── walmart_features.csv     # Feature-engineered dataset (lags, rolling stats, surge target)
    ├── model_metrics.csv        # Benchmarked regression scores (MAE, RMSE, R², MAPE)
    ├── classification_metrics.csv # Classification scores (Precision, Recall, F1, Accuracy)
    ├── test_predictions.csv     # Unseen test period actual vs predicted values
    ├── model_rf.pkl             # Serialized Random Forest Regressor
    ├── model_lin.pkl            # Serialized Linear Regression pipeline
    ├── dashboard_data.json      # Pre-aggregated web studio metrics
    └── figures/                 # 13 high-resolution publication figures:
        ├── 01_sales_distribution.png        # Histogram & KDE (Linear & Log scale)
        ├── 02_store_avg_sales.png           # Ranked Bar Chart of Store Average Sales
        ├── 03_store_boxplot.png             # Box Plot of Store Sales Spread & Outliers
        ├── 04_total_sales_timeseries.png    # Line Chart of 143-Week Total Chain Sales
        ├── 05_seasonality_holiday.png       # Monthly Sales Bar Chart & Holiday Box Plot
        ├── 06_holiday_index.png             # Holiday Lift Multipliers vs Baseline
        ├── 07_scatter_external.png          # 4-Panel Scatter Plots with Regression Lines
        ├── 08_correlation_heatmaps.png      # Pooled vs Within-Store Correlation Heatmaps
        ├── 09_model_actual_vs_pred.png      # Actual vs Predicted Scatter & Timeline
        ├── 10_feature_importance.png        # Random Forest Top Feature Importances Bar Chart
        ├── 11_confusion_matrix.png          # High-Demand Surge Classification Confusion Matrix
        ├── 12_classification_roc_curve.png  # Receiver Operating Characteristic (ROC-AUC) Curve
        └── 13_regression_residuals.png      # Residual Distribution & Homoscedasticity Scatter
`

---
*Prepared for RVCE Applied Data Science Skill Lab.*
