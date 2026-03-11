import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Price Predictor | 99 Acres ML", page_icon="🏙️", layout="centered")

# ── Load assets ───────────────────────────────────────────────────────────────
@st.cache_resource
def load_assets():
    with open('df.pkl', 'rb') as f:
        df = pickle.load(f)
    with open('pipeline.pkl', 'rb') as f:
        pipeline = pickle.load(f)
    return df, pipeline

df, pipeline = load_assets()

# ── Page Header ───────────────────────────────────────────────────────────────
st.title("🏙️ Gurgaon Property Price Predictor")
st.caption("ML-powered price estimation based on real 99 Acres listings · XGBoost Model · 91% Accuracy")
st.divider()

# ── Section 1: Location ───────────────────────────────────────────────────────
st.subheader("📍 Location & Property Type")
col1, col2 = st.columns(2)
with col1:
    property_type = st.selectbox("Property Type", sorted(df['property_type'].unique()))
with col2:
    sector = st.selectbox("Sector", sorted(df['property_name'].unique()))

# ── Section 2: Configuration ──────────────────────────────────────────────────
st.subheader("🛏 Configuration")
col3, col4, col5 = st.columns(3)
with col3:
    bedroom = int(st.selectbox("Bedrooms", sorted(df['bedroom'].unique())))
with col4:
    bathroom = int(st.selectbox("Bathrooms", sorted(df['bathroom'].unique())))
with col5:
    bhk = int(st.selectbox("BHK", sorted(df['configuration'].unique())))

# ── Section 3: Area ───────────────────────────────────────────────────────────
st.subheader("📐 Area Details")
col6, col7 = st.columns(2)
with col6:
    area = float(st.number_input("Total Area (sqft)", min_value=100.0, max_value=50000.0, value=1000.0, step=50.0))
with col7:
    area_type = st.selectbox("Area Type", sorted(df['area_type'].unique()))

# ── Section 4: Age ────────────────────────────────────────────────────────────
st.subheader("🏗 Property Age")
age = st.selectbox("Age / Possession Status", sorted(df['age_possession'].unique()))

st.divider()

# ── Predict Button ────────────────────────────────────────────────────────────
if st.button("⚡ Predict Price Range", use_container_width=True, type="primary"):
    data = [[sector, bedroom, bathroom, bhk, area, area_type, age, property_type]]
    one_df = pd.DataFrame(data, columns=df.columns)

    pred = np.expm1(pipeline.predict(one_df))[0]
    low  = pred - 0.5
    high = pred + 0.5

    # Result
    st.success(f"### 💰 Estimated Price: ₹{low:.2f} Cr — ₹{high:.2f} Cr")

    # Summary metrics
    st.subheader("📋 Your Input Summary")
    summary = {
        "Property Type": property_type,
        "Sector": sector,
        "Bedrooms": bedroom,
        "Bathrooms": bathroom,
        "BHK": bhk,
        "Area (sqft)": f"{area:,.0f}",
        "Area Type": area_type,
        "Property Age": age,
    }
    col_a, col_b = st.columns(2)
    for i, (k, v) in enumerate(summary.items()):
        with col_a if i % 2 == 0 else col_b:
            st.metric(label=k, value=v)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built by **Prince Kumar** · Data Scientist · [LinkedIn](https://www.linkedin.com/in/prince-datascientist) · [GitHub](https://github.com/prince-kumar-ds)")