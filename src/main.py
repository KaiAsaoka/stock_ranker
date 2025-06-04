import numpy as np
import yfinance as yf

from finvizfinance.screener.overview import Overview

def get_top_gainers():
    """
    Fetches a list of top gainer stock tickers from Finviz.
    Returns a list of tickers.
    """
    try:
        foverview = Overview()
        foverview.set_filter(signal='Top Gainers')
        df = foverview.screener_view(verbose=0)

        if not df.empty and 'Ticker' in df.columns:
            return df['Ticker'].tolist()
        else:
            print("Could not retrieve top gainers or 'Ticker' column not found.")
            return []

    except Exception as e:
        print(f"An error occurred while fetching top gainers: {e}")
        return []


if __name__ == "__main__":
    print("Fetching top gainers from Finviz...")
    top_gainers_tickers = get_top_gainers()

    if top_gainers_tickers:
        print("\nTop Gainer Tickers:")

        if len(top_gainers_tickers) > 0:

            try:
                top10 = top_gainers_tickers[:10]
                tickers_data = yf.Tickers(top10)
                hist_data = yf.download(top10, period="1mo")

                for ticker_symbol in top10:
                        stock_data = yf.Ticker(ticker_symbol)
                        print(f"\n--- {ticker_symbol} ---")
                        print(f"Name: {stock_data.info.get('shortName')}")
                        print(f"Current Price: {stock_data.info.get('currentPrice')}")
                        print(f"Day Change %: {stock_data.info.get('regularMarketChangePercent') * 100:.2f}%")
                        hist = stock_data.history(period="2d")

                        if not hist.empty and len(hist) >= 1:
                            today_open = hist['Open'].iloc[-1]
                            today_close = hist['Close'].iloc[-1]
                            change_percent = ((today_close - today_open) / today_open) * 100
                            print(f"Today's Open: {today_open:.2f}, Today's Close: {today_close:.2f}, Change: {change_percent:.2f}%")
                        else:
                            print("Could not fetch sufficient historical data for today's change.")
                        print(tickers_data.tickers[ticker_symbol].info)
                print(hist_data.head())

            except Exception as e:
                print(f"Could not fetch data for {ticker_symbol} using yfinance: {e}")            
    else:
        print("No top gainer tickers were found.")
