import investpy
import datetime

today = datetime.date.today()
date = "{}/{}/{}".format(today.day, today.month, today.year)

df = investpy.get_stock_historical_data(
    stock="PG", country="United States", from_date="01/01/1980", to_date=date
)
df.reset_index(drop=False, inplace=True)
print(df)
