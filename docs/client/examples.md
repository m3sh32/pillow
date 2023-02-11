# API Client Examples
Accessing 
```{.py3 title="HTTP Request with HTTP Library" linenums="1"}
import http.client
path = '/v3/bill/117/hr/3076/?api_key=' + api_key
connection = http.client.HTTPSConnection(host='api.congress.gov') # Opens a connection to the host
connection.request(method='GET', url='/v3/bill/117/hr/3076') # Client sends HTTP Request with GET method
response = connection.getresponse()
response_body = response.read()
connection.close() # Connection closed
```
!!! note "API Key"
    The HTTP request does not contain an API Key, so the response from the server will be a 403 error. To get your own API Key for the Congress API, take a look [here](https://api.congress.gov/sign-up/).