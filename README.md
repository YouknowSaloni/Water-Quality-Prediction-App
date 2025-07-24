# 💧 Water Quality Prediction App

A machine learning-based Streamlit web application that predicts **concentrations of key water pollutants** like O₂, NO₃, NO₂, SO₄, PO₄, and Cl based on the **year** and **station ID**. The app also provides visualizations, pollution alert flags, and a severity score to evaluate water safety.

## 📌 Features

- 📅 Predict water pollutants using **year** and **station ID**
- 📊 Visualize predicted concentrations in a **table** and **bar chart**
- ⚠️ Highlight pollutants that exceed **safe environmental limits**
- 🎯 Compute a **Pollution Severity Score** for quick assessment
- 📁 Download prediction results as a **CSV**
- 🧾 Informative popups to explain the meaning of each pollutant

## 📂 Project Structure

├── test.py # Main Streamlit app
├── Waterqualityprediction.ipynb # Notebook for data preprocessing, training, and evaluation
├── pollution_model_compressed.pkl # Compressed ML model
├── model_columns.pkl # Encoded model input feature names
├── README.md # Project documentation

## ⚙️ How It Works

1. User inputs `Year` and `Station ID`
2. App encodes inputs and feeds them to a pre-trained model
3. Model predicts pollutant concentrations (O₂, NO₃, etc.)
4. App displays results and flags any health/safety violations


## 🧪 Machine Learning Model

- **Model Used**: [Mention the algorithm here, e.g., Random Forest Regressor]
- **Features**: Year, Encoded Station ID
- **Targets**: O₂, NO₃, NO₂, SO₄, PO₄, Cl
- **Libraries**: `pandas`, `numpy`, `scikit-learn`, `joblib`, `streamlit`

## 📈 Results

- Model shows strong predictive ability on unseen station/year pairs.
- Integrated **Pollution Alert System** improves environmental awareness.
- Delivers clear, actionable insights for water quality monitoring.

---

## 🔮 Future Scope

- 🌐 Integrate real-time water monitoring sensor data via APIs
- 🗺️ Add geolocation-based station mapping
- 🤖 Improve model accuracy with ensemble methods
- 📉 Include time-series trend prediction (e.g., forecast next 5 years)
- 📲 Deploy app for mobile users and NGOs involved in water safety


## 📚 References

- Central Pollution Control Board (CPCB) reports
- WHO Guidelines for Drinking-Water Quality
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)


## 🙌 Acknowledgements

Special thanks to my mentors and peers who supported this project during my internship.

& here is the drive link of the pkl file of pollution model 

https://drive.google.com/file/d/1LNX6E3enXoJaO_zJhch_TgSkFdpxQjVQ/view?usp=sharing
