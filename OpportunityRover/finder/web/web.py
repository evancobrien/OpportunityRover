import requests
import time
from selenium.webdriver.firefox.webdriver import WebDriver

def get_content(
        url: str,
        headers=None,
        driver=None):
    
    if not headers and not driver: 
        raise ValueError("either headers or driver parameter must be provided.")
    
    elif headers and driver: 
        raise ValueError("headers and driver parameters are mutually exclusive. provide one.")
    
    elif headers: 
        return grab_html_requests(url, headers)
    
    elif driver:
        return grab_html_dynamic(url, driver)


def grab_html_requests(url: str, headers: dict) -> str:
    return requests.get(url, headers=headers).content

def grab_html_dynamic(url:str, driver: WebDriver) -> str:
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.2)
    return driver.page_source