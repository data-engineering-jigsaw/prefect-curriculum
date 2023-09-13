from bs4 import BeautifulSoup
from data import html


soup = BeautifulSoup(html, 'html.parser')

# Extract title from each list element
for li in soup.find_all('li', class_='cl-search-result'):
    title = li['title']
    print("Title:", title)

    # Extract metadata
    metadata = li.find('span', class_='meta').get_text(strip=True, separator=' ')
    print("Metadata:", metadata)

