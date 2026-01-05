import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset Load
df = pd.read_csv('insurance.csv')

# 2. Duplicate Check & remove
print(f"before Cleaning total rows: {len(df)}")
df = df.drop_duplicates()
print(f"after removing Duplicate  total rows: {len(df)}")

# 3. Missing Values Check
print("\nKhali cells (Missing values):")
print(df.isnull().sum())

# 4. Data Quality Check (Outliers)
#  BMI  boxplot banayenge to check  abnormal values
plt.figure(figsize=(8,5))
sns.boxplot(x=df['bmi'], color='skyblue')
plt.title('Checking Outliers in BMI')
plt.show()

# 1. Smoking  (Bar Plot)
plt.figure(figsize=(7,5))
sns.barplot(x='smoker', y='charges', data=df, palette='magma')
plt.title('Smokers vs Non-Smokers ka Kharcha')
plt.show()

# 2. Age (Scatter Plot)
plt.figure(figsize=(8,6))
sns.scatterplot(x='age', y='charges', hue='smoker', data=df)
plt.title('Age vs Charges (Smoker ke saath)')
plt.show()

# 3. Correlation Heatmap

numeric_df = df.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix (Kaun kisse juda hai?)')
plt.show()

from sklearn.preprocessing import LabelEncoder

#  encoder machine
le = LabelEncoder()

# 1. Sex column  (0 aur 1 mein)
df['sex'] = le.fit_transform(df['sex'])

# 2. Smoker column (yes=1, no=0)
df['smoker'] = le.fit_transform(df['smoker'])

# 3. Region column
df['region'] = le.fit_transform(df['region'])

print("\nafter Encoding :")
print(df.head())

# Ab hum data ko Feature (X) aur Target (y) mein divide karenge
X = df.drop(['charges'], axis=1) # Charges ko chhod kar baaki sab "Features" hain
y = df['charges'] # Sirf Charges hamara "Target" hai jise predict karna hai

print("\nFeatures (X) ke pehle 5 rows:")
print(X.head())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Data Split (80% seekhne ke liye, 20% test karne ke liye)
#  'charges' prediction
X = df.drop(['charges'], axis=1) # Sab columns except charges
y = df['charges'] # Sirf charges column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Linear Regression Model banana
model = LinearRegression()

# 3. Model ko train karna (Data khilana)
model.fit(X_train, y_train)

# 4. Prediction karna (Test data par)
y_pred = model.predict(X_test)

# 5. Accuracy (R-squared Score) check karna
accuracy = r2_score(y_test, y_pred)
print(f"\nModel  Accuracy (R2 Score): {accuracy * 100:.2f}%")


from sklearn.ensemble import RandomForestRegressor

# 1. Random Forest Model  (Isme 100 chote-chote trees hote hain)
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# 2. Model train
rf_model.fit(X_train, y_train)

# 3. Prediction
y_pred_rf = rf_model.predict(X_test)

# 4.  Accuracy check
rf_accuracy = r2_score(y_test, y_pred_rf)
print(f"Random Forest  Accuracy: {rf_accuracy * 100:.2f}%")


# Model  importance
importances = rf_model.feature_importances_
feature_names = X.columns

# Graph
plt.figure(figsize=(8,6))
sns.barplot(x=importances, y=feature_names)
plt.title('which factor cause highest cost?')
plt.show()