import abc


class HandlerInterface(abc.ABC):
    """
    Interface for other handlers implemented through abstract base classes.


    Methods
    -------
        path_part : Abstract method for other handlers.

    """

    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def path_part(self) -> str | None:
        """
        Returns
        -------
        Empty string
        """
        pass
