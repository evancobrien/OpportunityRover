import json

from OpportunityRover.finder.web.web import get_content
from OpportunityRover.finder.util import find_relevent_subjects
from OpportunityRover.finder.config import subjects
from OpportunityRover.finder.results import Opportunity

def api_lookup(
                      source:str,
                      site_type:str,
                      source_url:str,
                      lookinside_base: str,
                      headers: dict,
                      list_container: str,
                      link_search: dict,
                      link_constructor: str,
                      searches: dict
                      ):

    response = json.loads(get_content(source_url, headers=headers))
    listings = response[list_container]

    targets = [listing[link_search] for listing in listings]

    ops = []
    for target in targets:
        target_url = lookinside_base.replace('REPLACE_ME', target)
        item = json.loads(get_content(target_url, headers=headers))

        keyword_body = ''
        for term in searches['keyword']:
            keyword_body += item[term]

        ops.append(Opportunity(
            source                  = source,
            source_url              = source_url,
            name                    = item[searches['name']],
            relevant_subjects       = find_relevent_subjects(keyword_body, subjects),
            link                    = link_constructor.replace('REPLACE_ME', target),
            application_fee         = item[searches['application_fee']],
            deadline                = item[searches['deadline']],
            summary                 = item[searches['summary']],
            review_state            = None,

        ))

    return ops


    