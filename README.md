# 🏥 Healthcare Cost & Lifestyle Trend Analysis

## 📌 Project Overview
This project is an **end-to-end data analysis solution** designed to identify key cost drivers in health insurance. By analyzing 1,300+ records, I developed a predictive model that estimates insurance charges based on individual health and lifestyle metrics.

---

## 🛠 Project Workflow (Step-by-Step)

I followed a standard **Data Science Lifecycle** to ensure the results are accurate, reliable, and business-ready:

### 1️⃣ Data Collection & Inspection
- **Source:** Public Healthcare Dataset.
- **Goal:** Understand the initial structure of the data (1,338 rows and 7 features including BMI, Smoking Status, and Age).

### 2️⃣ Data Cleaning (Quality Improvement)
- **Duplicate Removal:** Identified and removed duplicate entries to maintain data integrity.
- **Outlier Management:** Utilized **Box Plots** to detect and analyze extreme insurance charges.
- **Model Readiness:** Performed **Label Encoding** on categorical features (Sex, Smoker, Region) to transform them for machine learning compatibility.

### 3️⃣ Exploratory Data Analysis (EDA)
- **Correlation Discovery:** Used **Seaborn Heatmaps** to quantify relationships between variables.
- **Lifestyle Impact Visualization:** Created Bar Plots and Scatter Plots to demonstrate how smoking status and high BMI exponentially increase medical costs.
- **Key Insight:** Smoking was identified as the most significant factor affecting insurance premiums across all age groups.

### 4️⃣ Predictive Modeling
- **Baseline Model:** Developed a **Linear Regression** model as a benchmark (Accuracy: **80.68%**).
- **Optimization:** Implemented a **Random Forest Regressor** to capture complex non-linear patterns in the data.
- **Final Result:** Achieved a high prediction accuracy of **88.34%**.

### 5️⃣ Deployment (Interactive Dashboard)
- **Framework:** Built a web application using **Streamlit**.
- **Functionality:** Created a user-friendly interface where users can input personal metrics to receive real-time cost predictions from the trained model.

---

## 📊 Key Business Insights
* **The Smoking Penalty:** Smoking is the #1 predictor of high insurance costs, often tripling the premium compared to non-smokers.
* **BMI & Health Risk:** A BMI over 30 combined with smoking creates a "high-risk" bracket, resulting in the highest insurance premiums in the dataset.
* **Predictable Aging:** Medical costs show a steady, predictable increase with age, allowing for reliable long-term financial planning.

---

## 💻 Tech Stack
* **Languages:** Python 3.x
* **Analysis:** Pandas, NumPy
* **Visualizations:** Seaborn, Matplotlib
* **Machine Learning:** Scikit-learn
* **Web App:** Streamlit

---

## 📂 Project Structure
- `insurance.csv`: Raw dataset.
- `health_analysis.py`: Script for Data Cleaning, EDA, and Model Building.
- `app.py`: Streamlit dashboard code.
- `requirements.txt`: List of required Python libraries.
