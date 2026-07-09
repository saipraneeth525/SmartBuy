import requests
from bs4 import BeautifulSoup

from app.scrapers.base import BaseScraper
from app.scrapers.utils import clean_price


class FlipkartScraper(BaseScraper):

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "en-IN,en;q=0.9",
        "Referer": "https://www.google.com/",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
    }

    def scrape(self, url: str):

        response = requests.get(
            url=url,
            headers=self.HEADERS,
            timeout=20,
            allow_redirects=True,
        )

        print("=" * 60)
        print("STATUS CODE :", response.status_code)
        print("FINAL URL   :", response.url)
        print("=" * 60)

        response.raise_for_status()

        return BeautifulSoup(
            response.text,
            "lxml",
        )

    def extract(self, url: str):

        soup = self.scrape(url)

        # Save HTML for debugging
        with open("flipkart.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())

        print("Saved flipkart.html")

        title = ""
        price = 0
        rating = 0.0
        reviews = 0
        image = ""

        # ---------------- TITLE ----------------

        title_selectors = [
            "span.VU-ZEz",
            "span.B_NuCI",
            "h1._6EBuvT",
            "h1",
        ]

        for selector in title_selectors:
            tag = soup.select_one(selector)

            if tag:
                title = tag.get_text(strip=True)
                break

        # ---------------- PRICE ----------------

        price_selectors = [
            "div.Nx9bqj",
            "div._30jeq3",
            "div._16Jk6d",
            "div.CxhGGd",
        ]

        for selector in price_selectors:

            tag = soup.select_one(selector)

            if tag:
                price = clean_price(tag.get_text())

                if price > 0:
                    break

        # ---------------- RATING ----------------

        rating_selectors = [
            "div.XQDdHH",
            "div._3LWZlK",
        ]

        for selector in rating_selectors:

            tag = soup.select_one(selector)

            if tag:
                try:
                    rating = float(tag.get_text())
                    break
                except Exception:
                    pass

        # ---------------- REVIEWS ----------------

        review_selectors = [
            "span.Wphh3N",
            "span._2_R_DZ",
        ]

        for selector in review_selectors:

            tag = soup.select_one(selector)

            if tag:

                text = tag.get_text()

                digits = "".join(
                    ch if ch.isdigit() else " "
                    for ch in text
                ).split()

                if digits:
                    reviews = int(digits[0])
                    break

        # ---------------- IMAGE ----------------

        image_selectors = [
            "img._396cs4",
            "img.DByuf4",
            "img._53J4C-",
            "img",
        ]

        for selector in image_selectors:

            tag = soup.select_one(selector)

            if tag:

                image = (
                    tag.get("src")
                    or tag.get("data-src")
                    or ""
                )

                if image:
                    break

        print("\n========== FLIPKART ==========")
        print("TITLE   :", title)
        print("PRICE   :", price)
        print("RATING  :", rating)
        print("REVIEWS :", reviews)
        print("IMAGE   :", image)
        print("==============================\n")

        return {
            "title": title,
            "price": price,
            "rating": rating,
            "reviews": reviews,
            "image": image,
        }