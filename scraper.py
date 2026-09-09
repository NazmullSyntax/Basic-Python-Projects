import requests
from bs4 import BeautifulSoup

url = input("Enter URL: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get all headlines (for news sites)
for headline in soup.find_all('h1'):
    print(headline.text.strip())