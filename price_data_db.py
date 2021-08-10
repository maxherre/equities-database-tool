import datetime
import sqlite3

import investpy
import pandas as pd
import sqlalchemy
from requests.api import get
from sqlalchemy.sql.expression import table

equity_database = str("equities.db")
equities_price_database = str("equities_price.db")


def load_data_from_csv():

    # load .csv data for the NASDAQ exchange
    nasdaq_data = pd.read_csv("nasdaq_companies.csv")
    nasdaq_data = nasdaq_data[
        ["Name", "Symbol", "Country", "IPO Year", "Sector", "Industry;"]
    ]
    nasdaq_data["Industry"] = nasdaq_data["Industry;"]
    nasdaq_data.drop(columns="Industry;", inplace=True)
    nasdaq_data["Exchange"] = "nasdaq"

    # load .csv data for the NYSE exchange
    nyse_data = pd.read_csv("nyse_companies.csv")
    nyse_data = nyse_data[
        ["Name", "Symbol", "Country", "IPO Year", "Sector", "Industry;"]
    ]
    nyse_data["Industry"] = nyse_data["Industry;"]
    nyse_data.drop(columns="Industry;", inplace=True)
    nyse_data["Exchange"] = "nyse"

    # merge the three dataframes into one
    exchange_data = pd.concat([nasdaq_data, nyse_data])
    exchange_data["IPO_Year"] = exchange_data["IPO Year"]
    exchange_data.drop(columns="IPO Year", inplace=True)
    # exchange_data.dropna(axis="rows", inplace=True)
    exchange_data["ID"] = exchange_data.index + 1
    return exchange_data


def create_connection(name):
    conn = None
    conn = sqlalchemy.create_engine("sqlite:///" + name)
    return conn


def upload_data_to_db():
    conn = create_connection(equity_database)
    data = load_data_from_csv()
    data[
        [
            "Name",
            "Symbol",
            "Country",
            "Sector",
            "Industry",
            "IPO_Year",
            "Exchange",
            "ID",
        ]
    ].to_sql("company_info", conn, if_exists="replace", index=False)
    print("Data successfully saved to database!")


def download_data_to_df(database_name, table_name):
    data = pd.read_sql_table(
        table_name=table_name, con=create_connection(database_name)
    )
    return data


def download_and_store_pricing_data():
    with open("logfile.txt", "w") as log:

        try:
            tickersList = download_data_to_df(
                database_name=equity_database, table_name="company_info"
            )["Symbol"].to_list()

            countryList = download_data_to_df(
                database_name=equity_database, table_name="company_info"
            )["Country"].to_list()

            conn = create_connection(equities_price_database)
            date = "{}/{}/{}".format(
                datetime.date.today().day,
                datetime.date.today().month,
                datetime.date.today().year,
            )

            counter = 0
            for ticker in tickersList:
                frame = investpy.get_stock_historical_data(
                    stock=ticker, from_date="01/01/1980", to_date=date
                ).reset_index(drop=False, inplace=True)

                frame[
                    ["Date", "Open", "High", "Low", "Close", "Volume", "Currency"]
                ].to_sql(ticker, conn, if_exists="replace", index=False)
                counter += 1
                print(counter)
        except Exception as e:
            log.write("Failed to download {0}: {1}\n".format(str(ticker), str(e)))
            pass


download_and_store_pricing_data()
