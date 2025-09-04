import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd



base_url = "http://books.toscrape.com/"


def bookScraper():
    counterr = 1
    url=base_url
    allBooks = []
    current_percentage = 2

    while url:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"}
        response = requests.get(url,headers=headers,timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article")

        for book in books:
            title = book.h3.a["title"]
            bookPrice = book.find("p",class_="price_color").text
            allBooks.append({"title":title,"price":bookPrice})
        
    
        next_button = soup.find("li",class_="next")
        if next_button and counterr < 5:
            next_page = next_button.a["href"]
            url = urljoin(url, next_page)
            counterr += + 1
        else:
            url=None
        
    
        print(f"{current_percentage}% is completed" )
        current_percentage +=  2

    df = pd.DataFrame(allBooks)

    df["price"] = (
        df["price"]
        .str.replace("£", "", regex=False)  
        .str.replace("Â", "", regex=False)  
        .astype(float)
    )

    df.to_csv("outputs/books.csv",index=False)
    
    
