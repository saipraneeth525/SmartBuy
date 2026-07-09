from urllib.parse import urlparse


def detect_store(url: str) -> str:
    domain = urlparse(url).netloc.lower()

    if "amazon" in domain:
        return "amazon"

    if "flipkart" in domain:
        return "flipkart"

    if "myntra" in domain:
        return "myntra"

    if "ajio" in domain:
        return "ajio"

    if "croma" in domain:
        return "croma"

    return "generic"