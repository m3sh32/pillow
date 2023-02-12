# **Pillow**
A RESTful API Adventure.
## **Table of Contents**
* [About](#about)
* [Getting Started](#getting-started)
* [License](#license)
## **About**
Pillow is my very first experience with **REST APIs** and has helped me gain proficiency in other aspects of programming, such as **OOP** and the use of **Git**.

The project is split into 2 parts: an **API Client** and an **API Service**.

### What is a REST API?
To understand what a REST(Repersentational State Transfer) API or RESTful API is, we must first understand what an API is.

An Application Programming Interface(API) is a way for computers to communicate with each other programmatically to share resources between a client and server. To read more about APIs, consider looking [here](https://en.wikipedia.org/wiki/API)

A REST API is an API that also follows the following principles:
- **Client-Server** - In a REST API, the client and the server must be completely seperate.
- **Uniform Interfacing** - In a REST API, each resource on the server is uniquely identifiable, 
resources can be altered through their repersentations, messages from client to server and vice versa are self-descriptive, 
meaning that the messages contain all the information the recipient needs to fully understand the message. Another constraint on REST APIs is [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS).
- **Statelessness** - No previous information is stored by the server about the client in between requests.
- **Cacheability** - Resources on both server and client side should be cacheable.
- **Layered Systems** - Between the client and the API server there maybe multiple intermediary servers carrying out different functionality, however these must not alter the request or response to and from the API and the client should have no direct knowledge of intermediary servers. 

### What I did
The first part of my project: implementing an **API Client** for the [Congress API](https://api.congress.gov/)


## **Getting Started**
### API Client
Using the Git CLI, you can easily clone the pillow repo locally
```console
foo@bar:~$ gh repo clone m3sh32/pillow 
```

To use the client:
```{.py3 title="Using API Client" linenums="1"}
from src.client import Client
client = Client()
response = client.bills(117, 'hr', limit=1)
print(response)
```

Dependencies:
- Requests: https://pypi.org/project/requests/
- Python-Dotenv: https://pypi.org/project/python-dotenv/

## **License**
This code is made available under the MIT license.