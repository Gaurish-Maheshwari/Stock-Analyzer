# Stock Price Analyzer

A lightweight and interactive web application built with Streamlit to analyze historical stock prices, returns, and trends for companies listed on both US and Indian stock exchanges. The app uses Yahoo Finance data and visualizes it in an intuitive format.

## Features

- Select from a list of popular US and Indian stocks or enter any custom ticker symbol.
- Choose a date range to fetch and analyze historical stock data.
- Interactive line plot of closing prices over the selected period.
- Key statistics including start price, end price, and percentage return.
- Expandable view to inspect raw historical data in tabular format.
- Responsive layout with sidebar controls for user inputs.
- Data caching for faster repeated queries.

## Tech Stack

- **Streamlit** – Frontend framework for building interactive data apps.
- **yFinance** – To fetch historical stock price data from Yahoo Finance.
- **Pandas** – For data manipulation and processing.
- **Matplotlib** – For visualizing stock trends via line plots.
- **Python** – Core programming language for logic and integration.

## Inputs

- **Stock Selection**: Dropdown menu of predefined tickers or custom ticker input (e.g., AAPL for Apple, RELIANCE.NS for Reliance).
- **Date Range**: Start and end date selectors to define the analysis period.

## Outputs

- **Line Chart**: Visualization of the stock's closing price trend.
- **Key Metrics**: Display of start price, end price, and overall return percentage.
- **Raw Data Table**: Expandable section showing the downloaded stock data.

## Example Ticker Formats

- US Stocks: `AAPL`, `MSFT`, `GOOGL`
- Indian Stocks (NSE): `RELIANCE.NS`, `TCS.NS`, `HDFCBANK.NS`
- Indian Stocks (BSE): `500325.BO`, `532174.BO`

## Getting Started

1. Download Dependencies
2. Create a Virtual Environment
3. Install requirements.txt
4. Run streamlit app from the terminal
    ```

## License

This project is open-source and free to use for educational and personal purposes.
