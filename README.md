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

| Rank | Model Architecture | Type | MAE (US\$) | RMSE (US\$) | R² Score | MAPE (%) |
|:---:|---|---|:---:|:---:|:---:|:---:|
| **#1 🏆** | **Random Forest (300 Trees)** | **Ensemble ML** | **\$64,887** | \$94,056 | **0.977** | **5.93%** |
| **#2** | **Linear Regression (OLS + OneHot)** | **Parametric ML** | **\$67,353** | **\$92,172** | **0.978** | **6.68%** |
| **#3** | **Naive: Prior Year Same Week (`lag_52`)** | **Heuristic** | **\$75,416** | \$106,156 | **0.970** | **6.81%** |
| **#4** | **Naive: Prior Week (`lag_1`)** | **Heuristic** | **\$91,423** | \$144,038 | **0.945** | **8.42%** |

- **Feature Importance:** `lag_52` (sales of the same week in the prior calendar year) accounts for **97.12%** of Random Forest feature importance.

---

## 📚 Deliverables & File Structure
```
├── index.html                   # Standalone Executive Web Application
├── app.py                       # Python Streamlit Dashboard
├── server.py                    # Lightweight Python REST API & Static Server
├── run_app.bat                  # One-click Windows launcher
├── VIVA_PREPARATION_GUIDE.md    # 60s pitch, 10 anticipated questions & scoring answers
├── Walmart.csv                  # Raw dataset (45 stores × 143 weeks)
├── Walmart_EDA.ipynb            # Jupyter Notebook with full EDA & pipeline
└── outputs/
    ├── dashboard_data.json      # Structured aggregate metrics
    ├── data.js                  # Pre-computed client payload
    ├── model_metrics.csv        # Benchmarked model scores
    ├── test_predictions.csv     # Test period actual vs predictions
    ├── model_rf.pkl             # Serialized Random Forest model
    ├── model_lin.pkl            # Serialized Linear Regression pipeline
    └── figures/                 # 10 publication-quality notebook plots
```

---
*Prepared for RVCE Applied Data Science Skill Lab.*
