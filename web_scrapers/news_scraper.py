from bs4 import BeautifulSoup
import requests
base_url = "https://www.manoramaonline.com/news/latest-news/2025/09/04/digs-report-minimizes-youth-congress-leader-assaulted-in-police-custody-incident.html"

def newsScarper():
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"}
    
    response = requests.get(base_url,headers=headers)
    response.encoding = 'utf-8'
    # print(response)
    
    soup = BeautifulSoup(response.text,"html.parser")
    
    Headline = soup.find("h1",class_="article-header__title").get_text(strip=True)
    content = soup.find("div",class_="rtearticle text")
    print(Headline)
    for cont in content:
        text = cont.get_text(strip=True)
        print(text.encode('utf-8').decode('utf-8'))
    
    