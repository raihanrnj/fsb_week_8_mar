
import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Iris Prediction App", layout="centered")

# Sidebar
st.sidebar.title("🌸 About This App")
st.sidebar.write("""
This app predicts the species of an Iris flower based on its measurements using a trained Machine Learning model.

**Features:**
- Sepal Length & Width
- Petal Length & Width
- Real-time prediction
""")

st.title("🌸 Website Prediksi Bunga Iris")
st.markdown("### Predict iris species using trained ML model")
st.markdown("---")

try:
    model = joblib.load("iris_model.pkl")
except FileNotFoundError:
    st.error("Model file 'iris_model.pkl' not found. Please ensure the model is trained and saved.")
    st.stop()

# Create two columns for sliders
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1, 0.1)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5, 0.1)

with col2:
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4, 0.1)
    petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2, 0.1)

st.markdown("---")

if st.button("🔮 Predict Species", type="primary"):
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(data)[0]
    st.success(f"🌼 Predicted Species: **{prediction}**")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit and Machine Learning*")
