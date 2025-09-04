import questionary;
from api_integrations.anime_api import get_anime_details
from web_scrapers.books_scraper import bookScraper
from web_scrapers.news_scraper import newsScarper
def main():

    choice = questionary.select(
        "Welcome to DataScraperAPI \n Please Select an Option : ",
        choices=[
            "Fetch anime Details",
            "Scrape Books",
            "Scrape Malayalam News",
            "Exit"
        ]
    ).ask()
    
    if choice == "Fetch anime Details":
        get_anime_details()
    elif choice == "Scrape Books":
        bookScraper()
    elif choice == "Scrape Malayalam News":
        newsScarper()
    else:
        print("Exiting")


if __name__ == "__main__":
    main()
