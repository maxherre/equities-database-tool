import pycountry

code = "AU"

country = pycountry.countries.get(alpha_2=code)
currency = pycountry.currencies.get(numeric=country.numeric)
currency_code = currency.alpha_3
print(country)
print(currency)
