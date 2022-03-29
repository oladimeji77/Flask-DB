import requests

# Where USD is the base currency you want to use
url = 'http://api.exchangeratesapi.io/v1/latest?access_key=30ed49bc78023f2a1e8632ff0519445b&symbols=USD,GBP,AUD,JPY,CNY'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print (data)