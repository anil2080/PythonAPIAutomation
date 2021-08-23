import requests


response = requests.get('https://reqres.in/api/users', params={'page':2}, )
print(response.text)
print(response.status_code)