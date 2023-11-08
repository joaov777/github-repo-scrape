import requests
from bs4 import BeautifulSoup


github_username = input("Enter the Github username: ")

# URL to scrape
url = f'https://github.com/{github_username}?tab=repositories'

# Send an HTTP GET request
response = requests.get(url)


# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and print the titles of the latest articles
    h3_elements = soup.find_all('h3')

    for h3_tag in h3_elements:
        a_tag = h3_tag.find('a')

        if a_tag:
            link = a_tag.get('href')

            print(link[1:])

else:
    print(f"Failed! User {github_username} not found!!")

