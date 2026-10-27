"""
Walmart Store Sales Intelligence & Forecasting Studio
RVCE Applied Data Science Skill Lab — Mini-Project
"""

import os
import json
import pickle
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Walmart Retail Econometrics & Forecasting",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# CUSTOM CLASSY STYLING (WALMART HERITAGE PALETTE)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=JetBrains+Mono:wght@400;600&family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Newsreader', Georgia, serif;
        font-weight: 600;
        letter-spacing: -0.01em;
        color: #0b1e3a;
    }
    
    .stMetricValue {
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 700 !important;
        color: #0b1e3a !important;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #071120 0%, #0d1e3a 50%, #09152b 100%);
        border-radius: 12px;
        padding: 24px 32px;
        color: #ffffff;
        margin-bottom: 24px;
        border-bottom: 2px solid #d97706;
    }
    
    .hero-title {
        font-family: 'Newsreader', Georgia, serif;
        font-size: 32px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 6px;
    }
    
    .hero-sub {
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: #94a3b8;
    }
    
    .badge-gold {
        background: rgba(217, 119, 6, 0.2);
        color: #fbbf24;
        border: 1px solid rgba(217, 119, 6, 0.4);
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 600;
        display: inline-block;
    }
    
    .callout-card {
        background: #f8fafc;
        border-left: 4px solid #d97706;
        padding: 16px 20px;
        border-radius: 0 8px 8px 0;
        margin: 16px 0;
        font-size: 14px;
        color: #1e293b;
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DATA LOADING & CACHING
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv('Walmart.csv')
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
    df = df.sort_values(['Store', 'Date']).reset_index(drop=True)
    
    with open('outputs/dashboard_data.json', 'r', encoding='utf-8') as f:
        meta = json.load(f)
        
    return df, meta

@st.cache_resource
def load_models():
    models = {}
    if os.path.exists('outputs/model_rf.pkl'):
        with open('outputs/model_rf.pkl', 'rb') as f:
            models['rf'] = pickle.load(f)
    if os.path.exists('outputs/model_lin.pkl'):
        with open('outputs/model_lin.pkl', 'rb') as f:
            models['lin'] = pickle.load(f)
    return models

df, meta = load_data()
models = load_models()

# -----------------------------------------------------------------------------
# HERO BANNER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
        <div>
            <div class="hero-title">Walmart Store Sales Intelligence & Forecasting Studio</div>
            <div class="hero-sub">RVCE Applied Data Science Skill Lab — Mini-Project • 45 Stores • 143 Weeks (2010–2012)</div>
        </div>
        <div>
            <span class="badge-gold">Academic Evaluation Edition</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SIDEBAR CONTROLS
# -----------------------------------------------------------------------------
st.sidebar.markdown("### 🏬 Navigation & Store Filter")
mode = st.sidebar.radio(
    "Select Lab View:",
    [
        "1. Executive Overview",
        "2. Store Intelligence Explorer",
        "3. Macroeconomic Analysis",
        "4. Holiday & Seasonality Lab",
        "5. Predictive Models & Leaderboard",
        "6. Live What-If Scenario Forecaster",
        "7. Notebook Figures Gallery",
        "8. Viva Defense Slide Deck"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Dataset Summary:**
- **Observations:** 6,435 records
- **Stores:** 45 Supercenters
- **Date Span:** Feb 2010 – Oct 2012
- **Cumulative Volume:** $7.132 Billion
- **Champion Model:** Random Forest (5.93% MAPE)
""")

# -----------------------------------------------------------------------------
# TAB 1: EXECUTIVE OVERVIEW
# -----------------------------------------------------------------------------
if mode == "1. Executive Overview":
    st.markdown("## Executive Overview & Chain Performance")
    st.markdown("Macro performance briefing across Walmart's 45 US supercenters over 143 weeks.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Chain Revenue", "$7.132 B", help="Cumulative turnover across 143 weeks")
    with col2:
        st.metric("Store Weekly Mean", "$1.108 M", "+17.9% vs Median ($940k)")
    with col3:
        st.metric("Holiday Volume Lift", "1.302×", "+30.24% surge during holiday weeks")
    with col4:
        st.metric("Store Disparity Ratio", "7.77×", "Store #2 ($2.66M) vs Store #43 ($0.34M)")
        
    st.markdown("---")
    
    st.markdown("### Total Chain Weekly Sales Timeline (US$ Million)")
    timeline_df = df.groupby('Date').agg({
        'Weekly_Sales': 'sum',
        'Holiday_Flag': 'first'
    }).reset_index()
    timeline_df['Sales_Millions'] = timeline_df['Weekly_Sales'] / 1e6
    
    fig = px.line(
        timeline_df,
        x='Date',
        y='Sales_Millions',
        title="Chain-Wide Weekly Sales (2010–2012) with Pronounced Thanksgiving & Christmas Surges",
        labels={'Sales_Millions': 'Total Sales ($M)', 'Date': 'Week Ending'},
        color_discrete_sequence=['#002244']
    )
    
    # Highlight holiday weeks
    holidays = timeline_df[timeline_df['Holiday_Flag'] == 1]
    fig.add_trace(go.Scatter(
        x=holidays['Date'],
        y=holidays['Sales_Millions'],
        mode='markers',
        name='Holiday Week',
        marker=dict(color='#d97706', size=8, symbol='diamond')
    ))
    fig.update_layout(height=420, hovermode="x unified", margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### Top 5 vs Bottom 5 Stores by Revenue")
        store_totals = df.groupby('Store')['Weekly_Sales'].agg(['mean', 'sum']).reset_index()
        store_totals['Weekly_Mean_M'] = store_totals['mean'] / 1e6
        store_totals['Total_Sales_M'] = store_totals['sum'] / 1e6
        store_totals = store_totals.sort_values('sum', ascending=False).reset_index(drop=True)
        
        top5 = store_totals.head(5).copy()
        top5['Type'] = 'Top 5 Flagship'
        bottom5 = store_totals.tail(5).copy()
        bottom5['Type'] = 'Bottom 5 Compact'
        
        disp_df = pd.concat([top5, bottom5])[['Store', 'Type', 'Weekly_Mean_M', 'Total_Sales_M']]
        disp_df.columns = ['Store #', 'Tier', 'Weekly Avg ($M)', 'Total Sales ($M)']
        st.dataframe(disp_df.style.format({'Weekly Avg ($M)': '${:.2f}M', 'Total Sales ($M)': '${:.2f}M'}), use_container_width=True)
        
    with col_b:
        st.markdown("### Outlier Policy: Investigate, Do Not Delete")
        st.markdown("""
        <div class="callout-card">
            <strong>Key Data Science Methodology Justification:</strong><br>
            The standard Interquartile Range (IQR) rule flags <strong>127 weeks (1.97%)</strong> as outliers.<br><br>
            All 127 data points belong to high-volume supercenters during <strong>Thanksgiving (Black Friday)</strong> and <strong>Christmas rushes</strong>. In retail inventory forecasting, purging these real revenue peaks biases inventory downwards, causing catastrophic out-of-stock events during peak consumer demand.
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TAB 2: STORE INTELLIGENCE EXPLORER
# -----------------------------------------------------------------------------
elif mode == "2. Store Intelligence Explorer":
    st.markdown("## Store Intelligence & Portfolio Explorer")
    
    selected_store = st.selectbox(
        "Select Store ID to inspect:",
        options=sorted(df['Store'].unique()),
        index=0
    )
    
    store_df = df[df['Store'] == selected_store].sort_values('Date').reset_index(drop=True)
    s_mean = store_df['Weekly_Sales'].mean()
    s_median = store_df['Weekly_Sales'].median()
    s_std = store_df['Weekly_Sales'].std()
    s_cv = s_std / s_mean
    s_max = store_df['Weekly_Sales'].max()
    s_min = store_df['Weekly_Sales'].min()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Store Weekly Mean", f"${s_mean/1e6:.2f}M", f"{((s_mean/1108331.6)-1)*100:+.1f}% vs Chain")
    with col2:
        st.metric("Weekly Median", f"${s_median/1e6:.2f}M")
    with col3:
        st.metric("Stability (CV)", f"{s_cv:.3f}", f"Std Dev: ${s_std/1e3:.0f}k")
    with col4:
        st.metric("Peak Holiday Week", f"${s_max/1e6:.2f}M", f"Min: ${s_min/1e6:.2f}M")
        
    fig_store = px.line(
        store_df,
        x='Date',
        y='Weekly_Sales',
        title=f"Store #{selected_store} — 143-Week Sales Trajectory",
        labels={'Weekly_Sales': 'Weekly Sales ($)', 'Date': 'Date'},
        color_discrete_sequence=['#1e40af']
    )
    fig_store.add_hline(y=s_mean, line_dash="dash", line_color="#d97706", annotation_text=f"Mean: ${s_mean/1e6:.2f}M")
    fig_store.update_layout(height=400, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_store, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 3: MACROECONOMIC ANALYSIS
# -----------------------------------------------------------------------------
elif mode == "3. Macroeconomic Analysis":
    st.markdown("## Macroeconomic & Environmental Factors Studio")
    st.markdown("""
    <div class="callout-card">
        <strong>Econometric Takeaway:</strong> External macro variables (CPI, Fuel Price, Unemployment, Temperature) have 
        <strong>near-zero correlation</strong> with weekly sales once store baseline scale and 52-week seasonality are accounted for.
    </div>
    """, unsafe_allow_html=True)
    
    factor = st.selectbox(
        "Select Macro Indicator to analyze against Weekly Sales:",
        ["Temperature", "Fuel_Price", "CPI", "Unemployment"]
    )
    
    fig_scatter = px.scatter(
        df,
        x=factor,
        y='Weekly_Sales',
        color='Store',
        opacity=0.6,
        title=f"Weekly Sales vs {factor} (Color by Store)",
        labels={'Weekly_Sales': 'Weekly Sales ($)'},
        color_continuous_scale='Viridis'
    )
    fig_scatter.update_layout(height=450, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown("### Pooled vs. Within-Store Correlations")
    corr_df = pd.DataFrame([
        {"Indicator": "Temperature (°F)", "Pooled Correlation": -0.0639, "Within-Store Correlation": -0.1384, "Finding": "Colder winter temps correlate with holiday peaks."},
        {"Indicator": "Fuel Price ($/gal)", "Pooled Correlation": +0.0095, "Within-Store Correlation": -0.0121, "Finding": "Negligible direct elasticity on essential goods."},
        {"Indicator": "CPI (Index)", "Pooled Correlation": -0.0726, "Within-Store Correlation": +0.0214, "Finding": "Inflation rose 15% but weekly sales remained steady."},
        {"Indicator": "Unemployment (%)", "Pooled Correlation": -0.1062, "Within-Store Correlation": -0.0452, "Finding": "Slight negative tilt; store format dominates."}
    ])
    st.dataframe(corr_df, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 4: HOLIDAY & SEASONALITY LAB
# -----------------------------------------------------------------------------
elif mode == "4. Holiday & Seasonality Lab":
    st.markdown("## Holiday & Seasonality Dynamics Lab")
    
    st.markdown("### Holiday Lift Multipliers vs Non-Holiday Baseline ($1.085M)")
    hol_df = pd.DataFrame([
        {"Holiday Event": "Super Bowl", "Calendar Window": "Mid-February (Week 06)", "Mean Sales": "$1.079 M", "Lift Multiplier": "0.994×", "Surge %": "-0.6%"},
        {"Holiday Event": "Labor Day", "Calendar Window": "Early September (Week 36)", "Mean Sales": "$1.042 M", "Lift Multiplier": "0.960×", "Surge %": "-4.0%"},
        {"Holiday Event": "Thanksgiving", "Calendar Window": "Late November (Week 47)", "Mean Sales": "$1.471 M", "Lift Multiplier": "1.355×", "Surge %": "+35.5%"},
        {"Holiday Event": "Pre-Christmas Rush", "Calendar Window": "Dec 23–24 (Week 51)", "Mean Sales": "$1.790 M", "Lift Multiplier": "1.649×", "Surge %": "+64.9%"},
        {"Holiday Event": "Christmas (Flagged)", "Calendar Window": "Dec 30–31 (Week 52)", "Mean Sales": "$1.391 M", "Lift Multiplier": "1.282×", "Surge %": "+28.2%"}
    ])
    st.dataframe(hol_df, use_container_width=True)
    
    st.markdown("""
    <div class="callout-card">
        <strong>The "Christmas Week" Calendar Anomaly:</strong><br>
        In Walmart's historical record, the official <code>Holiday_Flag = 1</code> falls on Dec 30/31 (post-holiday New Year's eve). 
        However, the <strong>unflagged pre-Christmas week</strong> (Dec 23/24) consistently generated over <strong>$1.79M per store</strong>, representing the true annual demand peak.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TAB 5: PREDICTIVE MODELS & LEADERBOARD
# -----------------------------------------------------------------------------
elif mode == "5. Predictive Models & Leaderboard":
    st.markdown("## Predictive Modeling Benchmark & Evaluation")
    st.markdown("Time-based split: 80% Train (Feb 2010 – Jun 2012) | 20% Test (Jun 2012 – Oct 2012; 855 unseen store-weeks).")
    
    models_df = pd.DataFrame([
        {"Rank": "#1 🏆", "Model Architecture": "Random Forest (300 Trees)", "Type": "Ensemble ML", "MAE ($)": "$64,887", "RMSE ($)": "$94,056", "R² Score": 0.977, "MAPE (%)": "5.93%"},
        {"Rank": "#2", "Model Architecture": "Linear Regression (OLS + One-Hot)", "Type": "Parametric ML", "MAE ($)": "$67,353", "RMSE ($)": "$92,172", "R² Score": 0.978, "MAPE (%)": "6.68%"},
        {"Rank": "#3", "Model Architecture": "Naive: Same Week Last Year (Lag-52)", "Type": "Heuristic", "MAE ($)": "$75,416", "RMSE ($)": "$106,156", "R² Score": 0.970, "MAPE (%)": "6.81%"},
        {"Rank": "#4", "Model Architecture": "Naive: Previous Week (Lag-1)", "Type": "Heuristic", "MAE ($)": "$91,423", "RMSE ($)": "$144,038", "R² Score": 0.945, "MAPE (%)": "8.42%"}
    ])
    st.dataframe(models_df, use_container_width=True)
    
    col_x, col_y = st.columns(2)
    with col_x:
        st.markdown("### Random Forest Feature Importance")
        feat_df = pd.DataFrame([
            {"Feature": "lag_52 (Prior Year Same Week)", "Importance (%)": 97.12},
            {"Feature": "Store Identity (Scale/Format)", "Importance (%)": 1.42},
            {"Feature": "roll_mean_4 (4-Wk Momentum)", "Importance (%)": 0.58},
            {"Feature": "lag_1 (Previous Week)", "Importance (%)": 0.39},
            {"Feature": "Month / WeekOfYear", "Importance (%)": 0.24},
            {"Feature": "Holiday_Flag", "Importance (%)": 0.15},
            {"Feature": "Macro Factors (CPI, Fuel, Temp, Unemp)", "Importance (%)": 0.10}
        ])
        fig_feat = px.bar(
            feat_df,
            x='Importance (%)',
            y='Feature',
            orientation='h',
            title="Dominance of lag_52 (97.1%) in Random Forest Splits",
            color_discrete_sequence=['#d97706']
        )
        fig_feat.update_layout(yaxis=dict(autorange="reversed"), height=350, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_feat, use_container_width=True)
        
    with col_y:
        st.markdown("### Test Period Fit: Actual vs Predicted")
        test_pred_df = pd.read_csv('outputs/test_predictions.csv')
        test_chain = test_pred_df.groupby('Date')[['Actual', 'Pred_RF']].sum().reset_index()
        test_chain['Actual_M'] = test_chain['Actual'] / 1e6
        test_chain['Pred_RF_M'] = test_chain['Pred_RF'] / 1e6
        
        fig_test = px.line(
            test_chain,
            x='Date',
            y=['Actual_M', 'Pred_RF_M'],
            title="Chain-Wide Total Sales over 19 Unseen Test Weeks (US$ Million)",
            labels={'value': 'Total Sales ($M)', 'Date': 'Date'},
            color_discrete_map={'Actual_M': '#002244', 'Pred_RF_M': '#d97706'}
        )
        fig_test.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_test, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 6: LIVE WHAT-IF SCENARIO FORECASTER
# -----------------------------------------------------------------------------
elif mode == "6. Live What-If Scenario Forecaster":
    st.markdown("## Interactive What-If Scenario Forecaster")
    st.markdown("Simulate weekly sales using the trained machine learning pipeline.")
    
    col_in, col_out = st.columns([1.2, 1])
    with col_in:
        s_store = st.selectbox("Select Target Store:", options=sorted(df['Store'].unique()), index=0)
        s_holiday = st.selectbox("Holiday Event Status:", [0, 1], format_func=lambda x: "Holiday Week (Thanksgiving/Christmas)" if x == 1 else "Normal Week")
        s_temp = st.slider("Temperature (°F):", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
        s_fuel = st.slider("Fuel Price ($/gal):", min_value=2.0, max_value=5.0, value=3.5, step=0.05)
        s_cpi = st.slider("CPI Index:", min_value=120.0, max_value=230.0, value=215.0, step=1.0)
        s_unemp = st.slider("Unemployment Rate (%):", min_value=3.5, max_value=15.0, value=7.5, step=0.1)
        s_month = st.selectbox("Calendar Month:", list(range(1, 13)), index=10)
        
        store_mean = df[df['Store'] == s_store]['Weekly_Sales'].mean()
        s_lag52 = st.slider("Prior Year Same-Week Sales (lag_52):", min_value=float(store_mean*0.5), max_value=float(store_mean*2.0), value=float(store_mean))
        
    with col_out:
        if 'rf' in models:
            sample_row = pd.DataFrame([{
                'Holiday_Flag': s_holiday,
                'Temperature': s_temp,
                'Fuel_Price': s_fuel,
                'CPI': s_cpi,
                'Unemployment': s_unemp,
                'Month': s_month,
                'WeekOfYear': s_month * 4,
                'lag_1': store_mean,
                'lag_52': s_lag52,
                'roll_mean_4': store_mean,
                'Store': s_store
            }])
            
            pred_rf_val = models['rf'].predict(sample_row)[0]
            pred_lin_val = models['lin'].predict(sample_row)[0] if 'lin' in models else pred_rf_val
            
            st.markdown(f"""
            <div style="background:linear-gradient(135deg, #09152b 0%, #0e2246 100%); padding:28px; border-radius:12px; color:#ffffff; border:1px solid #d97706;">
                <div style="font-size:12px; text-transform:uppercase; color:#94a3b8; font-family:'JetBrains Mono',monospace;">Forecasted Store Sales</div>
                <div style="font-size:36px; font-weight:700; color:#fbbf24; font-family:'JetBrains Mono',monospace; margin:8px 0;">${pred_rf_val:,.0f}</div>
                <div style="font-size:13px; color:#e2e8f0;">
                    Confidence Interval (±5.9% MAPE):<br>
                    <strong>${pred_rf_val*0.941:,.0f} – ${pred_rf_val*1.059:,.0f}</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### Benchmarks")
            diff_pct = ((pred_rf_val - store_mean) / store_mean) * 100
            st.write(f"- **Store Historical Mean:** ${store_mean:,.0f}")
            st.write(f"- **Surge vs Baseline:** **{diff_pct:+.1f}%**")
            st.write(f"- **Linear Model Estimate:** ${pred_lin_val:,.0f}")
            st.write(f"- **Random Forest Estimate:** ${pred_rf_val:,.0f}")

# -----------------------------------------------------------------------------
# TAB 7: NOTEBOOK FIGURES GALLERY
# -----------------------------------------------------------------------------
elif mode == "7. Notebook Figures Gallery":
    st.markdown("## Official Notebook Visualizations")
    st.markdown("Direct figures generated by `Walmart_EDA.ipynb` during the skill lab experiment.")
    
    figures = [
        ("01_sales_distribution.png", "01. Distribution of Weekly Sales (Right-Skewed Tail)"),
        ("02_store_avg_sales.png", "02. Ranked Average Sales Across 45 Stores"),
        ("03_store_boxplot.png", "03. Store Sales Boxplots & Outlier Distribution"),
        ("04_total_sales_timeseries.png", "04. Chain-Wide 143-Week Sales Time Series"),
        ("05_seasonality_holiday.png", "05. Monthly Seasonality & Holiday Effect"),
        ("06_holiday_index.png", "06. Normalized Holiday Sales Index"),
        ("07_scatter_external.png", "07. Scatter Plots: External Factors vs Weekly Sales"),
        ("08_correlation_heatmaps.png", "08. Correlation Heatmaps (Pooled vs Within-Store)"),
        ("09_model_actual_vs_pred.png", "09. Model Diagnostics: Actual vs Predicted Scatter & Time Series"),
        ("10_feature_importance.png", "10. Random Forest Top Feature Importances")
    ]
    
    for filename, title in figures:
        filepath = os.path.join("outputs", "figures", filename)
        if os.path.exists(filepath):
            st.markdown(f"### {title}")
            st.image(filepath, use_container_width=True)
            st.markdown("---")

# -----------------------------------------------------------------------------
# TAB 8: VIVA DEFENSE SLIDE DECK
# -----------------------------------------------------------------------------
elif mode == "8. Viva Defense Slide Deck":
    st.markdown("## Viva Defense Presentation Deck")
    st.markdown("Tailored slide cards for presenting to the evaluation committee.")
    
    st.markdown("""
    <div class="callout-card">
        <h3>Slide 1: Problem Definition & Objectives</h3>
        <ul>
            <li><strong>Challenge:</strong> Predicting weekly sales across 45 hypermarkets with high holiday volatility.</li>
            <li><strong>Dataset:</strong> 6,435 records (143 weeks, 2010–2012) from Kaggle/Walmart Recruiting competition.</li>
            <li><strong>Core Question:</strong> Do external macroeconomic indicators drive retail demand or does historical calendar seasonality dominate?</li>
        </ul>
    </div>
    
    <div class="callout-card">
        <h3>Slide 2: Data Cleaning & Outlier Justification</h3>
        <ul>
            <li><strong>Verification:</strong> Perfect temporal continuity (every store has exactly 143 weekly observations; 0 missing values).</li>
            <li><strong>Outlier Decision:</strong> 127 records flagged by IQR were intentionally retained because 100% represent genuine Thanksgiving and Christmas revenue surges in large stores. Deleting them destroys retail inventory planning.</li>
        </ul>
    </div>
    
    <div class="callout-card">
        <h3>Slide 3: Exploratory Findings</h3>
        <ul>
            <li><strong>Store Scale:</strong> 7.8× disparity between largest and smallest supercenters.</li>
            <li><strong>Holiday Lift:</strong> Average chain-wide lift of +30.2% on holiday weeks, with pre-Christmas week reaching 1.65× baseline.</li>
            <li><strong>Macro Myth:</strong> CPI, Unemployment, and Fuel Price exhibit near-zero linear correlation with weekly sales fluctuations.</li>
        </ul>
    </div>
    
    <div class="callout-card">
        <h3>Slide 4: Feature Engineering & Time-Series Lags</h3>
        <ul>
            <li><code>lag_1</code>: Prior week's sales (short-term inertia).</li>
            <li><code>lag_52</code>: Prior year's same-week sales (annual seasonal anchor).</li>
            <li><code>roll_mean_4</code>: 4-week rolling average (recent momentum).</li>
            <li><strong>Strict Splitting:</strong> Chronological cut at June 22, 2012 (unseen test set of 855 store-weeks).</li>
        </ul>
    </div>
    
    <div class="callout-card">
        <h3>Slide 5: Model Leaderboard & Champion Model</h3>
        <ul>
            <li><strong>Random Forest:</strong> MAE $64,887 | RMSE $94,056 | R² 0.977 | MAPE 5.93%.</li>
            <li><strong>Linear Regression:</strong> MAE $67,353 | RMSE $92,172 | R² 0.978 | MAPE 6.68%.</li>
            <li><strong>Dominant Feature:</strong> <code>lag_52</code> accounts for 97.1% of Random Forest split importance.</li>
        </ul>
    </div>
    
    <div class="callout-card">
        <h3>Slide 6: Limitations & Future Enhancements</h3>
        <ul>
            <li><strong>Test Period Truncation:</strong> Test set ends in October 2012, missing Thanksgiving/Christmas in the evaluation window.</li>
            <li><strong>Feature Needs:</strong> Department-level granularity and markdown promotion flags would further improve precision.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
