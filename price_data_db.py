import datetime
import os

import pandas as pd
import requests_cache
import sqlalchemy
import yfinance as yf
from requests.api import get
from sqlalchemy.sql.expression import table

# setting some global variables
equities_conn_string = str(os.environ["POSTGRES_DB_EQUITIES"])
equitiies_pricedata_conn_string = str(os.environ["POSTGRES_DB_EQUITIES_PRICEDATA"])

equities_engine = sqlalchemy.create_engine(equities_conn_string)
equities_pricedata_engine = sqlalchemy.create_engine(equitiies_pricedata_conn_string)

session = requests_cache.CachedSession("yfinance.cache")


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


def create_connection(database_name):
    equities_conn_string = str(os.environ["POSTGRES_DB_EQUITIES"])
    equitiies_pricedata_conn_string = str(os.environ["POSTGRES_DB_EQUITIES_PRICEDATA"])
    if database_name == "equities":
        equities_engine = sqlalchemy.create_engine(equities_conn_string)
        return equities_engine
    elif database_name == "equities_pricedata":
        equities_pricedata_engine = sqlalchemy.create_engine(
            equitiies_pricedata_conn_string
        )
        return equities_pricedata_engine
    else:
        print("please provide a valid database_name and try again!")


def tosql_equities_data():
    conn = create_connection(database_name="equities")
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


def download_and_tosql_equities_pricingdata():
    tickersList = download_data_to_df(
        database_name="equities", table_name="company_info"
    )["Symbol"].to_list()

    conn = create_connection(database_name="equities_pricedata")
    startdate = "1980-01-01"
    enddate = datetime.date.today()
    failures = []
    counter = 0
    for ticker in tickersList:
        try:
            frame = yf.Ticker(ticker, session=session).history(
                start=startdate, end=enddate, interval="1d"
            )
            frame.reset_index(drop=False, inplace=True)
            frame["last_update"] = datetime.date.today()
            frame.to_sql(ticker, conn, if_exists="replace", index=False)

            counter += 1
            print(counter)
        except Exception as e:
            failures.append(e)
            failures = pd.DataFrame(data=failures)
            failures.to_csv("failures.csv")


download_and_tosql_equities_pricingdata()
