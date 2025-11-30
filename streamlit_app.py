import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Power Analysis", layout="wide")

st.title("🔆 Solar Power Generation Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("solarpower.csv")
    return df

df = load_data()

st.subheader("📌 Dataset Preview")
st.dataframe(df.head())

# Missing values
st.subheader("📌 Missing Values")
st.write(df.isnull().sum())

# Summary statistics
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# Select column to plot
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

if len(numeric_cols) > 0:
    st.subheader("📈 Time Series Plot")
    col = st.selectbox("Select a column to visualize", numeric_cols)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df[col])
    ax.set_title(f"{col} Over Time")
    ax.set_xlabel("Index")
    ax.set_ylabel(col)
    st.pyplot(fig)
else:
    st.warning("No numeric columns found for plotting.")
