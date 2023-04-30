import json

from OpportunityRover.finder.web.web import grab_content
from OpportunityRover.finder.results import Opportunity

def api_lookup(
                      source:str,
                      site_type:str,
                      source_url:str,
                      lookinside_base: str,
                      headers: dict,
                      list_container: str,
                      link_search: dict,
                      name_search: dict,
                      summary_search: dict,
                      keyword_search: dict,
                      ):

    response = json.loads(grab_content(source_url, headers=headers))
    listings = response[list_container]

    targets = [listing[link_search] for listing in listings]

    ops = []
    for target in targets:
        target_url = lookinside_base.replace('REPLACE_ME', target)
        item = json.loads(grab_content(target_url, headers=headers))

        name = item[name_search]
        summary = item[summary_search]

        ops.append(Opportunity(
            source=source,
            source_url=source_url,
            name=name,
            summary=summary
        ))

    return ops


    