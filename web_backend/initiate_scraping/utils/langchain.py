from langchain_community.document_loaders import BSHTMLLoader
import re

from parsing import curate_urls, fetch_and_parse, remove_html_tags


'''
langchain.py

Will run a BSHTMLLoader Langchain model on the curated list of urls to return a vector embedding
'''

KEYWORDS = ["admissions", "financial aid", "scholarship", "campus life", "academics", "meal plans"]


# Remove special characters and extra whitespace
def clean_text(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text


def finalize_text(home_url):
    subpage_contents = set()

    # Curate urls using parsing.py functions
    sub_urls = curate_urls(home_url, KEYWORDS)

    for url in sub_urls:
        try:
            # Fetch the HTML content
            html_content = fetch_and_parse(url)
            processed_text = clean_text(html_content)
            subpage_contents.add(processed_text)
        except Exception as e:
            print(f"Failed to process {url}: {e}")
            continue
    return subpage_contents


# def langchain_loader(home_url):
    subpage_contents = set()

    # Curate urls using parsing.py functions
    sub_urls = curate_urls(home_url, KEYWORDS)

    for url in sub_urls:
        try:
            # Fetch the HTML content
            html_content = fetch_and_parse(url)
            processed_text = clean_text(html_content)
            
            # Initialize BSHTMLLoader with the HTML content
            loader = BSHTMLLoader(str(processed_text))
            
            # Load data
            data = loader.load()
            subpage_contents.add(data)
        except Exception as e:
            print(f"Failed to process {url}: {e}")
            continue
    return subpage_contents


# Testing
if __name__ == '__main__':
    start_url = "http://www.dickinson.edu"
    sub_cont = finalize_text(start_url)
    print(sub_cont)