from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

bitcoin_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '1',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'cd599a62-2212-4cdd-b45a-a5dbb38a98ad',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(bitcoin_api_url, params=parameters)
    data = json.loads(response.text)
    # First we look at everything in 'data' and isolate the items in the 'quote' key which has an index of 0 in the list. Then, the price in USD is extracted from the list
    price = data['data'][0]['quote']['USD']['price']
    print(f'The current Bitcoin value is: ${int(price)}')
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
