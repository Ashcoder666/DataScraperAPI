import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "http://books.toscrape.com/"
url=base_url

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")

    for book in books:
        title = book.h3.a["title"]
        bookPrice = book.find("p",class_="price_color").text
        print(f"Book title : {title} , Price : {bookPrice}")
    
    next_button = soup.find("li",class_="next")
    if next_button:
        next_page = next_button.a["href"]
        url = urljoin(url, next_page)
        # print(url)
    else:
        url=None
        


