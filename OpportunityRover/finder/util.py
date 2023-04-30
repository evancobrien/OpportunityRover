from bs4 import BeautifulSoup



def find_relevent_subjects(string: str, subject_dict: dict) -> list:
    results = []
    for subj, terms in subject_dict.items():
        for term in terms:
            if string.find(term) != -1:
                results.append(subj)
                break

    return results

def soup_find(soup: BeautifulSoup, search_dict: dict) -> BeautifulSoup:
    stype = search_dict.get('type')
    sid = search_dict.get('id')
    sclass = search_dict.get('class')

    listing_container = soup

    if stype and sid and sclass:
        listing_container = soup.find(stype, id=sid, class_=sclass)
    elif stype and sid:
        listing_container = soup.find(stype, id=sid)
    elif stype and sclass:
        listing_container = soup.find(stype, class_=sclass)
    elif stype:
        listing_container = soup.find(stype)
    
    return listing_container

def soup_children(soup: BeautifulSoup, search_dict: dict) -> list[BeautifulSoup]:
    stype = search_dict.get('type')
    sid = search_dict.get('id')
    sclass = search_dict.get('class')
    srecurse = search_dict.get('recursive', False)

    listing_container = soup

    if stype and sid and sclass:
        listing_container = soup.findChildren(stype, id=sid, class_=sclass, recursive=srecurse)
    elif stype and sid:
        listing_container = soup.findChildren(stype, id=sid, recursive=srecurse)
    elif stype and sclass:
        listing_container = soup.findChildren(stype, class_=sclass, recursive=srecurse)
    elif stype:
        listing_container = soup.findChildren(stype, recursive=srecurse)
    
    return listing_container