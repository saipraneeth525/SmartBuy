import requests
from bs4 import BeautifulSoup

from app.scrapers.base import BaseScraper
from app.scrapers.utils import clean_price


class AmazonScraper(BaseScraper):

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-IN,en;q=0.9",
    }

    def scrape(self, url: str):

        response = requests.get(
            url,
            headers=self.HEADERS,
            timeout=20,
        )

        response.raise_for_status()

        return BeautifulSoup(
            response.text,
            "lxml",
        )

    def extract(self, url: str):

        soup = self.scrape(url)

        # ---------- Title ----------
        title = ""

        title_selectors = [
            "#productTitle",
            "#title",
            "span#productTitle",
        ]

        for selector in title_selectors:
            tag = soup.select_one(selector)
            if tag:
                title = tag.get_text(strip=True)
                break

        # ---------- Price ----------
        price = 0

        price_selectors = [
            ".priceToPay .a-offscreen",
            ".apexPriceToPay .a-offscreen",
            ".a-price.aok-align-center .a-offscreen",
            ".reinventPricePriceToPayMargin .a-offscreen",
            ".a-price .a-offscreen",
            ".a-price-whole",
        ]

        for selector in price_selectors:
            tag = soup.select_one(selector)

            if tag:
                price = clean_price(tag.get_text())

                if price > 0:
                    break

        # ---------- Rating ----------
        rating = 0

        rating_selectors = [
            "span.a-icon-alt",
            "#acrPopover span.a-size-base",
        ]

        for selector in rating_selectors:
            tag = soup.select_one(selector)

            if tag:
                try:
                    rating = float(tag.get_text().split()[0])
                    break
                except Exception:
                    pass

        # ---------- Reviews ----------
        reviews = 0

        review_selectors = [
            "#acrCustomerReviewText",
            "#acrCustomerReviewLink span",
        ]

        for selector in review_selectors:
            tag = soup.select_one(selector)

            if tag:
                text = (
                    tag.get_text()
                    .replace(",", "")
                    .split()[0]
                )

                try:
                    reviews = int(text)
                    break
                except Exception:
                    pass

        # ---------- Image ----------
        image = ""

        image_selectors = [
            "#landingImage",
            "#imgTagWrapperId img",
        ]

        for selector in image_selectors:
            tag = soup.select_one(selector)

            if tag:
                image = (
                    tag.get("src")
                    or tag.get("data-old-hires")
                    or ""
                )

                if image:
                    break

        print("------------ SCRAPER DEBUG ------------")
        print("TITLE   :", title)
        print("PRICE   :", price)
        print("RATING  :", rating)
        print("REVIEWS :", reviews)
        print("IMAGE   :", image)
        print("---------------------------------------")

        return {
            "title": title,
            "price": price,
            "rating": rating,
            "reviews": reviews,
            "image": image,
        }