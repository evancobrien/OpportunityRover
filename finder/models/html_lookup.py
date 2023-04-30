import OpportunityRover.finder.config as config
import time
from random import uniform
from OpportunityRover.finder.web.web import grab_content
from OpportunityRover.finder.util import find_relevent_subjects, soup_find, soup_children
from OpportunityRover.finder.results import Opportunity
from OpportunityRover.finder.exceptions import InvalidSiteType
from bs4 import BeautifulSoup


def html_lookup(
                      source:str,
                      site_type:str,
                      limit: int,
                      source_url:str,
                      lookinside_base: str,
                      headers: dict,
                      list_container_search: dict,
                      list_item_search: dict,
                      anchor_search: dict,
                      name_search: dict,
                      summary_search: dict,
                      keyword_search: dict,
                      driver = None,
                      ):
    
    if site_type == 'static':
        content = grab_content(url=source_url, headers=headers)
    elif site_type == 'dynamic':
        content = grab_content(url=source_url, driver=driver)
    else: raise InvalidSiteType()


    # Create Soup
    soup = BeautifulSoup(content, "html.parser")
    listing_container = soup_find(soup, list_container_search)
    listings = soup_children(listing_container, list_item_search)

    opportunities = []

    anchors = set()
    for item in listings:
        # We need to get a url to the main description page here where we can do a more thorough search
        
        try:
            anchor_url = soup_find(item, anchor_search).find('a')['href']
            anchors.add(anchor_url)
        except:
            pass

    i = 0
    for anchor in anchors:
        if i == limit: break

        time.sleep(uniform(0.5, 1))
        target = lookinside_base + anchor

        if site_type == 'static':
            item_content = grab_content(target, headers=headers)
        elif site_type == 'dynamic':
            item_content = grab_content(target, driver=driver)

        item_soup = BeautifulSoup(item_content, "html.parser")
        print(item_soup)
        name = soup_find(item_soup, name_search).get_text(" ")
        summary = soup_find(item_soup,summary_search).get_text("\n")
        keyword_search_text = soup_find(item_soup, keyword_search).get_text("\n")
        subjects = find_relevent_subjects(keyword_search_text, config.subjects)

        opp = Opportunity(
            source=source,
            source_url=source_url,
            name=name,
            relevant_subjects=subjects,
            link=target,
            summary=summary
        )

        opportunities.append(opp)
    
    return opportunities