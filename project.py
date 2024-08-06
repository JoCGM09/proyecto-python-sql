# Manejo de API
import requests

url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
payload = {'name':'Blue-Eyes White Dragon'}
r = requests.get(url, params=payload)

print(r.text)
