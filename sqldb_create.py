import io
from sqlite3.dbapi2 import Row
from numpy.core import numeric
import requests
import os

import sqlite3
import pycountry
import pandas as pd
import numpy as np

from sqlite3 import Error


def create_server_connection(database_name):
    conn = None
    try:
        conn = sqlite3.connect(database_name)
        conn.execute("PRAGMA foreign_key = 1")
        return conn
    except Error as error:
        print(error)
    return conn


def create_table(conn, create_table):
    try:
        c = conn.cursor()
        c.execute(create_table)
    except Error as error:
        print(error)


db_name = "nyse_database.db"


def main():
    database = db_name

    create_exchange_table = """ CREATE TABLE IF NOT EXISTS exchange (
                                    id integer ,
                                    name text NOT NULL,
                                    code text NOT NULL UNIQUE,
                                    country text NOT NULL,
                                    country_code text,
                                    PRIMARY KEY(id)
                                ); """

    create_company_table = """ CREATE TABLE IF NOT EXISTS company (
                                    cik integer ,
                                    name text NOT NULL,
                                    industry text,
                                    sector text,
                                    security_id integer,
                                    PRIMARY KEY(cik),
                                    FOREIGN KEY(security_id ) REFERENCES security(id)  
                                );"""

    create_security_table = """ CREATE TABLE IF NOT EXISTS security (
                                    id integer,
                                    ticker text NOT NULL UNIQUE,
                                    name text NOT NULL,
                                    company_cik integer,
                                    exchange_id integer,
                                    PRIMARY KEY(id)
                                    FOREIGN KEY(company_cik) REFERENCES company(cik)
                                    FOREIGN KEY(exchange_id) REFERENCES exchange(id)
                                );"""

    create_security_price_table = """ CREATE TABLE IF NOT EXISTS security_price (
                                        id integer,
                                        date text NOT NULL,
                                        open decimal NOT NULL,
                                        high decimal NOT NULL,
                                        low decimal NOT NULL,
                                        close decimal NOT NULL,
                                        volume integer,
                                        adj_close decimal NOT NULL,
                                        security_id integer,
                                        PRIMARY KEY(id),
                                        FOREIGN KEY(security_id) REFERENCES security(id)
                                    );"""
    conn = create_server_connection(database)

    if conn is not None:
        create_table(conn, create_exchange_table)
        create_table(conn, create_company_table)
        create_table(conn, create_security_table)
        create_table(conn, create_security_price_table)
    else:
        print("Creating th database connection or the tables failed!!")


main()

# load the list of stock exchanges
exchange_data = pd.read_csv(
    "https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.csv",
    encoding="iso-8859-1",
)

# select the relevant columns
exchange_data = exchange_data[
    [
        "COUNTRY",
        "ISO COUNTRY CODE (ISO 3166)",
        "MIC",
        "NAME-INSTITUTION DESCRIPTION",
    ]
]

# rename the selected columns
exchange_data.rename(
    columns={
        "ISO COUNTRY CODE (ISO 3166)": "country_code",
        "MIC": "code",
        "NAME-INSTITUTION DESCRIPTION": "name",
        "COUNTRY": "country",
    },
    inplace=True,
)

# create a new "id" column and fill with the index of each row
exchange_data["id"] = exchange_data.index

# insert exchange_data dataframe into database
conn = sqlite3.connect(db_name)

exchange_data[["id", "name", "code", "country", "country_code"]].to_sql(
    "exchange", conn, if_exists="append", index=False
)
