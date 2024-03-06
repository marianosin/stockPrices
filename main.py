import pandas as pd
import yfinance as yf
import sqlite3

def create_database():
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('stocks.db')

    # Create a cursor object
    c = conn.cursor()

    # Create the stockNames table
    c.execute('''
        CREATE TABLE IF NOT EXISTS stockNames (
            stocId INTEGER PRIMARY KEY,
            symbol TEXT,
            security TEXT,
            sector TEXT,
            subSector TEXT,
            headquarters TEXT,
            dateAdded TEXT,
            cik TEXT,
            founded TEXT
        )
    ''')

    # Create the stockPrices table
    c.execute('''
        CREATE TABLE IF NOT EXISTS stockPrices (
            RECORDid INTEGER PRIMARY KEY,
            stockId INTEGER,
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            adjClose REAL,
            volume INTEGER,
            FOREIGN KEY(stockId) REFERENCES stockNames(stockId)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def download_sp500_companies():
    # Get the table of S&P 500 companies from Wikipedia
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    companies = table[0]
    # Rename to match db columns
    companies = companies.rename(columns={
        'Symbol': 'symbol' ,
        'Security': 'security',
        'GICS Sector': 'sector',
        'GICS Sub-Industry': 'subSector',
        'Headquarters Location': 'headquarters',
        'Date first added': 'dateAdded', 
        'CIK': 'cik', 
        'Founded': 'founded'
    })

    return companies
    


if __name__ == '__main__':

    #Create database if it doesn't exist
    create_database()

    download_sp500_companies()