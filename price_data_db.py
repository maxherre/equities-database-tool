import sqlite3

import pandas as pd
import sqlalchemy
from sqlalchemy.sql.expression import table


def load_data_from_csv():
    # load .csv data for the AMEX exchange
    amex_data = pd.read_csv("amex_companies.csv")
    amex_data = amex_data[
        ["Name", "Symbol", "Country", "IPO Year", "Sector", "Industry"]
    ]

    # load .csv data for the NASDAQ exchange
    nasdaq_data = pd.read_csv("nasdaq_companies.csv")
    nasdaq_data = nasdaq_data[
        ["Name", "Symbol", "Country", "IPO Year", "Sector", "Industry;"]
    ]
    nasdaq_data["Industry"] = nasdaq_data["Industry;"]
    nasdaq_data.drop(columns="Industry;", inplace=True)

    # load .csv data for the NYSE exchange
    nyse_data = pd.read_csv("nyse_companies.csv")
    nyse_data = nyse_data[
        ["Name", "Symbol", "Country", "IPO Year", "Sector", "Industry;"]
    ]
    nyse_data["Industry"] = nyse_data["Industry;"]
    nyse_data.drop(columns="Industry;", inplace=True)

    # merge the three dataframes into one
    exchange_data = pd.concat([amex_data, nasdaq_data, nyse_data]).reset_index(
        drop=True
    )
    exchange_data["IPO_Year"] = exchange_data["IPO Year"]
    exchange_data.drop(columns="IPO Year", inplace=True)
    exchange_data["ID"] = exchange_data.index + 1
    return exchange_data


def create_connection():
    conn = None
    conn = sqlalchemy.create_engine(
        "sqlite:///C:/Users/maxhe/Documents/GitHub/nyseportfolio/equities.db"
    )
    return conn


def upload_data_to_db():
    conn = create_connection()
    data = load_data_from_csv()
    data[["Name", "Symbol", "Country", "Sector", "Industry", "IPO_Year", "ID"]].to_sql(
        "company_info", conn, if_exists="replace", index=False
    )
    print("Data successfully saved to database!")


def download_data_to_df():
    conn = create_connection()
    data = pd.read_sql_table(table_name="company_info", con=conn)
    return data
