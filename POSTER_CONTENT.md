# Poster Presentation Blueprint & Content Guide
## Walmart Store Sales Analytics & Predictive Demand Forecasting

Designed specifically to match the academic poster presentation layout (following the RVCE Skill Lab chart paper format).

---

## 📐 Poster Layout Grid (Visual Arrangement)

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           WALMART STORE SALES ANALYTICS                                               │
│             AGENDA: MULTI-STORE DEMAND FORECASTING & ECONOMETRIC INTELLIGENCE                         │
├───────────────────────────────┬───────────────────────────────────────┬───────────────────────────────┤
│  OBJECTIVES ~                 │        [CENTER VISUALS PANEL]         │  KEY TAKEAWAYS ~              │
│  • Comprehensive multi-store  │                                       │  • 52-WEEK LAG IS STRONGEST:  │
│    demand analysis.           │  ┌─────────────────────────────────┐  │    lag_52 drives 97.1% of     │
│  • Identify macroeconomic     │  │   CHART 1: STORE AVG SALES      │  │    model feature importance.  │
│    vs. calendar drivers.      │  │   (Ranked Bar Chart / Top vs    │  │  • STORE FOOTPRINT DOMINATES: │
│  • Evaluate outlier policy    │  │    Bottom Store Comparison)     │  │    7.8× volume disparity      │
│    under holiday volatility.  │  └─────────────────────────────────┘  │    across 45 store formats.   │
│  • Build predictive models for│                                       │  • MACRO FACTORS INELASTIC:   │
│    sales & surge detection.   │  ┌───────────────┐ ┌────────────────┐ │    CPI, Fuel, Unemployment    │
│                               │  │ CHART 2:      │ │ CHART 3:       │ │    explain <1% sales variance.│
│  TOOLS USED ~                 │  │ HOLIDAY LIFT  │ │ DONUT CHART:   │ │  • CHRISTMAS CALENDAR ANOMALY:│
│  [Python] [Pandas] [Seaborn]  │  │ (Thanksgiving │ │ NORMAL (93%)   │ │    True peak is pre-Christmas │
│  [Matplotlib] [Scikit-Learn]  │  │  1.35× lift)  │ │ vs HOLIDAY(7%) │ │    week at 1.65× baseline.    │
│                               │  └───────────────┘ └────────────────┘ │  • OUTLIER PRESERVATION:      │
│  METHODOLOGY ~                │                                       │    100% of IQR outliers are   │
│  • Data Ingestion (Panel Data)│  ┌───────────────┐ ┌────────────────┐ │    authentic holiday surges.  │
│  • Data Cleaning (0 missing)  │  │ CHART 4:      │ │ CHART 5:       │ │                               │
│  • Feature Engg (Lags & Target│  │ SCATTER PLOT: │ │ CONFUSION      │ │  RECOMMENDATIONS ~            │
│  • Exploratory Data Analysis  │  │ SALES vs TEMP │ │ MATRIX HEATMAP │ │  • BUFFER HOLIDAY INVENTORY:  │
│  • Predictive Models (RF/OLS) │  │ (Regression   │ │ (98.2% Accuracy│ │    Allocate 1.4×–1.6× buffer  │
│  • Insights & Presentation    │  │  Trendline)   │ │  Surge Alert)  │ │    for Thanksgiving & Wk 51.  │
│                               │  └───────────────┘ └────────────────┘ │  • REALIGN PROMO CALENDARS:   │
│  KEY METRICS ~                │                                       │    Target pre-Christmas Wk 51 │
│  ┌───────────┐ ┌───────────┐  │  ┌─────────────────────────────────┐  │    instead of statutory Dec 31│
│  │   6,435   │ │    45     │  │  │ CHART 6: ACTUAL vs PREDICTED    │  │  • AGNOSTIC TO FUEL SPIKES:   │
│  │TOTAL WEEKS│ │STORES RUN │  │  │ (Timeline with Holiday Peaks)   │  │    Maintain grocery stocking  │
│  ├───────────┤ ├───────────┤  │  └─────────────────────────────────┘  │    during gas price spikes.   │
│  │   5.93%   │ │  $1.05M   │  │                                       │  • AUTOMATE SURGE REPLENISH:  │
│  │CHAMPION   │ │AVERAGE    │  │                                       │    Use RF classifier to trigger│
│  │   MAPE    │ │WEEK SALES │  │                                       │    regional depot cross-docks.│
│  └───────────┘ └───────────┘  │                                       │                               │
│  • 8 attributes: Store, Date, │                                       │  NAMES: [YOUR NAMES]          │
│    Sales, Holiday, Temp, Fuel,│                                       │  TEAM: [TEAM ID]              │
│    CPI, Unemployment.         │                                       │                               │
└───────────────────────────────┴───────────────────────────────────────┴───────────────────────────────┘
```

---

## 📝 Exact Section-by-Section Content for Your Poster

### 1. Header (Top Center Banner)
* **Main Title:** `WALMART STORE SALES ANALYTICS`
* **Sub-title / Agenda:** `AGENDA: MULTI-STORE SALES FORECASTING & ECONOMETRIC INTELLIGENCE`

---

### 2. Left Column

#### `OBJECTIVES ~`
* Comprehensive analysis of 143-week sales across 45 hypermarkets.
* Determine whether external macro factors (CPI, Fuel, Unemployment) or calendar seasonality dominate retail demand.
* Establish an empirical outlier governance policy ("Investigate, Do Not Delete") under holiday demand surges.
* Engineer predictive time-series models for continuous sales forecasting and peak demand surge classification.

#### `TOOLS USED ~`
*(Draw small brand logos or colored boxes next to each tool)*
* **Python** (Core computational engine)
* **Pandas & NumPy** (Panel data wrangling & time-series lags)
* **Matplotlib & Seaborn** (Publication-grade visual analytics)
* **Scikit-Learn** (Ensemble pipelines, regression & classification models)

#### `METHODOLOGY ~`
* **Data Collection:** 45 Walmart US stores across 143 weeks (6,435 balanced observations).
* **Data Cleaning:** Verified zero missing values, zero duplicates, and strict chronological sorting.
* **Feature Engineering:** Calendar decomposition, 52-week lag (`lag_52`), 4-week moving average (`roll_mean_4`), and surge classification target.
* **Exploratory Analysis:** Descriptive parametric & non-parametric statistics, skewness, and store CV.
* **Predictive Modelling:** Benchmarked Linear Regression, Ridge, Random Forest Regressor, and Naive baselines.
* **Interpretation:** Translated empirical model findings into actionable retail inventory recommendations.

#### `KEY METRICS ~`
*(Draw 4 distinct colored rectangular boxes like in the sample poster)*
* **Box 1 (Purple / Red):**
  $$\mathbf{6,435}$$
  `TOTAL STORE-WEEKS`
* **Box 2 (Blue):**
  $$\mathbf{45}$$
  `STORES TRACKED`
* **Box 3 (Green):**
  $$\mathbf{5.93\%}$$
  `CHAMPION MAPE`
* **Box 4 (Orange / Peach):**
  $$\mathbf{\$1.05\text{M}}$$
  `AVERAGE WEEKLY SALES`

* **Short Bullet Note below Boxes:**
  * The dataset spans 8 attributes: Store ID, Week Date, Weekly Sales, Holiday Flag, Temperature, Fuel Price, CPI, and Unemployment Rate.

---

### 3. Center Column (Graphs & Visual Elements)

*(You can sketch or paste printouts of the figures from `outputs/figures/`)*

* **Chart 1 (Top Center — Bar Chart):**
  * **Title:** *Store Average Sales (Scale Disparity)*
  * **Sketch / Printout:** [`02_store_avg_sales.png`](file:///outputs/figures/02_store_avg_sales.png)
  * **Caption:** Highlights the 7.8× volume spread between Flagship Store #2 (\$2.66M/wk) and Compact Store #43 (\$342k/wk).
* **Chart 2 (Middle Left — Grouped / Column Bar Chart):**
  * **Title:** *Holiday Lift Multipliers*
  * **Sketch / Printout:** [`06_holiday_index.png`](file:///outputs/figures/06_holiday_index.png)
  * **Caption:** Thanksgiving generates a massive **1.35× sales lift** above baseline.
* **Chart 3 (Middle Right — Donut / Pie Chart):**
  * **Title:** *Calendar Composition*
  * **Drawing:** Donut chart with **93% Normal Weeks** (Blue) vs. **7% Holiday Weeks** (Orange).
* **Chart 4 (Lower Left — Scatter Plot with Trendline):**
  * **Title:** *Sales vs. Temperature*
  * **Sketch / Printout:** Subplot from [`07_scatter_external.png`](file:///outputs/figures/07_scatter_external.png)
  * **Caption:** Weak linear correlation ($r = -0.064$), demonstrating price-inelastic demand.
* **Chart 5 (Lower Right — Confusion Matrix Heatmap):**
  * **Title:** *Surge Demand Confusion Matrix*
  * **Drawing:** 2×2 grid from [`11_confusion_matrix.png`](file:///outputs/figures/11_confusion_matrix.png):
    * TN = 642 (75.1%) | FP = 3 (0.4%)
    * FN = 12 (1.4%) | TP = 198 (23.2%)
    * **Overall Accuracy: 98.25% | Precision: 98.51%**
* **Chart 6 (Bottom Center — Time-Series Line Chart):**
  * **Title:** *Chain-Wide Weekly Sales Timeline (2010–2012)*
  * **Sketch / Printout:** [`04_total_sales_timeseries.png`](file:///outputs/figures/04_total_sales_timeseries.png)
  * **Caption:** Twin annual spikes during Thanksgiving and Christmas recurring across all years.

---

### 4. Right Column

#### `KEY TAKEAWAYS ~`
* **PRIOR YEAR SAME-WEEK SALES (`lag_52`) IS THE STRONGEST DRIVER:** Accounts for **97.12%** of Random Forest feature importance; store sales repeat on strict 52-week annual cycles.
* **STORE FOOTPRINT DOMINATES VOLUME:** 45 locations exhibit a **7.8× disparity** in baseline sales (\$342k to \$2.66M/wk), reflecting physical formats rather than macro shocks.
* **MACROECONOMIC FACTORS ARE INELASTIC:** CPI, Fuel Prices, and Unemployment account for **<1%** of weekly sales variation; discount groceries are non-discretionary necessities.
* **THE "CHRISTMAS WEEK" CALENDAR ANOMALY:** The statutory holiday flag is on Dec 30/31, but the true annual sales peak occurs during the **unflagged pre-Christmas week** (Dec 23/24) at **1.65× baseline** (>\$1.79M per store).
* **OUTLIERS ARE CRITICAL SURGES ("DO NOT DELETE"):** All 127 IQR outliers occur during authentic Black Friday and pre-Christmas peaks; deleting them causes severe under-stocking.
* **RANDOM FOREST IS THE CHAMPION MODEL:** Delivers **5.93% MAPE** and **\$64,897 MAE**, beating naive heuristics by over \$26,500 per store-week.

#### `RECOMMENDATIONS ~`
* **ALLOCATE PRE-HOLIDAY BUFFER STOCK:** Provide **1.4× to 1.6×** baseline safety stock starting 3 weeks prior to Thanksgiving through pre-Christmas Week 51.
* **REALIGN MERCHANDISING CALENDARS:** Create an internal operational surge flag for Week 51 (pre-Christmas rush) rather than relying on statutory federal holiday dates.
* **MAINTAIN GROCERY STOCKING DURING FUEL HIKES:** Do not reduce inventory orders when fuel prices rise; grocery footfall and purchase volumes remain resilient.
* **DEPLOY AUTOMATED PEAK ALERTS:** Integrate the Random Forest Classifier (**98.5% precision**) to automatically schedule temporary warehouse labor and cross-docking bays ahead of surge weeks.

#### `PROJECT CREDITS` *(Bottom Right Corner)*
* **NAMES:** `[Enter Member 1, Member 2, Member 3]`
* **TEAM ID:** `TEAM-[Your Team Number]`
* **COURSE:** `RVCE Applied Data Science Skill Lab`
