import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

st.set_page_config(page_title="Stock Price Analyzer", layout="wide")

# --------------------
# Predefined Stock List
# --------------------
stock_dict = {
    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "Amazon (AMZN)": "AMZN",
    "Google (GOOGL)": "GOOGL",
    "Tesla (TSLA)": "TSLA",
    "Meta (META)": "META",
    "Nvidia (NVDA)": "NVDA",
    "Netflix (NFLX)": "NFLX",
    "Infosys (INFY.NS)": "INFY.NS",
    "TCS (TCS.NS)": "TCS.NS",
    "Reliance (RELIANCE.NS)": "RELIANCE.NS",
    "HDFC Bank (HDFCBANK.NS)": "HDFCBANK.NS",
    "ICICI Bank (ICICIBANK.NS)": "ICICIBANK.NS",
    "Axis Bank (AXISBANK.NS)": "AXISBANK.NS",
    "SBI (SBIN.NS)": "SBIN.NS"
}

st.title("Stock Price Analyzer")
st.markdown("Analyze historical stock prices, returns, and trends with a simple interface.")

# --------------------
# Sidebar Inputs
# --------------------
st.sidebar.header("Select a Stock")

selected_name = st.sidebar.selectbox("Choose from list:", list(stock_dict.keys()))
selected_symbol = stock_dict[selected_name]

custom_symbol = st.sidebar.text_input("Or enter custom ticker (optional)", value="")
final_symbol = custom_symbol.strip().upper() if custom_symbol else selected_symbol

start_date = st.sidebar.date_input("Start Date", value=date.today() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", value=date.today())

# --------------------
# Data Fetching
# --------------------
@st.cache_data
def fetch_stock_data(symbol, start, end):
    df = yf.download(symbol, start=start, end=end)
    return df

try:
    df = fetch_stock_data(final_symbol, start_date, end_date)

    if df.empty:
        st.warning("No data found. Please check the ticker symbol or date range.")
    else:
        st.subheader(f"📉 Price Trend: {final_symbol}")
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(df.index, df["Close"], color="green", label="Close Price")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (₹ / $)")
        ax.set_title(f"Closing Price Over Time for {final_symbol}")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

        st.subheader("📈 Key Statistics")
        start_price = float(df["Close"].iloc[0])
        end_price = float(df["Close"].iloc[-1])
        return_pct = ((end_price - start_price) / start_price) * 100

        col1, col2, col3 = st.columns(3)
        col1.metric("Start Price", f"{start_price:.2f}")
        col2.metric("End Price", f"{end_price:.2f}")
        col3.metric("Return (%)", f"{return_pct:.2f}%")

        with st.expander("🔎 View Raw Data"):
            st.dataframe(df.reset_index(), use_container_width=True)

except Exception as e:
    st.error(f"Error fetching stock data: {e}")
