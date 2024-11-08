import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://quotes.toscrape.com"

def scrape_quotes():
    quotes = []
    next_url = BASE_URL + "/"

    while next_url:
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, "html.parser")
        quote_divs = soup.select('.quote')

        for quote_div in quote_divs:
            text = quote_div.select_one('.text').get_text()
            author = quote_div.select_one('.author').get_text()
            quotes.append({"text": text, "author": author})

        next_page = soup.select_one('.next > a')
        next_url = BASE_URL + next_page['href'] if next_page else None

    return quotes

if __name__ == "__main__":
    quotes = scrape_quotes()
    with open('quotes.json', 'w', encoding='utf-8') as json_file:
        json.dump(quotes, json_file, ensure_ascii=False, indent=4)
