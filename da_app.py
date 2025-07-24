import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Analysis App", layout="wide")

st.title("📊 Data Analysis Web App")
st.markdown("Upload your dataset (CSV) to get started.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    
    # Data preview
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Basic Info
    st.subheader("📈 Basic Statistics")
    st.write(df.describe())

    # Null values
    st.subheader("🧪 Missing Values")
    st.write(df.isnull().sum())

    # Correlation matrix
    st.subheader("📉 Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Select variable for histogram
    st.subheader("📊 Histogram")
    col = st.selectbox("Select Column for Histogram", df.select_dtypes(include='number').columns)
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    st.pyplot(fig)

    # Scatterplot
    st.subheader("📌 Scatter Plot")
    numeric_cols = df.select_dtypes(include='number').columns
    x = st.selectbox("X-axis", numeric_cols, key="scatter_x")
    y = st.selectbox("Y-axis", numeric_cols, key="scatter_y")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x], y=df[y], ax=ax)
    st.pyplot(fig)
