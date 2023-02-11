from src.handlers.handler_interface import HandlerInterface
from src.handlers.bill_handler import BillHandler


def test_path_part():
    instance = BillHandler()
    assert instance.path_part(117, "hr", 3387) == "bill/117/hr/3387"


def test_subclassing():
    instance = BillHandler()
    assert issubclass(BillHandler, HandlerInterface) == True
    assert isinstance(instance, BillHandler) == True
    assert isinstance(instance, HandlerInterface) == True
