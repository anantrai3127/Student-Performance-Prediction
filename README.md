# Student Performance Prediction using Machine Learning

An end-to-end machine learning project that predicts a student's final grade (`G3`) from academic, demographic, family, social, and school-related information.

## Project Goal

The objective is to build a regression model that predicts a student's final grade using **32 input features**.

The workflow is:

**Data → EDA → Preprocessing → Model Training → Cross-Validation → Model Comparison → Final Model → Evaluation → Prediction**

## Dataset

The project uses the **Student Performance** mathematics dataset.

The original dataset contains:

- **395 students**
- **33 columns**
- **32 input features**
- Target: `G3` (final grade)

### Dataset Included

The actual `student-mat.csv` file is included in this GitHub-ready package inside the `data/` folder. No separate dataset download is required to run the notebook.

The notebook expects the file at `../data/student-mat.csv`.

## Features

The model uses:

`school`, `sex`, `age`, `address`, `famsize`, `Pstatus`, `Medu`, `Fedu`, `Mjob`, `Fjob`, `reason`, `guardian`, `traveltime`, `studytime`, `failures`, `schoolsup`, `famsup`, `paid`, `activities`, `nursery`, `higher`, `internet`, `romantic`, `famrel`, `freetime`, `goout`, `Dalc`, `Walc`, `health`, `absences`, `G1`, `G2`

Target:

`G3`

## Exploratory Data Analysis

The notebook covers:

- Dataset shape and structure
- Data types
- Missing-value checking
- Descriptive statistics
- Final-grade distribution
- Correlation analysis
- Study time vs final grade
- Previous grades vs final grade
- Absences vs final grade
- Several categorical relationships with `G3`

A key observation from the original analysis is that previous grades, particularly `G2`, are strongly related to `G3`.

## Preprocessing

The dataset contains categorical and numerical features.

The pipeline uses:

- `OneHotEncoder(handle_unknown="ignore")` for categorical features
- Numerical features passed through unchanged
- `ColumnTransformer`
- `Pipeline`

Keeping preprocessing inside the pipeline ensures it is fitted separately during cross-validation.

## Models Compared

Five regression models were evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Tuned Decision Tree Regressor
4. Tuned Random Forest Regressor
5. Random Forest Regressor with 100 trees

## 5-Fold Cross-Validation Results

Results from the original notebook:

| Model | Mean R² | R² Std | Mean MAE | Mean RMSE |
|---|---:|---:|---:|---:|
| **Random Forest (100 trees)** | **0.890** | 0.034 | **0.957** | **1.499** |
| Tuned Random Forest | 0.821 | 0.034 | 1.344 | 1.898 |
| Tuned Decision Tree | 0.808 | 0.055 | 1.217 | 1.954 |
| Linear Regression | 0.804 | 0.032 | 1.393 | 1.987 |
| Decision Tree | 0.792 | 0.084 | 1.070 | 2.012 |

### Selected Model

**Random Forest Regressor with 100 trees**

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

## Final Test Results

The selected model achieved the following results on the held-out test set:

| Metric | Score |
|---|---:|
| **R²** | **0.803** |
| **MAE** | **1.209** |
| **RMSE** | **2.009** |

An MAE of about 1.21 means that the model's predictions are off by about 1.21 grade points on average.

## Important Finding

The earlier academic grades are highly informative for predicting the final grade.

In the original notebook's Decision Tree feature-importance analysis:

- `G2` importance ≈ **0.825**
- `absences` importance ≈ **0.175**

Because `G1` and `G2` are included as inputs, this model should be described as predicting final performance **when earlier-period grades are already available**.

## Prediction Function

The project includes a reusable `predict_student()` function.

It validates:

- Missing feature names
- Extra/unknown feature names
- Missing values
- Invalid numerical values
- Correct feature order

Then it sends the student data through the complete preprocessing + Random Forest pipeline.

## Project Structure

```text
Student_Performance_Prediction/
│
├── data/
│   ├── README.md
│   └── student-mat.csv              # included dataset
│
├── notebooks/
│   └── Student_Performance_Prediction_Final.ipynb
│
├── models/
│   └── final_model.pkl               # trained final model
│
├── images/
│   └── model_comparison.png
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Student_Performance_Prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Open Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/Student_Performance_Prediction_Final.ipynb
```

### 4. Run all cells

The notebook trains the models, evaluates them, trains the final model, and saves:

```text
models/final_model.pkl
```

## Technologies

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
- Correlation analysis
- Train-test split
- Categorical preprocessing
- One-Hot Encoding
- Regression
- Linear Regression
- Decision Trees
- Random Forest
- Hyperparameter tuning
- Five-fold cross-validation
- R²
- MAE
- RMSE
- Pipelines
- Feature importance
- Model persistence
- Prediction on new data

## Future Improvements

- Try additional regression algorithms.
- Perform more systematic hyperparameter tuning.
- Test the workflow on a larger dataset.
- Build a Streamlit prediction interface.
- Deploy the model.
- Compare performance when `G1` and `G2` are excluded.

## Author

**Anant Rai**

Artificial Intelligence & Machine Learning Student
