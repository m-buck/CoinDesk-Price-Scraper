from datetime import datetime, timedelta
import requests
import json

CoinDesk_base_url = 'http://api.coindesk.com/v1/bpi/'
current_price_url = "{}currentprice.json".format(CoinDesk_base_url)
day_change_url = 'https://api.coinmarketcap.com/v2/ticker/?convert=BTC&limit=1'
time_format = '%Y-%m-%d'
date_format = '%m-%d'

# Create dates
today = datetime.now()
last_year = datetime.strftime(today - timedelta(days=365), time_format)
last_year2 = datetime.strftime(today - timedelta(days=366), time_format)
last_month = datetime.strftime(today - timedelta(days=32), time_format)
last_week = datetime.strftime(today - timedelta(days=8), time_format)

historic_price_url = "{}historical/close.json?start={}&end={}".format(
    CoinDesk_base_url,
    last_year2,
    last_year,)
month_price_url = "{}historical/close.json?start={}&end={}".format(
    CoinDesk_base_url,
    last_month,
    datetime.strftime(today, time_format))
week_price_url = "{}historical/close.json?start={}&end={}".format(
    CoinDesk_base_url,
    last_week,
    datetime.strftime(today, time_format))

# Query CoinDesk Current price API
current_price_response = requests.get(current_price_url).json()
# Query CoinDesk historical API
historic_price_response = requests.get(historic_price_url).json()
# Query CoinDesk historical API
month_price_response = requests.get(month_price_url).json()
# Query CoinDesk historical API
week_price_response = requests.get(week_price_url).json()

current_price = "$" + str(round(current_price_response['bpi']['USD']['rate_float'], 2))
historic_price = "$" + str(round(historic_price_response['bpi'][last_year], 2))
month_price = "$" + str(round(month_price_response['bpi'][last_month], 2))
week_price = "$" + str(round(week_price_response['bpi'][last_week], 2))

print "Current price: " + str(current_price)
print "Last week's price: " + str(week_price)
print "Last month's price: " + str(month_price)
print "Last year's price: " + str(historic_price)

#coindesk json fetch
url = "https://api.coindesk.com/v1/bpi/historical/close.json"
data = requests.get(url).json()
day_change = requests.get(day_change_url).json()
day_change = str(day_change["data"]["1"]["quotes"]["USD"]["percent_change_24h"])
day_change = day_change  +"%"
print "24hr change: " + day_change
count = 32
prices = "["
days = "["
while count > 1:	
	day = datetime.strftime(today - timedelta(days=count), time_format)	
	price = round(month_price_response['bpi'][day], 2)
	prices = prices + str(price) + ","
	day = datetime.strftime(today - timedelta(days=count), date_format)
	days = days + "\""+str(day)+"\"" + ","
	#print ('{} {}'.format(day, price))
	count = count - 1
prices = prices[:-1]
days = days[:-1]
prices = prices + "]"
days = days + "]"
print prices
print days