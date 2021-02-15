import requests

url = "https://cdn.pixabay.com/photo/2015/06/08/15/02/pug-801826_960_720.jpg"
response = requests.get(url)
if response.status_code == 200:
    with open("/geekforgeeks/a.jpg", 'wb') as f:
        f.write(response.content)
