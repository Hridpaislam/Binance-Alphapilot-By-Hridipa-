import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_price(symbol):
    """
    Get the current Binance market price.
    """

    url = "https://api.binance.com/api/v3/ticker/price"

    response = requests.get(
        url,
        params={"symbol": symbol},
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return float(data["price"])


def market_snapshot():
    """
    Collect a simple market snapshot.
    """

    symbols = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT"
    ]

    result = {}

    for symbol in symbols:
        try:
            result[symbol] = get_price(symbol)
        except Exception as error:
            result[symbol] = f"Error: {error}"

    return result


def generate_report():
    """
    Generate a simple AI-agent style market report.
    """

    market = market_snapshot()

    print("\n================================")
    print("      BINANCE ALPHAPILOT")
    print("================================\n")

    print("MARKET SNAPSHOT\n")

    for symbol, price in market.items():
        print(f"{symbol}: {price}")

    print("\n--------------------------------")
    print("AGENT ANALYSIS")
    print("--------------------------------\n")

    print(
        "The agent collected current market prices "
        "and prepared a basic market snapshot."
    )

    print(
        "\nNext step: connect this workflow to "
        "Agent OS tools and an AI reasoning model."
    )


if __name__ == "__main__":
    generate_report()