import requests
import not_requests

requests.get('https://gmail.com', timeout=60)
requests.get('https://gmail.com', timeout=None)
requests.get('https://gmail.com', timeout=5)
requests.post('https://gmail.com', timeout=60)
requests.post('https://gmail.com', timeout=None)
requests.post('https://gmail.com', timeout=5)
requests.put('https://gmail.com', timeout=60)
requests.put('https://gmail.com', timeout=None)
requests.put('https://gmail.com', timeout=5)
requests.delete('https://gmail.com', timeout=60)
requests.delete('https://gmail.com', timeout=None)
requests.delete('https://gmail.com', timeout=5)
requests.patch('https://gmail.com', timeout=60)
requests.patch('https://gmail.com', timeout=None)
requests.patch('https://gmail.com', timeout=5)
requests.options('https://gmail.com', timeout=60)
requests.options('https://gmail.com', timeout=None)
requests.options('https://gmail.com', timeout=5)
requests.head('https://gmail.com', timeout=60)
requests.head('https://gmail.com', timeout=None)
requests.head('https://gmail.com', timeout=5)

# Okay
not_requests.get('https://gmail.com')
