import requests


api_key = 'Your api key'



def exchange(currency):
    url = f' https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/{currency}'
    req = requests.get(url)
    data = req.json()
    res = str(data['conversion_rate'])[:8]
    return res
    


