# 💻 Laptop Price Predictor

A machine learning web application built with **Flask** that predicts the price of a laptop based on its specifications. The model is trained using a dataset of laptops with various configurations and prices.

---

## 🚀 Features

- Predicts laptop prices based on user input
- Uses a trained machine learning pipeline
- Clean and responsive UI with HTML/CSS
- Deployed locally using Flask

---

## 🧠 Tech Stack

- **Frontend**: HTML5, CSS3
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, numpy
- **Model**: Regression model saved as `pipe.pkl`

---

## 📊 Input Parameters

Users are required to input the following laptop features:
- Company
- Type of Laptop (e.g., Gaming, Ultrabook)
- RAM (in GB)
- Weight (in kg)
- Touchscreen (Yes/No)
- IPS Panel (Yes/No)
- Screen Resolution (e.g., 1920x1080)
- Screen Size (in inches)
- CPU Brand
- GPU Brand
- HDD Storage (in GB)
- SSD Storage (in GB)
- Operating System

---

## 📦 Project Structure
laptop-price-predictor/
├── app.py # Main Flask app
├── pipe.pkl # Trained ML pipeline (model)
├── df.pkl # DataFrame for dropdowns
├── templates/
│ └── index.html # HTML UI template
├── requirements.txt # Python dependencies
└── README.md


---

## 🚀 How to Run Locally

1. **Clone the repository**  
   ```bash
   git clone https://github.com/sunayana90/Laptop-Price-Prediction.git
   cd laptop-price-predictor
