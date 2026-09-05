def create_strategy(symbol, market_data):
    """
    Create a simple rule-based market hypothesis.

    This is intentionally not financial advice
    and does not execute trades.
    """

    change = market_data["change_percent"]

    if change > 3:
        scenario = "Strong positive momentum"

    elif change > 0:
        scenario = "Positive momentum"

    elif change < -3:
        scenario = "Strong negative momentum"

    else:
        scenario = "Weak or neutral momentum"

    return {
        "symbol": symbol,
        "scenario": scenario,
        "24h_change": change,
        "action": "REVIEW",
        "execution": False
    }