from dataclasses import dataclass, field

@dataclass
class Opportunity:
    source: str = ""
    source_url: str = ""
    name: str = ""
    link: str = ""
    relevant_subjects: list = field(default_factory=list)
    application_fee = None
    deadline = None
    review_state = None
    summary: str = ""
