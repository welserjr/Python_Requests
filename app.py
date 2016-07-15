__author__ = 'WelserJr'

import requests


""" Make a Response """
# r = requests.get('https://api.github.com/events')

# r = requests.post("http://httpbin.org/post")
#
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")

""" Passing Parameters in URLs """
# # payload = {'key1': 'value1', 'key2': 'value2'}
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r)
# print(r.url)

""" Response Content """
# r = requests.get('https://api.github.com/events')
# print(r.text)
# print(r.encoding)

""" JSON Response Content """
# r = requests.get('https://api.github.com/events')
# print(r.json())

""" More complicated POST requests """
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
