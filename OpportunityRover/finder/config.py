
targets = {

    "Artist Communities" : {

        "site_type":"static",

        "model": "lookinside",

        "limit": -1,

        "site": "https://artistcommunities.org/directory/open-calls?opencall_name=&residency=&org=&field_residency_address_locality=&discipline%5B%5D=429&discipline%5B%5D=378&discipline%5B%5D=422&no_deadline=0&sort_bef_combine=field_deadline_value_ASC",

        "lookinside_base":"https://artistcommunities.org",

        "list_container_search": {"type":"tbody"},

        "list_item_search": {"type": "tr"},

        "anchor_search": {},

        "name_search": {"type":"h1", "class":"page-title"},

        "summary_search": {"type":"div", "class":"clearfix text-formatted field field--name-field-oc-residency-description field--type-text-with-summary field--label-hidden field__item"},

        "keyword_search": {"type":"div", "id": "block-aca-content", "class":"block block-system block-system-main-block"}
    },

    "Mid America Print Council" : {

        "site_type":"static",

        "model": "lookinside",

        "limit": -1,

        "site": "https://midamericaprintcouncil.org/category/opportunities/",

        "lookinside_base":"",

        "list_container_search": {"type":"div", "class":None, "id":"isotope-list"},

        "list_item_search": {"type": "div"},

        "anchor_search": {"type":"h2", "class":"entry-title default-max-width"},

        "name_search": {"type":"h1", "class":"entry-title"},

        "summary_search": {"type":"div", "class":"entry-content"},

        "keyword_search": {"type":"div", "class":"entry-content"},
    },

    "artwork archive - print" : {

        "site_type":"static",

        "model": "lookinside",

        "limit": -1,

        "site": "https://www.artworkarchive.com/call-for-entry?call_search=print",

        "lookinside_base":"https://www.artworkarchive.com",

        "list_container_search": {"type":"div", "class":"medium-9 columns"},

        "list_item_search": {"type": "div", "class":"medium-12 columns", "recursive": True},

        "anchor_search": {},

        "name_search": {"type":"h2"},

        "summary_search": {"type":"section", "class":"external_link_security"},

        "keyword_search": {"type":"section", "class":"external_link_security"},
    },

    "New York Foundation for the Arts" : {

        "site_type":"api",

        "model": "apilookinside",

        "limit": -1,

        "site": "https://api.nyfa.org/api/client/listing/opportunities?Type=Opportunity&q=&page=1&location=&noFeeApplication=&opportunityType=&opportunityDiscipline=&oppRemoteType=",

        "lookinside_base":"https://api.nyfa.org/api/client/listing/REPLACE_ME/opportunity",

        "list_container": "listings",

        "link_search": "listingId",

        "link_constructor": "https://www.nyfa.org/view-opportunity/?id=REPLACE_ME",

        "searches": {

            "name": "title",

            "summary": "description",

            "keyword": ["description", "opportunityDisciplines"],

            "application_fee": "applicationFee",

            "deadline": "applicationDeadline"
        }

    },
}

subjects = {
    "book arts": ["book arts", "bookmaking", "bookbinding", "book making", "book binding"],
    "paper making": ["paper"],
    "print": ["printmaking", "print", "printmedia"],
    "disability": ["disability", "disabilities"],
    "women": ["woman", "women"]
}

connection_defaults = {
    "headers": {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1'
    },
}