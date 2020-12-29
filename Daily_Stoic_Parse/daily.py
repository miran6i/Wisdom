import csv
import requests
from bs4 import BeautifulSoup

pages_num = list(range(1,17))
raw_link = 'https://www.goodreads.com/quotes/tag/stoicism?page='
links = []
for x in pages_num:
    links.append(raw_link + str(x))


def get_html(url):
    res = requests.get(url)
    return res.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        author = soup.find('span', class_="authorOrTitle").get_text(strip=True)
    except:
        author = ''
    try:
        quote = soup.find('div', class_="quoteText").get_text(strip=True)
    except:
        quote = ''
    data = {'author': author, 'quote': quote}
    return data

def write_csv(data):
    with open('quotes.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['author'], data['quote']])

def main():
        while True:
            for link in links:
                html = get_html(link)
                data = get_page_data(html)
                print(data)
                write_csv(data)

if __name__ == "__main__":
    main()