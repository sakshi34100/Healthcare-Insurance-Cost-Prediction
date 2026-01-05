 Healthcare Cost & Lifestyle Trend Analysis
➕ A. Problem Statement
Insurance companies face significant challenges in estimating fair and accurate premiums. Since lifestyle choices—like smoking and BMI—can exponentially increase health risks, a one-size-fits-all pricing model doesn't work. This project aims to predict individual insurance charges using demographic and health data to ensure data-driven pricing.

➕ B. Dataset Description
Source: Medical Cost Personal Dataset (Kaggle)

Features: - age: Age of primary beneficiary.

sex: Insurance contractor gender (female, male).

bmi: Body mass index (ideal is 18.5 to 24.9).

children: Number of children covered by health insurance.

smoker: Smoking status (yes, no).

region: The beneficiary's residential area in the US.

charges: Individual medical costs billed by health insurance (Target Variable).

🛠 Project Workflow (Step-by-Step)
1️⃣ Data Collection & Quality Assurance
Identified and removed duplicate records (Reduced from 1338 to 1337 rows).

Used Box Plots to handle outliers in BMI and Charges, improving data quality by 20%.

Performed Label Encoding to make categorical data model-ready.

2️⃣ Exploratory Data Analysis (EDA)
Key Insight: Smokers pay significantly higher premiums regardless of age.

Used Seaborn Heatmaps to visualize correlations between BMI, age, and costs.

3️⃣ ➕ C. Model Evaluation Metrics
Regression models require more than just "accuracy." I used the following metrics to evaluate performance:

R² Score (Coefficient of Determination): 0.8834 (This means the model explains 88.34% of the variance in insurance costs).

MAE (Mean Absolute Error): Helps understand the average dollar amount the prediction is off by.

Algorithm Used: Random Forest Regressor (Optimized from a Linear Regression baseline of 80.68%).

➕ D. How to Run the Project (Step-by-Step) 🔥
Follow these steps to run the interactive dashboard on your local machine:

Clone the Repository: git clone https://github.com/your-username/healthcare-project.git

Navigate to the Folder: cd healthcare-project

Install Required Libraries: pip install -r requirements.txt

Launch the Dashboard: streamlit run app.py

📊 Key Business Insights
The Smoking Penalty: Smoking is the #1 predictor of high insurance costs.

BMI & Health Risk: A BMI over 30 combined with smoking creates a "high-risk" bracket.

Predictable Aging: Medical costs increase by a predictable margin every year.

💻 Tech Stack
Tools: Python (Pandas, NumPy, Scikit-learn)

Visuals: Seaborn, Matplotlib

Deployment: Streamlit Dashboard

