import requests
from src.requesters.requester_interface import RequesterInterface


class HTTPRequester(RequesterInterface):
    def make_request(self, full_path: str = "") -> str:
        json_object = requests.get(full_path).text
        return json_object
