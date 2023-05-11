import requests
import time
from selenium.webdriver.firefox.webdriver import WebDriver

from OpportunityRover.finder.config import connection_defaults

def get_content(
        url: str,
        headers=None,
        driver=None,
        dynamic=False):
    
    if dynamic and not driver:
        raise ValueError("Missing driver for dynamic content request.")

    elif dynamic:
        grab_html_dynamic(url, driver=driver)
    
    elif headers: 
        return grab_html_requests(url, headers)
    
    else:
        return grab_html_requests(url, headers=connection_defaults['headers'])


def grab_html_requests(url: str, headers: dict) -> str:
    return requests.get(url, headers=headers).content

def grab_html_dynamic(url:str, driver: WebDriver) -> str:
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.2)
    return driver.page_source