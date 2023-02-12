# Welcome to Pillow

A RESTful API Adventure.
## **What is a REST API?**

An Application Programming Interface(API) is a way for computers to communicate with each other programmatically to share resources between a client and server. To read more about APIs, consider looking [here](https://en.wikipedia.org/wiki/API)

A REST(Repersentational State Transfer) API is an API that also follows the following principles:

- **Client-Server** - In a REST API, the client and the server must be completely seperate.
- **Uniform Interfacing** - In a REST API, each resource on the server is uniquely identifiable, resources can be altered through their repersentations, messages from client to server and vice versa are self-descriptive, 
meaning that the messages contain all the information the recipient needs to fully understand the message. Another constraint on REST APIs is [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS).
- **Statelessness** - No previous information is stored by the server about the client in between requests.
- **Cacheability** - Resources on both server and client side should be cacheable.
- **Layered Systems** - Between the client and the API server there maybe multiple intermediary servers carrying out different functionality, however these must not alter the request or response to and from the API and the client should have no direct knowledge of intermediary servers. 
### What I did
The first part of my project: implementing an **API Client** for the [Congress API](https://api.congress.gov/)

The second part of my project: implementing a basic API Service with AWS. The demo site is: https://f8m11ot12a.execute-api.us-east-1.amazonaws.com