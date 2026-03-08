# 🌸 Iris Flower Prediction — Streamlit App

A machine learning web application built with **Streamlit** to predict Iris flower species using a **pre-trained Random Forest model**.

This project demonstrates a complete ML workflow:
data preparation → model training → model deployment → user interaction.

---

## 🚀 Features
- Interactive UI using **Streamlit**
- Machine Learning model trained with **Scikit-learn**
- Real-time prediction
- Clean and minimal interface
- Ready for deployment (local or Streamlit Cloud)

---

## 🗂 Project Structure
```
.
├── app.py                # Streamlit application
├── iris_model.pkl        # Trained ML model
├── train_iris.ipynb      # Model training notebook
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Tech Stack
- Python 3.8+
- Streamlit
- Scikit-learn
- NumPy
- Joblib

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/your-username/iris-streamlit-app.git
cd iris-streamlit-app
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Make sure `iris_model.pkl` exists in the project folder.

```bash
streamlit run app.py
```

Open in browser:
```
http://localhost:8501
```

---

## 🧠 Model Details
- Dataset: Iris Dataset (Seaborn)
- Algorithm: Random Forest Classifier
- Features:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- Output Classes:
  - Setosa
  - Versicolor
  - Virginica

---

## 🧪 Model Training
Training is done using:
```
train_iris.ipynb
```

The notebook:
- Loads Iris dataset
- Splits training and testing data
- Trains Random Forest model
- Exports model as `iris_model.pkl`

---

## 📌 Notes
- Suitable for ML demo or portfolio project
- Easy to extend with:
  - Probability visualization
  - Model evaluation
  - Streamlit Cloud deployment

---

## 📄 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
Developed by **Your Name**  
Machine Learning & Data Science Enthusiast
