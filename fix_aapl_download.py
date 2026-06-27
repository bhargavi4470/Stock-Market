import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def download_aapl_data():
    """
    Download AAPL stock data with proper date range handling
    """
    
    # Use realistic date range (up to today)
    start = '2015-01-01'
    end = datetime.now().strftime('%Y-%m-%d')  # Today's date
    
    print(f"Downloading AAPL data from {start} to {end}")
    
    try:
        # Download with error handling
        df = yf.download(
            'AAPL',
            start=start,
            end=end,
            progress=True,
            auto_adjust=True,
            threads=True
        )
        
        if df.empty:
            print("Warning: No data returned. Trying alternative method...")
            # Try using period instead of start/end
            ticker = yf.Ticker("AAPL")
            df = ticker.history(period="max")
        
        print(f"Successfully downloaded {len(df)} rows of AAPL data")
        print("\nFirst 5 rows:")
        print(df.head())
        
        # Save to CSV for backup
        df.to_csv('AAPL_stock_data.csv')
        print("\nData saved to AAPL_stock_data.csv")
        
        return df
        
    except Exception as e:
        print(f"Error downloading data: {str(e)}")
        print("Trying with shorter date range...")
        
        # Try last 2 years as fallback
        fallback_start = (datetime.now() - timedelta(days=730)).strftime('%Y-%m-%d')
        fallback_end = datetime.now().strftime('%Y-%m-%d')
        
        try:
            df = yf.download('AAPL', start=fallback_start, end=fallback_end)
            print(f"Fallback successful: downloaded {len(df)} rows")
            return df
        except Exception as e2:
            print(f"Fallback also failed: {str(e2)}")
            return None

if __name__ == "__main__":
    df = download_aapl_data()
