from src.handlers.handler_interface import HandlerInterface


class BillHandler(HandlerInterface):
    """
    Attributes
    ----------
        None

    Methods
    -------
        path_part : Constructs the path to the congress api
    """

    def __init__(
        self,
    ) -> None:
        super().__init__()

    def path_part(  # type: ignore
        self,
        congress: int | None = None,
        bill_type: str | None = None,
        bill_number: int | None = None,
    ) -> str:
        """
        Parameters
        ----------
            congress : int
                An integer parameter repersenting different congresses

            bill_type : str
                Accepts a value to specify the type of bills the user wants. Options are: hr, s, hjres, sjres, hconres, sconres, hres, or sres.

            bill_number : int
                An integer parameter repersenting the unique identifier each bill has

        Returns
        -------
            Returns a string that is the path of the HTTP request to the congress api

        """
        self.bill_validator(congress, bill_type, bill_number)
        if congress == None:
            congress_path: str = ""
        else:
            congress_path = str(congress)
        if bill_type == None:
            bill_type_path: str = ""
        else:
            bill_type_path = bill_type  # type: ignore
        if bill_number == None:
            bill_number_path: str = ""
        else:
            bill_number_path = str(bill_number)
        return f"bill/{congress_path}/{bill_type_path}/{str(bill_number_path)}".rstrip(
            "/"
        )

    def bill_validator(
        self,
        congress: int | None = None,
        bill_type: str | None = None,
        bill_number: int | None = None,
    ) -> None:
        if isinstance(congress, int) == False and congress != None:
            raise ValueError(
                f"{type(congress)} is an invalid value for congress, please enter an integer"
            )

        if (
            bill_type
            not in [
                "hr",
                "s",
                "hjres",
                "sjres",
                "hconres",
                "sconres",
                "hres",
                "sres",
            ]
            and bill_type != None
        ):
            raise ValueError(
                f" {bill_type} is an invalid value for bill_type, please enter one of: hr, s, hjres, sjres, hconres, sconres, hres, sres"
            )

        if isinstance(bill_number, int) == False and bill_number != None:
            raise ValueError(
                f"{type(bill_number)} is an invalid value for bill_number, please enter an integer"
            )
