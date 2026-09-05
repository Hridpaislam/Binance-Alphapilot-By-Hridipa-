import requests


BINANCE_API = "https://api.binance.com"


def get_price(symbol):
    """
    Return the current Binance price for a symbol.
    """

    response = requests.get(
        f"{BINANCE_API}/api/v3/ticker/price",
        params={"symbol": symbol},
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return float(data["price"])


def get_24h_stats(symbol):
    """
    Return 24-hour market statistics.
    """

    response = requests.get(
        f"{BINANCE_API}/api/v3/ticker/24hr",
        params={"symbol": symbol},
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return {
        "symbol": symbol,
        "price": float(data["lastPrice"]),
        "change_percent": float(data["priceChangePercent"]),
        "volume": float(data["volume"]),
        "high": float(data["highPrice"]),
        "low": float(data["lowPrice"]),
    }