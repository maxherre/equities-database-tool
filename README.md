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

3. Create the two PostgreSQL databases: `equities` and `equities_pricedata`. These are just plain standard databases, not special configuration required.

4. Save the connection strings for each database in environment variables: `POSTGRES_DB_EQUITIES` and `POSTGRES_DB_EQUITIES_PRICEDATA`. The connection strings should look like this:
   `postgresql+psycopg2://username:password@server/equities_pricedata` or this `postgresql+psycopg2://username:password@server/equities` depending on the database in question. Make sure to replace `username`, `password`, `server` with your own values.

5. Now you can execute the `price_data_db.py` scipt. The `equities` database will contain around 7550 tickers of which ca. 840 tickers will fail to download any data from Yahoo Finance. These failed tickers will be saved to a `missing.csv` file in the project folder.

6. **!!! IMPORTANT !!!** It takes around 2-3 hours for the script to complete. The terminal should give you an indication during the process how far along you are, but don't be in a hurry. :)

## Outlook

Here are some ideas I have for future functionality:

1. adding more data from some (european) exchanges.
2. adding an updater function to update existing tickers.
3. asynchronous data loading and storing.
5. create new databases with higher resolution data i.e intraday.
6. currently the tickers are imported from .csv files. I like to change that to fetch the tickers directly from some web source.
7. integration into a cloud platform (probably Microsoft Azure)
8. a proper wiki 

## Credit

I'd like to thank Alex Reed and Stuart Jamieson for providing excellent python/finance educational content for free to the world. Their work inspired this project and has taught me a ton. Go check them out!

**Alex:**
[LinkedIn](https://www.linkedin.com/in/alex-reed)
[GitHub](https://github.com/areed1192)

**Stuart:**
[LinkedIn](https://www.linkedin.com/in/stuart-jamieson)
[GitHub](https://github.com/Stuj79)
