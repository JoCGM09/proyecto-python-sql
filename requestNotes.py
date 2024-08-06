## Manejo de la librería request
import requests

url = 'https://xkcd.com/353/'

r = requests.get(url)

## Código de respuesta HTTP
print(r.status_code)

## Conetenido de la página en HTML
print(r.text)

## Descargar una imagen
imgurl = 'https://imgs.xkcd.com/comics/python.png'
image = requests.get(imgurl)

### este comando creará el arhivo image.png y escribirá en formato web binary el contenido de la imagen
with open('image.png', 'wb') as f:
    f.write(image.content)

## obtener información de los headers de la página en formato json

print(r.headers)

## para pasar parámetros en el URL puedes crear un diccionario llamado payload
## 

payload = {'page': 2, 'count': 25}
req = requests.get('https://httpbin.org/get', params=payload)
