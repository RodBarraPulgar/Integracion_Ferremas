import requests

def get_usd_value():
    try:
        response = requests.get('https://mindicador.cl/api')
        data = response.json()
        return data['dolar']['valor']
    except Exception as e:
        print(f"Error fetching USD value: {e}")
        return None

def convert_price_to_clp(price_usd):
    usd_value = get_usd_value()
    if usd_value is not None:
        return price_usd * usd_value
    else:
        return None