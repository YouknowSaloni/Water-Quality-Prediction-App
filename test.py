# Import all the necessary libraries
import pandas as pd
import numpy as np
import joblib
import streamlit as st

# Load model and structure
model = joblib.load("pollution_model_compressed.pkl")
model_cols = joblib.load("model_columns.pkl")

# Page settings
st.set_page_config(page_title="Water Quality Predictor", layout="centered")

# -------------------------------
# 📲 Custom Branding Header
# -------------------------------
st.markdown("""
    <div style='text-align: center; padding: 10px 0; background-color: #e0f7fa; border-radius: 10px;'>
        <h1 style='color: #006064;'>💧 Water Quality Prediction App</h1>
        <h4 style='color: #00796b;'>Powered by Machine Learning | Developed by <a href='https://github.com/prilectro1098' target='_blank'>Pritam Saha</a></h4>
    </div>
""", unsafe_allow_html=True)

st.write("Predict the water pollutants based on **Year** and **Station ID**")

# -------------------------------
# Inputs
# -------------------------------
year_input = st.number_input("📅 Enter Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("🏷️ Enter Station ID", value='1')

# -------------------------------
# Prediction
# -------------------------------
if st.button('Predict'):
    if not station_id:
        st.warning('⚠️ Please enter a valid Station ID.')
    else:
        # Input Preparation
        input_df = pd.DataFrame({'year': [year_input], 'id': [station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]

        # Prediction
        predicted_pollutants = model.predict(input_encoded)[0]
        pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
        results_df = pd.DataFrame([predicted_pollutants], columns=pollutants)
        results_df.index = [f"Station {station_id}, Year {year_input}"]

        # -------------------------------
        # Display: Table
        # -------------------------------
        st.subheader("📊 Predicted Pollutant Levels (mg/L)")
        st.dataframe(results_df.style.highlight_max(axis=1))

        # -------------------------------
        # Display: Bar Chart
        # -------------------------------
        st.subheader("📉 Pollutant Levels - Bar Chart")
        chart_data = pd.DataFrame({
            'Pollutant': pollutants,
            'Concentration (mg/L)': predicted_pollutants
        })
        st.bar_chart(chart_data.set_index('Pollutant'))

        # -------------------------------
        # Download Button
        # -------------------------------
        csv = results_df.to_csv().encode('utf-8')
        st.download_button(
            label="⬇️ Download Prediction as CSV",
            data=csv,
            file_name=f'prediction_{station_id}_{year_input}.csv',
            mime='text/csv'
        )

        # -------------------------------
        # Info Popups
        # -------------------------------
        with st.expander("📘 What Do These Pollutants Mean?"):
            st.markdown("""
            - **O₂ (Dissolved Oxygen):** Essential for aquatic life. Low levels (<5 mg/L) can harm fish.
            - **NO₃ (Nitrate):** From fertilizers/sewage. Causes algal growth and health risks.
            - **NO₂ (Nitrite):** Toxic at low levels. Indicates pollution and nitrogen imbalance.
            - **SO₄ (Sulfate):** High levels affect taste, corrosive to pipes.
            - **PO₄ (Phosphate):** Promotes eutrophication and algal blooms.
            - **Cl (Chloride):** High chloride harms freshwater life and affects water taste.
            """)

        # -------------------------------
        # Pollution Alert System
        # -------------------------------
        st.subheader("⚠️ Pollution Alert Analysis")
        safe_limits = {
            'O2': 5,
            'NO3': 10,
            'NO2': 0.1,
            'SO4': 250,
            'PO4': 0.1,
            'CL': 250
        }

        alerts = []
        for pollutant, value in zip(pollutants, predicted_pollutants):
            limit = safe_limits[pollutant]
            if pollutant == 'O2' and value < limit:
                alerts.append(f"🔴 Low O₂: {value:.2f} mg/L (Safe ≥ {limit})")
            elif pollutant != 'O2' and value > limit:
                alerts.append(f"🔴 High {pollutant}: {value:.2f} mg/L (Safe ≤ {limit})")

        if alerts:
            st.error("⚠️ Some pollutant levels exceed safe limits:")
            for alert in alerts:
                st.markdown(f"- {alert}")
        else:
            st.success("✅ All predicted pollutant levels are within safe environmental limits.")

        # -------------------------------
        # 🎯 Pollution Severity Score
        # -------------------------------
        st.subheader("🎯 Pollution Severity Score")
        pollution_score = len(alerts)
        if pollution_score == 0:
            st.markdown("🟢 **Water Quality Status: GOOD**")
        elif pollution_score <= 2:
            st.markdown("🟡 **Water Quality Status: MODERATE**")
        else:
            st.markdown("🔴 **Water Quality Status: HAZARDOUS**")
        st.markdown(f"**Pollution Score:** {pollution_score} / {len(pollutants)}")

# -------------------------------
# Optional Footer (Optional)
# -------------------------------
st.markdown("""
---
<div style='text-align: center; color: gray;'>
    Created by <b>Pritam Saha</b> | <a href='https://github.com/prilectro1098' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)
