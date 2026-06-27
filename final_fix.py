import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time

def robust_aapl_download():
    """Robust AAPL data download with multiple fallback methods"""
    
    print("Attempting to download AAPL data...")
    
    # Method 1: Try with current date
    try:
        end = datetime.now()
        start = datetime(2015, 1, 1)
        
        # Add retry logic
        for attempt in range(3):
            print(f"Attempt {attempt + 1}...")
            df = yf.download('AAPL', start=start, end=end, progress=False)
            
            if not df.empty:
                print(f"✅ Success! Downloaded {len(df)} rows")
                print(df.head())
                df.to_csv('AAPL_working_data.csv')
                return df
                
            time.sleep(2)
            
    except Exception as e:
        print(f"Method 1 failed: {e}")
    
    # Method 2: Try shorter date range
    try:
        print("Trying shorter date range...")
        end = datetime.now()
        start = end - timedelta(days=365*2)  # Last 2 years
        
        df = yf.download('AAPL', start=start, end=end, progress=False)
        if not df.empty:
            print(f"✅ Success with shorter range! Downloaded {len(df)} rows")
            df.to_csv('AAPL_working_data.csv')
            return df
            
    except Exception as e:
        print(f"Method 2 failed: {e}")
    
    # Method 3: Try period parameter
    try:
        print("Trying period parameter...")
        ticker = yf.Ticker("AAPL")
        df = ticker.history(period="5y")
        
        if not df.empty:
            print(f"✅ Success with period! Downloaded {len(df)} rows")
            df.to_csv('AAPL_working_data.csv')
            return df
            
    except Exception as e:
        print(f"Method 3 failed: {e}")
    
    # Method 4: Try max period
    try:
        print("Trying max period...")
        ticker = yf.Ticker("AAPL")
        df = ticker.history(period="max")
        
        if not df.empty:
            print(f"✅ Success with max period! Downloaded {len(df)} rows")
            df.to_csv('AAPL_working_data.csv')
            return df
            
    except Exception as e:
        print(f"All methods failed: {e}")
    
    return None

if __name__ == "__main__":
    df = robust_aapl_download()
    if df is not None:
        print("\nData successfully downloaded and saved to AAPL_working_data.csv")
    else:
        print("\n❌ All download attempts failed. This may be a temporary Yahoo Finance API issue.")
        print("Please try again in a few minutes or check your internet connection.")
