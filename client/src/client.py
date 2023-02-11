from src.handlers.bill_handler import BillHandler
from src.requesters.http_requester import HTTPRequester
from dotenv import load_dotenv  # type: ignore
from os import getcwd, getenv
import re
import json
from src.typings.bill_typings import Bill
from src.typings.bills_typings import Bills


class Client:
    """
    A class that facilitates the user to make requests to api.congress.gov

    Attributes
    ----------
        host : str
            Always https://api.congress.gov/v3/.

        Requester : HTTPRequester
            Assigns the HTTPRequester class to the constructor to prevent multiple instantiation.

        api_key : str = ""
            Api key for congress api, default is to load the value from an environment variable file in the cwd, otherwise it can be passed into the constructor.

    Methods
    -------
        bill(congress: int | None = None, bill_type: str | None = None, bill_number: int | None = None, start_date: str | None = None, end_date: str | None = None, date_ascending: str | None = None) -> Bill
            Takes multiple parameters to construct a GET request to api.congress.gov and gets back a bill.

    """

    def __init__(self, api_key: str | None = None) -> None:
        """
        The constructor for the Client class.

        Parameters
        ----------
            host : str
                Always https://api.congress.gov/v3/.
            Requester : HTTPRequester
                Assigns the HTTPRequester class to the constructor to prevent multiple instantiation.
            api_key : str = ""
                Api key for congress api, default is to load the value from an environment variable file in the cwd, otherwise it can be passed into the constructor.

        """
        self.host = "https://api.congress.gov/v3/"  # TODO deal with part of the path that is in the host
        # TODO Fix the environment variable option
        if api_key == None:
            load_dotenv(getcwd())
            self.api_key = getenv("API_KEY", "")
        else:
            self.api_key = api_key
        self.Requester = HTTPRequester

    @staticmethod
    def __validate_query_parameters(  # TODO Complete query parameter validation
        start_date: str | None,
        end_date: str | None,
        date_order: str | None,
        offset: int | None,
        limit: int | None,
    ):
        if (
            start_date != None
            and re.search(
                pattern="[1-9][0-9][0-9][0-9]/([0][1-9]|[1][0-2])/([1-2][0-9]|[0][1-9]|[3][0-1])",
                string=start_date,  # type: ignore
            )
            == None
        ):
            raise ValueError(
                "Incorrect value entered as start_date, please enter start_date in a YYYY/MM/DD format"
            )
        if (
            end_date != None
            and re.search(
                pattern="[1-9][0-9][0-9][0-9]/([0][1-9]|[1][0-2])/([1-2][0-9]|[0][1-9]|[3][0-1])",
                string=end_date,  # type: ignore
            )
            == None
        ):
            raise ValueError(
                "Incorrect value entered as end_date, please enter start_date in a YYYY/MM/DD format"
            )
        if date_order != None and (date_order in ["asc", "desc"]) == False:
            raise ValueError("Incorrect value for date_order, please enter asc or desc")
        if offset != None and isinstance(offset, int) == False:  # type: ignore
            raise ValueError("Incorrect value for offset, please enter an integer")

    def __query_parameters(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        date_order: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> dict[str, str]:
        Client.__validate_query_parameters(
            start_date, end_date, date_order, offset, limit
        )
        start_date_param = ""
        end_date_param = ""
        date_order_param = ""
        offset_param = ""
        limit_param = ""
        if start_date != None:
            start_date_param = str(start_date)
        if end_date != None:
            end_date_param = str(end_date)
        if date_order != None:
            date_order_param = str(date_order)
        if offset != None:
            offset_param = str(offset)
        if limit != None:
            limit_param = str(limit)
        return {
            "fromDateTime": start_date_param + "T00:00:00Z",
            "toDateTime": end_date_param + "T00:00:00Z",
            "sort": date_order_param,
            "offset": offset_param,
            "limit": limit_param,
        }

    def __make_request(self, url: str) -> str:
        return self.Requester().make_request(url)

    def __deserialize_json(self, JSON: str):
        return json.loads(JSON)

    def bills(
        self,
        congress: int | None = None,
        bill_type: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        date_order: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> Bills:
        path: str = BillHandler().path_part(congress, bill_type)
        query_dict: dict[str, str] = self.__query_parameters(
            start_date, end_date, date_order, offset, limit
        )
        queries: str = f"?format=json&api_key={self.api_key}&" + "&".join(
            {
                f"{keys}={values}"
                for keys, values in query_dict.items()
                if values != "T00:00:00Z"
            }
        )
        url = self.host + path + queries.rstrip("&")
        bills_json: str = self.__make_request(url)
        bills_dict: Bills = self.__deserialize_json(bills_json)
        return bills_dict

    def bill(
        self,
        congress: int,
        bill_type: str,
        bill_number: int,
        start_date: str | None = None,
        end_date: str | None = None,
        date_order: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> Bill:
        """
        Takes multiple parameters to construct a GET request to api.congress.gov and gets back a bill.

        Parameters
        ----------
            congress : int | None
                Expects a "number" as a string literal, between 1 and 117. If only congress is given, expect multiple bills.

            bill_type : str | None
                Expects a value of hr, s, hjres, sjres, hconres, sconres, hres, or sres. Still expect multiple bills to be returned.

            bill_number : int | None
                The bill""s assigned number. Only one bill can be returned.

            start_date : str | None
                A filter constraining the date from which bills are returned. Will not affect the return value if a bill number is passed. Defaults to an empty string.

            end_date: str | None
                A filter constraining the date to which bills are returned. Will not affect the return value if a bill number is passed. Defaults to an empty string.

            date_ascending: str | None
                A filter that controls whether bills are filtered either in ascending or descending order, depending on the date they were created. Defaults to "ascending"/True.
            offset: int | None

            limit: int | None

        Returns
        -------
            Returns a json object as a string literal.

        Raises
        ------
            ValueError:
                Invalid value for congress, bill_type, bill_number
                Invalid date for start_date & end_date

        """
        # TODO define a typed dict with all the qery params as keys
        path: str = BillHandler().path_part(congress, bill_type, bill_number)
        query_dict: dict[str, str] = self.__query_parameters(
            start_date, end_date, date_order, offset, limit
        )
        queries: str = f"?format=json&api_key={self.api_key}&" + "&".join(
            {
                f"{keys}={values}"
                for keys, values in query_dict.items()
                if values != "T00:00:00Z"
            }
        )
        url = self.host + path + queries.rstrip("&")
        bill_json: str = self.__make_request(url)
        bill_dict: Bill = self.__deserialize_json(bill_json)
        return bill_dict

    def __getitem__(self, dict_key: str):
        return getattr(self, dict_key)
