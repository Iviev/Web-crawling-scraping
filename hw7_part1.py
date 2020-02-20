# 507/206 Homework 7 Part 1
import requests
import json
from bs4 import BeautifulSoup
#crawl the url that has all in it
#### Your Part 1 solution goes here ####
CACHE_FNAME = "cached_umsidata.json"
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# if there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}
#
# # A helper function that accepts 2 parameters
# # and returns a string that uniquely represents the request
# # that could be made with this info (url + params)

def get_unique_key(url):
  return url
#     #### Implement your function here ####

def make_request_using_cache(url):
    global header
    unique_ident = get_unique_key(url)

    ## first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    ## if not, fetch the data afresh, add it to the cache,
    ## then write the cache to file
    else:
        print("Making a request for new data...")
        # Make the request and cache the new data
        header = {'User-Agent': 'SI_CLASS'}
        resp = requests.get(url, headers=header)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]

baseurl = "https://www.si.umich.edu/directory?rid=All&page=0"
baseurl_contact = "https://www.si.umich.edu"

#
def get_umsi_data(page):
    baseurl_contact = "https://www.si.umich.edu"
    # header = {'User-Agent': 'SI_CLASS'}
    page_text = make_request_using_cache(page)
    page_soup = BeautifulSoup(page_text, 'html.parser')
    content_div = page_soup.find(class_="view-content")
    content_names = content_div.find_all(class_="views-row")


    umsi_titles_page = {}




    for profile in content_names:
        profile_name = profile.find(class_="field field-name-title field-type-ds field-label-hidden")
        name = profile_name.string
        name_listings = [name]

        profile_title = profile.find(class_="field field-name-field-person-titles field-type-text field-label-hidden")
        title = profile_title.string
        titles_listitngs = [title]


        profile_email = profile.find(class_="field field-name-contact-details field-type-ds field-label-hidden")
        contact_url_end = profile_email.find("a")["href"]
        contact_details_url = baseurl_contact + contact_url_end
        header = {'User-Agent': 'SI_CLASS'}
        contact_page_text = make_request_using_cache(contact_details_url)
        contact_page_soup = BeautifulSoup(contact_page_text, 'html.parser')
        contact_content_div = contact_page_soup.find_all(class_="container3")
        contact_email_div = contact_content_div[0]
        contact_email_id = contact_email_div.find(id = "content-inside")
        contact_email_info = contact_email_id.find(class_="field field-name-field-person-email field-type-email field-label-inline clearfix")
        contact_email = contact_email_info.find("a")["href"]
        email = contact_email[7:]
        email_lisitings = [email]
    # print(email)
        umsi_titles_page[name] = {}
        umsi_titles_page[name]["title"] = title
        umsi_titles_page[name]["email"] = email

    return umsi_titles_page


# get_umsi_data(baseurl)

umsi_titles = {}
for pages in range(13):
    baseurl = baseurl[:48] + str(pages)
    umsi_titles.update(get_umsi_data(baseurl))
# print(umsi_titles)


file_name = open("directory_dict.json", "w")
file_name.write(json.dumps(umsi_titles))
