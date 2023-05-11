import requests
import OpportunityRover.finder.config as config
import pandas as pd

from OpportunityRover.finder.web.driver import get_driver
from OpportunityRover.finder.models.html_listing import html_listing
from OpportunityRover.finder.models.html_lookup import html_lookup
from OpportunityRover.finder.models.api_lookup import api_lookup


def run_main():

    driver = get_driver()

    opportunities = []

    for key, value in config.targets.items():

        model = value['model']
        if model == 'simplelist':

            ops = html_listing(    
                                        source                  =key,
                                        site_type               =value['site_type'],
                                        source_url              =value['site'],
                                        headers                 =value['headers'],
                                        list_container_search   =value['list_container_search'],
                                        list_item_search        =value['list_item_search'],
                                        link_search             =value['link_search'],
                                        driver                  =driver)
                    
        if model == 'lookinside':

            ops = html_lookup(    
                                        source                  =key,
                                        site_type               =value['site_type'],
                                        limit                   =value['limit'],
                                        source_url              =value['site'],
                                        lookinside_base         =value['lookinside_base'],
                                        headers                 =value['headers'],
                                        list_container_search   =value['list_container_search'],
                                        list_item_search        =value['list_item_search'],
                                        anchor_search           =value['anchor_search'],
                                        name_search             =value['name_search'],
                                        summary_search          =value['summary_search'],
                                        keyword_search          =value['keyword_search'],
                                        driver                  =driver)
            
        if model == 'apilookinside':
            ops = api_lookup(                                        
                                        source                  =key,
                                        site_type               =value['site_type'],
                                        source_url              =value['site'],
                                        lookinside_base         =value['lookinside_base'],
                                        headers                 =value['headers'],
                                        list_container          =value['list_container'],
                                        link_search             =value['link_search'],                                        
                                        link_constructor        =value['link_constructor'],
                                        searches                =value['searches'])

        opportunities.extend(ops)
        print(f"Scraped {key}, {len(ops)} opportunities found.")

        

    df = pd.DataFrame(opportunities)
    print(df)
    df.to_csv("./results.csv")
    driver.quit()
     