import sys
import os
import http_helper as http

try:
    url = http.Url(sys.argv[1])
except IndexError:
    url = None

if url is None:
    print("Please provide a url")

print("getting:")
print(url)

document = http.Document(url)

document.render()