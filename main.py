import pandas as pd
import yfinance as yf

def download_sp500_companies_data():
    # Get the table of S&P 500 companies from Wikipedia
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    companies = table[0]
    print(companies.columns)


if __name__ == '__main__':
    download_sp500_companies_data()