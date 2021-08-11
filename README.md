# Equities Database Project

## Table of Content

- [Overview](#overview)
- [Setup and Usage](#setupandusage)
- [Outlook](#outlook)

## Overview

Current Version: **0.0.1**

The purpose of this tool is to download and store daily price data for all tickers on the **NYSE** and **NASDAQ**.
While there are many free APIs available to source this data from, these approaches are always reliant on a working internet connection and limited by whatever criteria the API provider has set. This can result in unavailable data or slow connectivity.
With this tool you can build your own database and store as much data as needed from as many sources as you'd like. For free :)

## Setup and Usage

1. You can either download a .zip folder of this project and save it to your computer or use the `git clone` command in Git Bash.

```console
$ git clone https://github.com/maxisui/equities-database-tool.git
```

2. Either way, once downloaded you should run the `setup.py` first to make sure you have all relevant dependencies installed on your machine or in your virtual environment.

3. Create the two PostgreSQL databases: `equities` and `equities_pricedata`.

4. Save the connection strings for each database in environment variables: `POSTGRES_DB_EQUITIES` and `POSTGRES_DB_EQUITIES_PRICEDATA`. The connection strings should look like this:
   `postgresql+psycopg2://username:password@server/equities_pricedata` or this `postgresql+psycopg2://username:password@server/equities` depending on the database in question. Make sure to replace `username`, `password`, `server` with your own values.

5. Now you can execute the `price_data_db.py` scipt. The `equities` database will contain around 7550 tickers of which ca. 840 tickers will fail to download any data from Yahoo Finance. These failed tickers will be saved to a `missing.csv` file in the project folder.

6. **!!! IMPORTANT !!!** It takes around 2-3 hours for the script to complete. The terminal should give you an indication during the process how far along you are, but don't be in a hurry. :)

## Outlook

Here are some ideas I have had for future functionality:

1. adding data from some european exchanges in the future.

2. adding an updater function to get more recent data added to existing databases.

3. create a new database with higher resolution data i.e intraday.

4.

5.
