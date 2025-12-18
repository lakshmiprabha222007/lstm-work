import streamlit as st
import pandas as pd
from scipy import stats

st.title("📊 Student Performance Analysis")

# Upload CSV file
uploaded_file = st.file_uploader("Upload Student Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.write(df.head())

    # Select marks column
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) > 0:
        marks_col = st.selectbox("Select Marks Column", numeric_cols)

        st.subheader("📈 Statistical Analysis")

        mean = df[marks_col].mean()
        median = df[marks_col].median()
        mode = stats.mode(df[marks_col], keepdims=True)[0][0]

        st.write("Mean (Average):", mean)
        st.write("Median:", median)
        st.write("Mode:", mode)

        st.subheader("📉 Marks Distribution")
        st.bar_chart(df[marks_col])
    else:
        st.warning("No numeric columns found in dataset")
