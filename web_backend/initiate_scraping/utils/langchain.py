from langchain_community.document_loaders import BSHTMLLoader

'''
langchain.py

Will run a BSHTMLLoader Langchain model on the curated list of urls to return a vector embedding
'''

# @TODO temporary variables - update keywords and get start_urls from FE
start_urls = ["http://www.dickinson.edu"]
keywords = ["admissions", "financial aid", "scholarship", "campus life", "academics", "meal plans"]

def langchain_loader(home_url):
    subpage_contents = {}

    # Curate urls using parsing.py functions
    subpage_urls = curate_urls([home_url], key)

    for url in subpage_urls:
        try:
            # Fetch the HTML content
            html_content = fetch_and_parse(url)
            
            # Initialize BSHTMLLoader with the HTML content
            loader = BSHTMLLoader(str(html_content))
            
            # Load data
            data = loader.load()
            print(data)
        except Exception as e:
            print(f"Failed to process {url}: {e}")