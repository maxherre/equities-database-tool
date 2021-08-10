# Equities Database Project

## Table of Content

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Outlook](#outlook)

## Overview

Current Version: **0.0.1**

The purpose of this tool is to download and store daily price data for all tickers on the NYSE and NASDAQ.
While there are many free APIs available to source this data from, these approaches are always reliant on a working internet connection and limited by whatever criteria the API provider has set. This can result in unavailable data or slow connectivity, which slows down the entire process downstream.
With this tool the user can build their own database and store as much data as needed.

## Setup

You can either download a .zip fodler of this project and save it to your computer or use the `git clone` command in Git Bash.

```console
$ git clone https://github.com/maxisui/nyseportfolio.git
```

Either way, once downloaded you should run the `setup.py` first to make sure you have all relevant dependencies installed on your machine or in your virtual environment.

**IMPORTANT**
Before running the `price_data_db.py` script you need to create two PostgreSQL databases and save both connection strings to environment variables called `POSTGRES_DB_EQUITIES` and `POSTGRES_DB_EQUITIES_PRICEDATA`. The connection strings should look like this: `postgresql+psycopg2://username:password@server/equities_pricedata` for the equities database and `postgresql+psycopg2://username:password@server/equities`. Make sure to replace `username`, `password`, `server` with your own values.

## Usage

Once setup is complete, using the script is very straight forward. Just execute the `price_data_db.py` script and let it run. In total the equities database will contain ca. 7545 ticker symbols and typically around 840 tickers will fail to download any data. All failed tickers will be saved to a `missing.csv` file in the project directory. **Keep in mind that it takes ca. 2.5 hours to run the script**

## Outlook

Here are some ideas I have had for future functionality:

1. adding data from some european exchanges in the future.

2. adding an updater function to get more recent data added to existing databases.

3. create a new database with higher resolution data.
