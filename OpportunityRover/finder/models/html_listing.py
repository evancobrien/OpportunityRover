import OpportunityRover.finder.config as config

from OpportunityRover.finder.web.web import get_content
from OpportunityRover.finder.util import find_relevent_subjects, soup_find, soup_children
from OpportunityRover.finder.exceptions import InvalidSiteType
from OpportunityRover.finder.results import Opportunity
from bs4 import BeautifulSoup


def html_listing(
                source:str,
                site_type:str,
                source_url:str,
                list_container_search: dict,
                list_item_search: dict,
                link_search: dict,
                driver=None
                ):

    if site_type == 'static':
        content = get_content(url=source_url)
    elif site_type == 'dynamic':
        content = get_content(url=source_url, driver=driver)
    else: raise InvalidSiteType()

    # Create Soup
    soup = BeautifulSoup(content, "html.parser")
    listing_container = soup_find(soup, list_container_search)
    listings = soup_children(listing_container, list_item_search)

    opportunities = []

    for item in listings:
        text = item.find('p').getText()
        class_type = " ".join(item['class'])


        link_object = soup_find(item, link_search).find('a')
        if link_object:
            link = link_object['href']
        else:
            link = item


        hits = find_relevent_subjects(string=text, subject_dict=config.subjects)

        opp = Opportunity(
            source=source,
            source_url=source_url,
            name=class_type,
            link=link,
            relevant_subjects=hits,
            summary=text
            )
        opportunities.append(opp)
    
    print(f"Simple List model run for {source}, {len(opportunities)} opportunities found")
    return opportunities