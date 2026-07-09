from app.scrapers.amazon import AmazonScraper
from app.scrapers.flipkart import FlipkartScraper
from app.scrapers.detector import detect_store


SCRAPERS = {
    "amazon": AmazonScraper,
    "flipkart": FlipkartScraper,
}


def get_scraper(url: str):

    store = detect_store(url)

    scraper_class = SCRAPERS.get(store)

    if scraper_class is None:
        raise ValueError(
            f"{store} is not supported."
        )

    return scraper_class()