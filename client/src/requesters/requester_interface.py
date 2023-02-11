import abc


class RequesterInterface(abc.ABC):
    """
    This is an abstract base class for the HTTPRequester
    """

    @abc.abstractmethod
    def make_request(self, full_path: str = "") -> str:
        return ""
