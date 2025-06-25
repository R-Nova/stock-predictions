import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("?? Google Stock Price Viewer")

uploaded_file = st.file_uploader("Upload a CSV file of stock prices", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("First 5 Rows of Your Data")
    st.write(df.head())

    if 'Close' in df.columns:
        st.subheader("?? Closing Price Over Time")
        fig, ax = plt.subplots()
        ax.plot(df['Close'], label='Close Price', color='blue')
        ax.set_xlabel("Time (days)")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)
    else:
        st.warning("No 'Close' column found in the CSV file.")
else:
    st.info("Please upload a CSV file to see the stock chart.")
