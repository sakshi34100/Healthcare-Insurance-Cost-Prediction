import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Page Configuration
st.set_page_config(page_title="Healthcare Cost Predictor", layout="wide")

# App Title and Description
st.title("🏥 Healthcare Insurance Cost Prediction Dashboard")
st.markdown("""
This interactive dashboard analyzes the impact of lifestyle habits on medical insurance costs and 
predicts future charges using a **Random Forest Regression** model.
""")


# Load Dataset
@st.cache_data
def load_data():
    data = pd.read_csv('insurance.csv')
    data = data.drop_duplicates()
    return data


df = load_data()

# Sidebar: User Input for Prediction
st.sidebar.header("User Demographics & Habits")


def user_input_features():
    age = st.sidebar.slider("Age", 18, 100, 30)
    bmi = st.sidebar.number_input("BMI (Body Mass Index)", 15.0, 50.0, 25.0)
    children = st.sidebar.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])
    smoker = st.sidebar.selectbox("Smoking Status", ["yes", "no"])
    sex = st.sidebar.selectbox("Gender", ["male", "female"])
    region = st.sidebar.selectbox("Region", df['region'].unique())

    data = {
        'age': age,
        'sex': 1 if sex == 'male' else 0,
        'bmi': bmi,
        'children': children,
        'smoker': 1 if smoker == 'yes' else 0,
        'region': region  # Placeholder for encoding
    }
    return pd.DataFrame(data, index=[0])


input_df = user_input_features()


# Model Training
@st.cache_resource
def train_model(data):
    le = LabelEncoder()
    temp_df = data.copy()
    for col in ['sex', 'smoker', 'region']:
        temp_df[col] = le.fit_transform(temp_df[col])

    X = temp_df.drop('charges', axis=1)
    y = temp_df['charges']
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model, le


rf_model, encoder = train_model(df)

# Prediction Logic
st.sidebar.markdown("---")
if st.sidebar.button("Predict Insurance Charges"):
    # Encoding region for prediction
    # Simple mapping for demo purposes
    region_map = {val: i for i, val in enumerate(df['region'].unique())}
    input_df['region'] = input_df['region'].map(region_map)

    prediction = rf_model.predict(input_df)
    st.sidebar.subheader("Result:")
    st.sidebar.success(f"Estimated Cost: ${prediction[0]:,.2f}")

# Main Section: Data Visualizations
st.header("Exploratory Data Analysis (EDA)")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Impact of Smoking on Charges")
    fig1, ax1 = plt.subplots()
    sns.barplot(x='smoker', y='charges', data=df, palette='viridis', ax=ax1)
    ax1.set_xlabel("Smoker")
    ax1.set_ylabel("Average Charges ($)")
    st.pyplot(fig1)

with col2:
    st.subheader("Age vs. Insurance Charges")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(x='age', y='charges', hue='smoker', data=df, ax=ax2)
    ax2.set_xlabel("Age")
    ax2.set_ylabel("Charges ($)")
    st.pyplot(fig2)

# Display Raw Data
if st.checkbox("Show Raw Dataset"):
    st.dataframe(df)