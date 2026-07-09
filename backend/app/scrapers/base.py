from abc import ABC, abstractmethod


class BaseScraper(ABC):

    @abstractmethod
    def scrape(self, url: str):
        """
        Fetch the webpage and return a BeautifulSoup object.
        """
        pass

    @abstractmethod
    def extract(self, url: str):
        """
        Return normalized product data.
        """
        pass