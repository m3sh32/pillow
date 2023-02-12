# API Client Examples
Accessing 
```{.py3 title="HTTP Request with HTTP Library" linenums="1"}
import http.client
path = '/v3/bill/117/hr/3076/?api_key=' + api_key
connection = http.client.HTTPSConnection(host='api.congress.gov') # Opens a connection to the host
connection.request(method='GET', url='/v3/bill/117/hr/?limit=1') # Client sends HTTP Request with GET method
response = connection.getresponse()
response_body = response.read()
connection.close() # Connection closed
print(response_body)
```

```{.py3 title="Server JSON Response" linenums="1"}
b'{\n    "bills": [\n        {\n            "congress": 118,\n            "latestAction": {\n                "actionDate": "2023-02-10",\n                "text": "Referred to the 
Subcommittee on Economic Development, Public Buildings, and Emergency Management."\n            },\n            "number": "964",\n            "originChamber": "House",\n 
           "originChamberCode": "H",\n            "title": "To direct the Administrator of General Services to ensure that the design of public buildings in the United States adheres to the guiding principles for Federal architecture, and for other purposes.",\n            "type": "HR",\n            "updateDate": "2023-02-11",\n            
           "updateDateIncludingText": "2023-02-11T08:13:55Z",\n            "url": "https://api.congress.gov/v3/bill/118/hr/964?format=json"\n        }\n    ],\n    "pagination": 
           {\n        "count": 392689,\n        "next": "https://api.congress.gov/v3/bill?offset=1&limit=1&format=json"\n    },\n    "request": {\n        "contentType": "application/
           json",\n        "format": "json"\n    }\n}'
```

!!! note "API Key"
    The HTTP request does not contain an API Key, so the response from the server will be a 403 error. To get your own API Key for the Congress API, take a look [here](https://api.congress.gov/sign-up/).

Making HTTP requests to an API this way takes too much time; with my API Client, this process is a lot simpler.

```{.py3 title="HTTP Request with Pillow" linenums="1"}
from src.client import Client
client = Client()
response = client.bills(117, 'hr', limit=1)
print(response)
```

```{.py3 title="Server JSON Response"}
{'bills': [
{'congress': 117, 
'latestAction': {'actionDate': '2023-01-05', 'text': 'Became Public Law No: 117-329.'}, 
'number': '897', 
'originChamber': 'House', 
'originChamberCode': 'H', 
'title': 'Agua Caliente Land Exchange Fee to Trust Confirmation Act', 
'type': 'HR', 
'updateDate': '2023-02-10',
'updateDateIncludingText': '2023-02-10T00:41:12Z', 'url': 'https://api.congress.gov/v3/bill/117/hr/897?format=json'}
],
'pagination': {'count': 9698, 'next': 'https://api.congress.gov/v3/bill/117/hr?sort=&offset=1&limit=1&format=json'}, 
'request': {'billType': 'hr', 
'congress': '117', 
'contentType': 'application/json', 
'format': 'json'}
}
```