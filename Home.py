import streamlit as st

st.set_page_config(
    page_title="99 Acres | Gurgaon Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# Light styling only — no layout overrides that break Streamlit UI
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&display=swap');
.big-title { font-family:'Syne',sans-serif; font-size:48px; font-weight:800; color:#0f172a; line-height:1.1; }
.orange { color:#f97316; }
.subtitle { font-size:17px; color:#64748b; margin-top:8px; line-height:1.7; }
.stat-box { background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:20px 24px; text-align:center; }
.stat-num { font-family:'Syne',sans-serif; font-size:30px; font-weight:800; color:#f97316; }
.stat-label { font-size:12px; color:#94a3b8; margin-top:4px; }
.step-card { background:#fff; border:1px solid #e2e8f0; border-left:4px solid #f97316; border-radius:10px; padding:18px 20px; margin-bottom:12px; }
.step-num { font-size:11px; color:#f97316; font-weight:700; letter-spacing:1px; text-transform:uppercase; }
.step-title { font-size:16px; font-weight:700; color:#0f172a; margin:4px 0; }
.step-desc { font-size:13px; color:#64748b; line-height:1.6; }
.tag { display:inline-block; background:#fff7ed; color:#f97316; font-size:11px; font-weight:600; padding:3px 10px; border-radius:20px; margin-top:8px; }
.chip-row { display:flex; flex-wrap:wrap; gap:10px; margin-top:8px; }
.chip { background:#f1f5f9; color:#475569; font-size:13px; padding:6px 16px; border-radius:100px; font-weight:500; }
.section-title { font-family:'Syne',sans-serif; font-size:26px; font-weight:800; color:#0f172a; margin-bottom:4px; }
.section-sub { font-size:14px; color:#94a3b8; margin-bottom:20px; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 48px 0 32px 0;">
    <div class="big-title">99<span class="orange">Acres</span> ML<br>Price Predictor</div>
    <div class="subtitle">Machine learning powered property price prediction<br>for Gurgaon real estate — built on real 99 Acres data.</div>
</div>
""", unsafe_allow_html=True)

st.page_link("pages/1_Price_Predictor.py", label="⚡ Try the Price Predictor", icon="🏠")
st.divider()

# ── STATS ─────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="stat-box"><div class="stat-num">2,600+</div><div class="stat-label">Property Listings</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-box"><div class="stat-num">200+</div><div class="stat-label">Gurgaon Sectors and Locations </div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-box"><div class="stat-num">91%</div><div class="stat-label">Model Accuracy (R²)</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="stat-box"><div class="stat-num">±8%</div><div class="stat-label">Price Range Margin</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# ── WORKFLOW ──────────────────────────────────────────────────────
st.markdown('<div class="section-title">Project Pipeline</div><div class="section-sub">End-to-end ML workflow from data to prediction</div>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)

steps_left = [
    ("01", "Data Collection", "Scraped real property listings from 99 Acres across Gurgaon sectors — BHK, area, price, amenities.", "Web Scraping"),
    ("02", "Cleaning & Preprocessing", "Handled nulls, fixed data types, removed outliers, applied log transformation on price.", "Pandas · NumPy"),
    ("03", "Exploratory Analysis", "Univariate and multivariate EDA to uncover price patterns by sector, BHK, and age.", "Matplotlib · Seaborn"),
]
steps_right = [
    ("04", "Feature Engineering", "Built meaningful features from BHK, carpet area, age brackets, and location encoding.", "Scikit-Learn"),
    ("05", "Feature Selection", "Correlation analysis and feature importance to retain the most predictive signals.", "SelectKBest · RFE"),
    ("06", "Model Training & Tuning", "XGBoost Regressor tuned with RandomizedSearchCV — delivers a reliable price range.", "XGBoost · GridSearchCV"),
]

with col_a:
    for num, title, desc, tag in steps_left:
        st.markdown(f"""
        <div class="step-card">
            <div class="step-num">Step {num}</div>
            <div class="step-title">{title}</div>
            <div class="step-desc">{desc}</div>
            <div class="tag">{tag}</div>
        </div>
        """, unsafe_allow_html=True)

with col_b:
    for num, title, desc, tag in steps_right:
        st.markdown(f"""
        <div class="step-card">
            <div class="step-num">Step {num}</div>
            <div class="step-title">{title}</div>
            <div class="step-desc">{desc}</div>
            <div class="tag">{tag}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()


# ── TECH STACK ────────────────────────────────────────────────────
st.markdown('<div class="section-title">Tech Stack</div>', unsafe_allow_html=True)
st.markdown("""
<div class="chip-row">
    <div class="chip">🐍 Python</div>
    <div class="chip">🐼 Pandas</div>
    <div class="chip">🔢 NumPy</div>
    <div class="chip">📊 Matplotlib</div>
    <div class="chip">🎨 Seaborn</div>
    <div class="chip">⚙️ Scikit-Learn</div>
    <div class="chip">⚡ XGBoost</div>
    <div class="chip">🔍 RandomizedSearchCV</div>
    <div class="chip">🌐 Streamlit</div>
    <div class="chip">🕸 BeautifulSoup</div>
    <div class="chip">📦 Pickle</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── FOOTER ────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding: 16px 0 8px 0; color:#94a3b8; font-size:13px;">
    Built by <b style="color:#0f172a">Prince Kumar</b> · Data Scientist · 📞 9971287050<br>
    <a href="https://www.linkedin.com/in/prince-datascientist" target="_blank" style="color:#f97316; text-decoration:none;">LinkedIn</a> &nbsp;·&nbsp;
    <a href="https://github.com/prince-kumar-ds" target="_blank" style="color:#f97316; text-decoration:none;">GitHub</a> &nbsp;·&nbsp;
    <a href="https://github.com/prince-kumar-ds/99_Acers" target="_blank" style="color:#f97316; text-decoration:none;">Project Repo</a>
</div>
""", unsafe_allow_html=True)