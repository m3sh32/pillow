from typing import TypedDict, Literal
from src.typings.bill_typings import RequestData


class latestAction(TypedDict, total=True):
    actionDate: str
    text: str


class BillsValue(TypedDict, total=True):
    congress: int
    latestAction: latestAction
    number: str
    originChamber: Literal["Senate", "House"]
    originChamberCode: Literal["S", "H"]
    title: str
    type: str
    updateDate: str
    updateDateIncludingText: str
    url: str
    request: RequestData


class Bills:
    bills: list[BillsValue]
