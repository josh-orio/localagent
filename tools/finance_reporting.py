import yfinance as yf
import json


def fetch_ticker_data(ticker: str) -> dict:
    """Fetches Open, Close, High, Low, and daily volatility for a given ticker."""
    try:
        # Fetch historical data for the last 2 days to calculate daily volatility
        data = yf.download(ticker, period="2d")
        if data.empty:
            return {"error": f"No data found for ticker: {ticker}"}

        # Get the most recent closing price and the previous day's closing price
        close_prices = [p[0] for p in data["Close"].values.tolist()]

        # print(data)
        # print("---")
        # print(data["Close"])
        # print("---")
        # print(close_prices)

        if len(close_prices) < 2:
            return {
                "error": f"Insufficient data points for volatility calculation for ticker: {ticker}"
            }

        # Calculate daily volatility (simple difference between the last two closing prices)
        # A more robust volatility calculation would involve standard deviation, but for simplicity, we use the daily range.
        latest_close = close_prices[-1]
        previous_close = close_prices[-2]
        daily_volatility = (
            abs(latest_close - previous_close) / previous_close * 100
            if previous_close != 0
            else 0.0
        )

        # Get OHLC from the most recent day's data
        latest_day = data.iloc[-1]

        return {
            "ticker": ticker,
            "open": round(float(latest_day["Open"].values[0]), 3),
            "close": round(float(latest_day["Close"].values[0]), 3),
            "high": round(float(latest_day["High"].values[0]), 3),
            "low": round(float(latest_day["Low"].values[0]), 3),
            "daily_volatility": round(daily_volatility, 3),
        }

    except Exception as e:
        return {"error": f"An error occurred while fetching data for {ticker}: {e}"}


def fetch_ticker_news(ticker: str) -> str:
    """Fetches recent news for a given ticker using yfinance (limited capability)."""
    try:
        ticker_obj = yf.Ticker(ticker)

        # Fetch and parse news articles
        news = ticker_obj.get_news(count=5, tab="news")
        # print(json.dumps(news,indent=4))
        if news:
            news_list = [
                {
                    "title": item["content"]["title"],
                    "summary": item["content"]["summary"],
                    "source": item["content"]["provider"]["displayName"],
                    "url": item["content"]["canonicalUrl"]["url"],
                }
                for item in news
            ]

            return news_list

        return f"No recent news found for {ticker} via yfinance."

    except Exception as e:
        return f"Error fetching news for {ticker}: {e}"


def get_ticker_summary(ticker: str) -> dict:
    """Combines fetching financial data and news for a ticker."""
    financial_data = fetch_ticker_data(ticker)
    news_data = fetch_ticker_news(ticker)

    return json.dumps({"financial_data": financial_data, "news": news_data})


__all__ = ["get_ticker_summary"]


if __name__ == "__main__":
    tickers = ["AAPL", "GOOGL", "MSFT"]
    for ticker in tickers:
        print(f"--- Processing {ticker} ---")
        summary = get_ticker_summary(ticker)
        print(json.dumps(summary, indent=4))
        # print(f"Financial Data: {summary['financial_data']}")
        # print("Financial Data: "+ json.dumps(summary['financial_data'], indent=4))
        # # print(f"News: \n{summary['news']}\n")
        # print("News: "+ json.dumps(summary['news'], indent=4))
