import requests

def get_university_website(school_name):
    # Replace spaces with '%20' for URL encoding
    school_name_encoded = school_name.replace(' ', '%20')

    # API endpoint for searching by name
    url = f'http://universities.hipolabs.com/search?name={school_name_encoded}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the JSON response
        universities = response.json()

        # Assuming the first match is the desired one
        if universities:
            return universities[0]['web_pages'][0]
        else:
            return "No university found with that name."

    except requests.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    school_name = "Dickinson College"
    website = get_university_website(school_name)
    print(website)
