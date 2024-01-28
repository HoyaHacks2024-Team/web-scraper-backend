import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

'''
parsing.py

Will curate a link of urls that can be passed into Langchain
'''

# Find the environmental variables
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env')
load_dotenv(dotenv_path=env_path)


# Confirm the validity of the url
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# Iterate and curate links
def get_filtered_links(url):
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [
        urljoin(url, a['href']) for a in soup.find_all('a', href=True)
        if a['href'] and not a['href'].startswith(('#', 'javascript:', 'mailto:', 'tel:'))
    ]
    return [link for link in links if is_valid_url(link) and urlparse(url).netloc in link]



# Search for keywords
def search_for_keywords(url, keywords):
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text().lower()
    for keyword in keywords:
        if keyword.lower() in text:
            return True
    return False



# Curate a list of links
def curate_urls(start_urls=[], keywords=[]):
    found_urls = set()
    for url in start_urls:
        all_links = get_filtered_links(url)
        for link in all_links:
            if link not in found_urls and search_for_keywords(link, keywords):
                found_urls.add(link)
    return found_urls

if __name__ == '__main__':
    found = curate_urls(["http://www.dickinson.edu"], ["admissions", "financial aid", "scholarship", "campus life", "academics", "meal plans"])
    print(found)