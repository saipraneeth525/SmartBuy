import re


def clean_price(text: str) -> float:
    """
    Converts:
    ₹79,999
    ₹ 79,999.00
    79,999

    into

    79999.0
    """

    if not text:
        return 0

    text = re.sub(r"[^\d.]", "", text)

    try:
        return float(text)
    except ValueError:
        return 0