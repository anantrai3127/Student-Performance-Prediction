# Student Performance Prediction using Machine Learning

An end-to-end machine learning project that predicts a student's final grade (`G3`) using academic, demographic, family, social, and school-related information.

## Project Goal

The objective of this project is to build a regression model that predicts a student's final grade using **32 input features**.

The complete workflow is:

**Data → EDA → Preprocessing → Model Training → Cross-Validation → Model Comparison → Final Model → Evaluation → Prediction**

## Dataset

This project uses the **Student Performance Mathematics Dataset**.

The dataset contains:

- **395 students**
- **33 columns**
- **32 input features**
- **Target:** `G3` (final grade)

### Dataset Features

The model uses the following input features:

```text
school, sex, age, address, famsize, Pstatus, Medu, Fedu,
Mjob, Fjob, reason, guardian, traveltime, studytime, failures,
schoolsup, famsup, paid, activities, nursery, higher, internet,
romantic, famrel, freetime, goout, Dalc, Walc, health,
absences, G1, G2
```

### Target Variable

```text
G3
```

`G3` represents the student's final grade.

## Exploratory Data Analysis

The notebook includes:

- Dataset shape and structure
- Data type analysis
- Missing-value checking
- Descriptive statistics
- Final-grade distribution
- Correlation analysis
- Study time vs final grade
- Previous grades vs final grade
- Absences vs final grade
- Categorical feature relationships with `G3`

### Key Observation

Previous academic grades, particularly **`G2`**, have a strong relationship with the final grade `G3`.

This is expected because `G2` represents the student's performance in an earlier grading period.

## Preprocessing

The dataset contains both categorical and numerical features.

The preprocessing pipeline uses:

- `OneHotEncoder(handle_unknown="ignore")` for categorical features
- Numerical features passed through unchanged
- `ColumnTransformer`
- `Pipeline`

Keeping preprocessing inside the pipeline ensures that preprocessing is fitted correctly within each cross-validation fold and helps prevent data leakage.

## Models Compared

Five regression models were evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Tuned Decision Tree Regressor
4. Tuned Random Forest Regressor
5. Random Forest Regressor with 100 trees

## 5-Fold Cross-Validation Results

The following results were obtained from the original notebook:

| Model | Mean R² | R² Std | Mean MAE | Mean RMSE |
|---|---:|---:|---:|---:|
| Random Forest (100 trees) | **0.890** | 0.034 | 0.957 | **1.499** |
| Tuned Random Forest | 0.821 | 0.034 | 1.344 | 1.898 |
| Tuned Decision Tree | 0.808 | 0.055 | 1.217 | 1.954 |
| Linear Regression | 0.804 | 0.032 | 1.393 | 1.987 |
| Decision Tree | 0.792 | 0.084 | 1.070 | 2.012 |

### Model Comparison

The Random Forest model with 100 trees achieved the highest mean cross-validation R² of **0.890** and the lowest RMSE of **1.499** among the models tested.

## Selected Model

The final model selected for the project is:

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

The complete model, including preprocessing, is saved using `joblib`.

## Final Test Results

The selected model was evaluated on a separate held-out test set.

| Metric | Score |
|---|---:|
| R² | **0.803** |
| MAE | **1.209** |
| RMSE | **2.009** |

An **MAE of approximately 1.21** means that the model's predictions are off by about **1.21 grade points on average** on the held-out test data.

### Cross-Validation vs Test Performance

The cross-validation R² of **0.890** and the test-set R² of **0.803** are calculated using different data.

- **0.890 R²:** Mean performance across 5 cross-validation folds
- **0.803 R²:** Performance on the separate held-out test set

Therefore, these values are not expected to be identical.

## Important Finding

The earlier academic grades are highly informative for predicting the final grade.

In the Decision Tree feature-importance analysis from the notebook:

```text
G2        ≈ 0.825
absences  ≈ 0.175
```

This means that `G2` was the most important feature in that particular Decision Tree analysis.

Because `G1` and `G2` are included as input features, this project should be understood as predicting **final academic performance when earlier-period grades are already available**.

## Prediction Function

The project includes a reusable `predict_student()` function.

The function validates:

- Missing feature names
- Extra or unknown feature names
- Missing values
- Invalid numerical values
- Correct feature order

The student data is then passed through the complete preprocessing and Random Forest pipeline to generate the predicted final grade.

## Project Structure

The project is organized as follows:

```text
Student_Performance_Prediction/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── student-mat.csv
├── model_comparison.png
├── final_model.pkl
└── Student_Performance_Prediction_Final.ipynb
```

## How to Run

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Student_Performance_Prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Open Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
Student_Performance_Prediction_Final.ipynb
```

### 4. Run the Notebook

Run all cells in order.

The notebook performs:

- Data loading
- Exploratory Data Analysis
- Data preprocessing
- Model training
- Cross-validation
- Model comparison
- Final model training
- Model evaluation
- Student grade prediction

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## Machine Learning Concepts Practiced

- Exploratory Data Analysis
- Correlation Analysis
- Train-Test Split
- Categorical Data Preprocessing
- One-Hot Encoding
- Regression
- Linear Regression
- Decision Trees
- Random Forest
- Hyperparameter Tuning
- Five-Fold Cross-Validation
- R²
- MAE
- RMSE
- Scikit-learn Pipelines
- ColumnTransformer
- Feature Importance
- Model Persistence
- Prediction on New Data

## Future Improvements

Possible future improvements include:

- Trying additional regression algorithms
- More systematic hyperparameter tuning
- Testing the workflow on a larger dataset
- Building a Streamlit prediction interface
- Deploying the trained model
- Comparing performance when `G1` and `G2` are excluded

## Author

**Anant Rai**

Artificial Intelligence & Machine Learning Student
