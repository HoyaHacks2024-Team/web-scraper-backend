import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

'''
parsing.py

Will curate a link of urls that can be passed into Langchain
'''


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
def curate_urls(start_urls, keywords=[]):
    found_urls = set()

    all_links = get_filtered_links(start_urls)
    for link in all_links:
        if link not in found_urls and search_for_keywords(link, keywords):
            found_urls.add(link)
    return found_urls


# Fetch and parse the html page of the url
def fetch_and_parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text


# Remove HTML tags
def remove_html_tags(html_content):
    if html_content is None:
        return ""
    
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract text without HTML tags
    text = soup.get_text()
    
    return text


# Testing
if __name__ == '__main__':
    found = curate_urls("http://www.dickinson.edu", ["admissions", "financial aid", "scholarship", "campus life", "academics", "meal plans"])
    print(found)