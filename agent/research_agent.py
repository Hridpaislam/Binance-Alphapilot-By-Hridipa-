from tools.market_data import get_24h_stats


def research(symbol):
    """
    Collect market information and create
    an explainable research summary.
    """

    data = get_24h_stats(symbol)

    change = data["change_percent"]

    if change > 0:
        direction = "up"

    elif change < 0:
        direction = "down"

    else:
        direction = "flat"

    return {
        "symbol": symbol,
        "price": data["price"],
        "direction": direction,
        "change_percent": change,
        "volume": data["volume"],
        "high": data["high"],
        "low": data["low"]
    }


if __name__ == "__main__":

    result = research("BTCUSDT")

    print("\nBINANCE ALPHAPILOT RESEARCH")
    print("----------------------------")

    for key, value in result.items():
        print(f"{key}: {value}")