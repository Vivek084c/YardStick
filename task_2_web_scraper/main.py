# Import required libraries
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://techcrunch.com/2024/04/30/sams-clubs-ai-powered-exit-tech-reaches-20-of-stores/"

# Send a GET request to fetch the raw HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the article title
    title = soup.find('h1').get_text()
    print(f"Title: {title}\n")

    # Extract the content of the article
    article_body = soup.find_all('p')
    
    print("Article Content:\n")
    for paragraph in article_body:
        print(paragraph.get_text())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")