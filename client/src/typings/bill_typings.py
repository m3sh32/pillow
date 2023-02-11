from typing import TypedDict, Literal

Party = Literal["D", "R", "I"]


class CountUrl(TypedDict, total=True):
    count: int
    url: str


class CosponsorUrl(TypedDict, total=True):
    count: int
    count_including_withdrawn_cosponsors: int
    url: str


class CboCostEstimate(TypedDict, total=True):
    pub_date: str
    title: str
    url: str


class CitationUrl(TypedDict, total=True):
    citations: str
    url: str


class DateText(TypedDict, total=True):
    date: str
    text: str


class NumberType(TypedDict, total=True):
    number: str
    _type: str


class RequestData(TypedDict, total=True):
    bill_number: int
    bill_type: Literal[
        "hr", "s", "hjres", "sjres", "hconres", "sconres", "hres", "sres"
    ]
    congress: int
    content_type: Literal["application/json"]
    _format: Literal["json"]


class Sponsor(TypedDict, total=True):
    bioguide_id: str
    full_name: str
    first_name: str
    last_name: str
    middle_name: str
    is_by_request: str
    url: str
    party: Party
    state: str
    district: str


class BillValue(TypedDict, total=True):
    """
    BillValue class is a child class of TypedDict, which allows for more specific type hints for dictionaries with set keys.
    """

    actions: CountUrl
    amendments: CountUrl
    cbo_cost_estimates: list[CboCostEstimate]
    comittee_reports: CitationUrl
    comittees: CountUrl
    congress: int
    constitutional_authority_statement_text: str
    cosponsors: CosponsorUrl
    introduced_date: str
    laws: list[NumberType]
    number: str
    origin_chamber: str
    policy_area: dict[Literal["name"], str]
    related_bills: CountUrl
    sponsors: list[Sponsor]
    subjects: CountUrl
    summaries: CountUrl
    text_versions: CountUrl
    title: str
    titles: CountUrl
    _type: str
    update_date: str
    udpate_date_including_text: str
    request: RequestData


class Bill(TypedDict, total=True):
    """
    TypedDict corresponding to JSON dictionary returned by Client.bills()
    """

    bill: BillValue
