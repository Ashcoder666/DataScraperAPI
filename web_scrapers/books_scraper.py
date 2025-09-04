import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd



base_url = "http://books.toscrape.com/"


def bookScraper():
    url=base_url
    allBooks = []
    current_percentage = 2

    while url:
        response = requests.get(url,timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article")

        for book in books:
            title = book.h3.a["title"]
            bookPrice = book.find("p",class_="price_color").text
            allBooks.append({"title":title,"price":bookPrice})
        
    
        next_button = soup.find("li",class_="next")
        if next_button:
            next_page = next_button.a["href"]
            url = urljoin(url, next_page)
        else:
            url=None
        
    
        print(f"{current_percentage}% is completed" )
        current_percentage +=  2

    df = pd.DataFrame(allBooks)

    df["price"] = df["price"].str.replace("£", "").astype(float)

    df.to_csv("books.csv",index=False)
    
    
