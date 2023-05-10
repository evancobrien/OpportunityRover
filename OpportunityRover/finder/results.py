import datetime as dt
from dataclasses import dataclass, field

@dataclass
class Opportunity:
    source: str = ""
    source_url: str = ""
    name: str = ""
    link: str = ""
    relevant_subjects: list = field(default_factory=list)
    application_fee: float = None
    deadline:str = None
    review_state: str = None
    summary: str = ""
    created_on: dt.datetime = dt.datetime.now()
