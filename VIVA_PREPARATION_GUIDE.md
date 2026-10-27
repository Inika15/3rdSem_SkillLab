# RVCE Applied Data Science Skill Lab — Viva Defense & Presentation Guide
**Project Title:** Walmart Store Sales Forecasting & Econometric Intelligence Studio  
**Dataset:** 45 Retail Stores × 143 Weeks (February 2010 – October 2012) • 6,435 Records  
**Author:** 3rd Sem Skill Lab

---

## 1. 60-Second Elevator Pitch (Memorize This)
> *"Good morning, Professors. Our project addresses multi-store sales forecasting for 45 Walmart supercenters. Using 143 weeks of historical records, we analyzed whether external macroeconomic factors like CPI, unemployment, and fuel prices drive weekly turnover, or if internal calendar seasonality and store format dominate.*
> 
> *Our exploratory data analysis proved that macro factors have negligible predictive power (<1% variance explained), while annual seasonality (`lag_52`) accounts for **97.1%** of Random Forest feature importance. By engineering domain-specific temporal lags and retaining authentic holiday surges, our **Random Forest champion model achieves a 5.93% Mean Absolute Percentage Error (MAPE)** and an **R² of 0.977** on unseen test weeks—beating naive retail heuristics by over \$26,000 per store-week."*

---

## 2. 5-Minute Demonstration Script (Step-by-Step UI Flow)

### Step 1: Open `index.html` (or run `run_app.bat` -> Option 1)
- **Show Tab 1 (Executive Overview):**
  - Point to the KPI banner: **\$7.132 Billion** cumulative chain volume, **45 stores**, weekly average of **\$1.108 Million**.
  - Show the **Chain Timeline chart**: Highlight the dramatic twin spikes occurring every November (Thanksgiving / Black Friday) and late December (Christmas rush).
  - Show the **Store Scale Disparity**: Store #2 is the largest (\$2.66M/week) vs Store #43 (\$0.34M/week), a **7.8× difference** in baseline volume due to store footprint and location format.

### Step 2: Explain the Outlier Treatment (Tab 1 / Slide 2)
- State clearly: *"We applied the IQR outlier detection rule, which flagged 127 observations (1.97%). Rather than naively deleting them, we conducted an investigation. 100% of these outliers occurred in large flagship stores during Thanksgiving and Christmas. In retail demand planning, deleting real holiday peaks results in under-stocking. Thus, we maintained a strict **'Investigate, Do Not Delete'** policy."*

### Step 3: Click Tab 3 (Macro & External Factors Studio)
- Show the **Pooled vs Within-Store Correlation Matrix**:
  - Point out that CPI, Fuel Price, and Unemployment have pooled correlations near 0 (-0.07, +0.01, -0.10).
  - Explain **Simpson's Paradox**: When pooling all stores together, store size differences mask underlying trends. Within individual stores, colder temperatures consistently boost holiday sales (within-store r = -0.138).

### Step 4: Click Tab 4 (Holiday & Seasonality Lab)
- Highlight the **Holiday Lift Multipliers**:
  - Thanksgiving lifts weekly store revenue to **1.35× baseline** (\$1.47M).
  - Reveal the **"Christmas Week Anomaly"**: The official holiday flag falls on Dec 30/31 (post-Christmas), but the *unflagged pre-Christmas week (Dec 23/24)* has the true annual peak at **1.65× baseline** (\$1.79M per store).

### Step 5: Click Tab 5 (Predictive Models & Leaderboard)
- Present the 4-model comparison table:
  1. **Naive Lag-1 (Prior Week):** MAE \$91,423 | MAPE 8.42%
  2. **Naive Lag-52 (Prior Year Same Week):** MAE \$75,416 | MAPE 6.81%
  3. **Linear Regression (OLS + One-Hot Stores):** MAE \$67,353 | MAPE 6.68%
  4. **Random Forest (300 Trees):** MAE \$64,887 | MAPE 5.93% (Champion 🏆)
- Highlight the **Feature Importance bar chart**: Show that `lag_52` accounts for **97.1%** of tree split weight.

### Step 6: Click Tab 6 (Live What-If Scenario Forecaster)
- Move the sliders in front of the professors!
  - Change the store selector to Store #2 (Flagship) vs Store #33 (Small).
  - Toggle `Holiday Flag` from 0 to 1 -> Watch the predicted revenue surge dynamically.
  - Tweak `Temperature` or `Fuel Price` -> Point out that predicted turnover changes very little, confirming the econometric finding that retail groceries are price-inelastic necessities.

---

## 3. Top 10 Anticipated Viva Questions & High-Scoring Answers

### Q1: Why did you not remove the 127 outliers detected by the IQR method?
**Answer:**
> *"In time-series retail econometrics, outliers are not necessarily errors. All 127 flagged points coincided with Black Friday (Thanksgiving) and Christmas shopping weeks in high-capacity supercenters. If we deleted them, our model would severely underestimate peak inventory requirements, causing severe out-of-stock losses. Therefore, we followed the industry-standard policy: investigate to verify data validity, then preserve them for accurate seasonal modeling."*

### Q2: Why is the correlation between macro indicators (CPI, Fuel Price, Unemployment) and sales so weak?
**Answer:**
> *"Walmart specializes in consumer staples, groceries, and discount general merchandise. These are non-discretionary goods with low price elasticity of demand. Customers continue buying groceries regardless of gas pump prices or moderate inflation. Furthermore, the variance across store formats (from \$340k to \$2.6M/wk) and holiday seasonality dwarfs the small percentage shifts caused by macroeconomic fluctuations."*

### Q3: What is the difference between pooled correlation and within-store correlation?
**Answer:**
> *"Pooled correlation calculates Pearson's r across all 6,435 observations simultaneously, conflating store-to-store baseline differences with temporal variation (an example of Simpson's Paradox). Within-store correlation computes the correlation separately for each store across its 143 weeks and averages the results. For example, the pooled correlation for temperature is -0.06, but the average within-store correlation is -0.14, showing that within any given store, winter brings higher sales."*

### Q4: Why does `lag_52` account for over 97% of Random Forest feature importance?
**Answer:**
> *"Retail sales exhibit strong 52-week annual periodicity. A store's sales in week 47 of this year (Thanksgiving) are predominantly determined by what that exact store sold in week 47 of last year, scaled slightly by overall store growth. `lag_52` acts as a compound feature capturing store identity, store footprint, regional demographics, and exact calendar seasonality simultaneously."*

### Q5: Why is model error higher on holiday weeks (8.3% MAPE) than on normal weeks (5.8% MAPE)?
**Answer:**
> *"Normal weeks have low variance and steady footfall, making them easy to predict with high precision. Holiday weeks, however, involve volatile customer surges driven by promotional circulars, competitor discounts, and whether Black Friday fell on pay-day weekends. Because holidays occur only once a year, the training data contains only two holiday examples per store, giving tree-based models fewer historical split opportunities."*

### Q6: Why did you split train and test chronologically rather than randomly?
**Answer:**
> *"In time-series forecasting, random cross-validation leaks future information into past predictions (data snooping / lookahead bias). We strictly partitioned the data chronologically at 80% (June 22, 2012), training only on earlier weeks and evaluating on 855 unseen future store-weeks from June to October 2012 to simulate realistic deployment."*

### Q7: What is the 'Christmas Week' anomaly in this dataset?
**Answer:**
> *"The Kaggle dataset flags `Holiday_Flag = 1` on the week ending Dec 31, 2010 and Dec 30, 2011. However, peak retail shopping occurs during the **pre-Christmas rush** (Dec 23/24), where chain-wide sales surpassed \$80 Million (> \$1.79M per store). The officially flagged post-Christmas week had lower sales. This highlights that business calendars and official statutory holidays often diverge in retail analytics."*

### Q8: Linear Regression had an R² of 0.978, very close to Random Forest's 0.977. Which is better?
**Answer:**
> *"While Linear Regression achieved a slightly lower RMSE (\$92,172 vs \$94,056), Random Forest delivered a superior **Mean Absolute Error (\$64,887 vs \$67,353)** and **MAPE (5.93% vs 6.68%)**. Because RMSE penalizes large outlier holiday errors quadratically, Linear Regression compromised typical-week accuracy to minimize peak errors. Random Forest provides better median and week-to-week forecast accuracy across normal operational periods."*

### Q9: What business recommendations would you give Walmart management?
**Answer:**
> *"1. **Staffing and Inventory Allocation:** Base baseline staffing on `lag_52` with store-specific multipliers, and allocate 1.4× to 1.6× buffer stock specifically for the two-week window of Thanksgiving through Christmas.  
> 2. **Calendar Alignment:** Create an internal promotional flag for the pre-Christmas week (Week 51) rather than relying on statutory holiday calendars.  
> 3. **Macro Agnosticism:** Avoid cutting grocery shelf inventory during gas price spikes, as grocery turnover is proven to remain stable."*

### Q10: What are the main limitations of this project and how would you improve it?
**Answer:**
> *"1. **Evaluation Window Restriction:** Our test period ended on October 26, 2012, so it contained Labor Day but did not test Thanksgiving or Christmas.  
> 2. **Lag Burn-in:** Using `lag_52` required sacrificing the first 52 weeks of data as history.  
> 3. **Missing Features:** Granular department sales, markdown discounts, and competitor locations were not in the public dataset. Future improvements would incorporate LightGBM, promotional markdown flags, and multi-step rolling walk-forward validation."*

---

## 4. Key Performance Metric Reference Card
| Metric | Baseline 1 (Lag-1) | Baseline 2 (Lag-52) | Linear Regression | Random Forest (Champion) |
|---|---|---|---|---|
| **MAE** | \$91,423 | \$75,416 | \$67,353 | **\$64,887** |
| **RMSE** | \$144,038 | \$106,156 | **\$92,172** | \$94,056 |
| **R²** | 0.945 | 0.970 | **0.978** | 0.977 |
| **MAPE** | 8.42% | 6.81% | 6.68% | **5.93%** |

---
*Created for RVCE Applied Data Science Skill Lab Mini-Project Evaluation.*
