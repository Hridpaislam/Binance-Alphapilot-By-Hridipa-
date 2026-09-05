from tools.risk_engine import risk_level


def analyze_portfolio(portfolio):
    """
    Analyze portfolio allocation.
    """

    risk = risk_level(portfolio)

    return {
        "portfolio": portfolio,
        "risk_level": risk["level"],
        "largest_position": risk["largest_asset"],
        "largest_allocation": risk["largest_allocation"]
    }


if __name__ == "__main__":

    example_portfolio = {
        "BTC": 0.52,
        "ETH": 0.28,
        "BNB": 0.12,
        "OTHER": 0.08
    }

    result = analyze_portfolio(example_portfolio)

    print(result)