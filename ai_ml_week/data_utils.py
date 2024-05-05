import pandas as pd
import re


def convert_to_billion(market_cap_str):
    """Convert market cap string to a numeric value in billions."""
    match = re.search(r'\$(\d+\.?\d*)\s*(B|T)', market_cap_str)
    if match:
        value, unit = match.groups()
        value = float(value)
        return value * 1000 if unit == 'T' else value
    return 0


def load_and_process_csv(file_path):
    """Load CSV file and process the 'Market Cap (USD)' column."""
    df = pd.read_csv(file_path, index_col=0)
    df['Market Cap (USD) Numerical'] = df['Market Cap (USD)'].apply(
        convert_to_billion)
    return df
