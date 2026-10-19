# 🎓 Student Performance AI

An end-to-end machine learning application that predicts a student's final academic performance using demographic, family, academic, lifestyle, and previous performance data.

The project uses a trained machine learning pipeline and provides an interactive **Streamlit web application** for making predictions.

---

## 🚀 Live Application

The application is built with **Streamlit** and can be run locally to interact with the trained model.

---

## 📌 Project Overview

The goal of this project is to predict the student's **final grade (G3)** on a scale of **0–20**.

The application takes **32 student features** as input and passes them through the trained preprocessing and machine learning pipeline.

### 🎯 Prediction Target

**G3 — Final Grade**

The model estimates the student's final academic performance based on the information provided.

---

## 🖥️ Application Screenshots

### 🏠 Prediction Dashboard

![Prediction Dashboard](images/dashboard.png)

### 📝 Student Information & Inputs

![Student Input Form](images/input-form.png)

### 🎯 Prediction Result

![Prediction Result](images/prediction-result.png)

### 📈 Performance Snapshot

![Performance Chart](images/performance-chart.png)

### 🤖 About the Model

![About Model](images/about-model.png)

### 🔄 Machine Learning Pipeline

![Machine Learning Pipeline](images/ml-pipeline.png)

---

## ⚙️ How the Application Works

The application follows an end-to-end machine learning workflow:

```text
Student Information
        ↓
Data Preprocessing
        ↓
Trained ML Pipeline
        ↓
G3 Prediction
        ↓
Performance Interpretation
```

### 1. Student Input

The user enters information such as:

- School
- Age
- Gender
- Family information
- Mother's and father's education
- Study time
- Past failures
- Educational support
- Absences
- G1 grade
- G2 grade
- Lifestyle information

### 2. Preprocessing

The trained preprocessing pipeline handles the numerical and categorical features and converts them into the format required by the machine learning model.

### 3. Machine Learning Model

The processed student data is passed to the saved model:

```text
models/final_model.pkl
```

### 4. Prediction

The model predicts the student's final **G3 grade** on a scale from **0 to 20**.

The application also displays:

- Grade out of 20
- Equivalent score out of 10
- Percentage
- Performance category
- Performance gauge
- G1 vs G2 vs predicted G3 chart

---

## 📊 Example Prediction

For example, a student with:

| Feature | Value |
|---|---:|
| G1 | 19 |
| G2 | 18 |
| Absences | 5 |
| Study Time | 2/4 |
| Past Failures | 0 |

can receive a predicted final grade such as:

```text
Predicted G3 = 18.84 / 20
Percentage   = 94.2%
Category     = Excellent Performance
```

> Note: The prediction is an estimate produced by the trained machine learning model.

---

## 🧠 Machine Learning Workflow

The project follows these major steps:

```text
Dataset
   ↓
Exploratory Data Analysis
   ↓
Data Preprocessing
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Selection
   ↓
Final Model
   ↓
Streamlit Application
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data analysis |
| Scikit-learn | Machine learning |
| Joblib | Saving/loading trained model |
| Streamlit | Web application |

---

## 📁 Project Structure

```text
Student-Performance-Prediction/
│
├── data/
│   └── student-mat.csv
│
├── images/
│   ├── dashboard.png
│   ├── input-form.png
│   ├── prediction-result.png
│   ├── performance-chart.png
│   ├── about-model.png
│   └── ml-pipeline.png
│
├── models/
│   └── final_model.pkl
│
├── notebooks/
│   └── Student_Performance_Prediction_Final.ipynb
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Student-Performance-Prediction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

The project dependencies are listed in:

```text
requirements.txt
```

Main libraries include:

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
joblib
```

---

## 🎯 Project Features

- ✅ 32 student input features
- ✅ Numerical and categorical preprocessing
- ✅ Trained machine learning pipeline
- ✅ Final G3 grade prediction
- ✅ 0–20 grading scale
- ✅ Percentage conversion
- ✅ Performance classification
- ✅ Visual performance gauge
- ✅ G1/G2/G3 comparison chart
- ✅ Interactive Streamlit interface
- ✅ Separate About Model page
- ✅ Saved model for reusable predictions

---

## 📚 Dataset

This project uses the **Student Performance dataset** containing information about students' demographic, social, family, academic, and lifestyle characteristics.

The final grade **G3** is used as the prediction target.

---

## ⚠️ Disclaimer

This project is developed for **educational and portfolio purposes**.

The predictions are estimates generated by a machine learning model and should not be treated as definitive assessments of a student's future academic performance.

---

## 👨‍💻 Author

**Anant Rai**

AI/ML Student  
GGSIPU

---

⭐ If you found this project useful, consider giving the repository a star!