# DataScaper API

A Python project demonstrating web scraping and API integration with multiple free datasets and APIs. This project helps you practice extracting data from websites, consuming APIs, and processing real-world data for analysis or application purposes.

🚀 Features
Web Scraping

This project includes scripts to scrape data from publicly available websites:

News Headlines
Scrape latest headlines from news portals like BBC or Hindustan Times.

Books Data
Scrape book titles, prices, and availability from Books to Scrape
.

Quotes
Scrape quotes and authors from Quotes to Scrape
.

API Integration

Integrate and fetch data using popular free APIs:

OpenWeatherMap API → Get weather information by city.

NewsAPI → Fetch latest news headlines globally.

CoinGecko API → Retrieve cryptocurrency prices.

Jikan API → Get Anime/Manga information (perfect for hobby projects).

🛠 Tech Stack

Language: Python 3.x

Libraries:

requests → HTTP requests

BeautifulSoup4 → Web scraping

pandas → Data storage and processing

json → Handling API responses

API Keys Needed:

OpenWeatherMap API

NewsAPI

All other APIs are free to use without authentication.

📖 Usage
1. Clone the Repository
git clone https://github.com/your-username/project-2-web-scraping-api.git
cd project-2-web-scraping-api

2. Install Dependencies
pip install -r requirements.txt

3. Run Web Scrapers
# News headlines
python web_scraping/news_scraper.py

# Books data
python web_scraping/books_scraper.py

# Quotes
python web_scraping/quotes_scraper.py

4. Use API Scripts
# Weather data
python api_integration/weather_api.py

# News headlines
python api_integration/news_api.py

# Cryptocurrency prices
python api_integration/crypto_api.py

# Anime/Manga info
python api_integration/anime_api.py


Make sure to add your API keys in the respective scripts (e.g., weather_api.py, news_api.py).

⚡ Key Learning Outcomes

Understand web scraping using BeautifulSoup.

Learn API integration and handling JSON responses.

Practice working with real-world datasets.

Enhance skills in data processing and storage using Python.

📌 Notes

Only scrape websites that allow scraping (like Books to Scrape and Quotes to Scrape).

Handle API rate limits and errors gracefully.

Scripts can be modified to store data in CSV/JSON for further analysis.

📚 References

BeautifulSoup Documentation

Requests Documentation

OpenWeatherMap API

NewsAPI

CoinGecko API

Jikan API
