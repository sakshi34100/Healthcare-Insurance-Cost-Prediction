# 🏥 Healthcare Cost & Lifestyle Trend Analysis

## 📌 Problem Statement
Insurance companies face significant challenges in estimating fair and accurate premiums. Since lifestyle choices—such as smoking habits and BMI—can exponentially increase health risks, a one-size-fits-all pricing model is ineffective.

This project aims to **predict individual insurance charges** using demographic and health data to support **data-driven and personalized pricing strategies**.

---

## 📂 Dataset Description
**Source:** Medical Cost Personal Dataset (Kaggle)

### Features:
- **age**: Age of the primary beneficiary  
- **sex**: Insurance contractor gender (female, male)  
- **bmi**: Body Mass Index (ideal range: 18.5–24.9)  
- **children**: Number of children covered by health insurance  
- **smoker**: Smoking status (yes, no)  
- **region**: Residential area in the United States  
- **charges**: Individual medical costs billed by health insurance (**Target Variable**)

---

## 🛠 Project Workflow

### 1️⃣ Data Collection & Quality Assurance
- Identified and removed duplicate records *(reduced dataset from 1338 to 1337 rows)*  
- Used box plots to **identify and handle outliers** in BMI and insurance charges  
- Improved overall data quality by approximately **20%**  
- Applied **Label Encoding** to convert categorical variables into model-ready format  

---

### 2️⃣ Exploratory Data Analysis (EDA)
- **Key Insight:** Smokers incur significantly higher insurance premiums regardless of age  
- Used **Seaborn heatmaps** to visualize correlations between BMI, age, and insurance costs  

---

### 3️⃣ Model Evaluation Metrics
Regression models require more than just accuracy. The following metrics were used:

- **R² Score (Coefficient of Determination):** `0.8834`  
  - Explains **88.34% of the variance** in insurance charges  
- **MAE (Mean Absolute Error):**  
  - Indicates the average dollar amount by which predictions differ from actual values  

**Algorithm Used:**  
- Random Forest Regressor  
- Optimized from a Linear Regression baseline (**R² = 80.68%**)

---

## 🚀 How to Run the Project
Follow these steps to run the interactive Streamlit dashboard locally:

```bash


# Navigate to the project directory
cd healthcare-project

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
