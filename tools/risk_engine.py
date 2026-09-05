def calculate_concentration(portfolio):
    """
    Calculate the largest portfolio allocation.
    
    Example:
    {
        "BTC": 0.50,
        "ETH": 0.30,
        "BNB": 0.20
    }
    """

    if not portfolio:
        return {
            "largest_asset": None,
            "largest_allocation": 0
        }

    largest_asset = max(
        portfolio,
        key=portfolio.get
    )

    return {
        "largest_asset": largest_asset,
        "largest_allocation": portfolio[largest_asset]
    }


def risk_level(portfolio):
    """
    Simple concentration-based risk assessment.
    """

    concentration = calculate_concentration(portfolio)

    allocation = concentration["largest_allocation"]

    if allocation >= 0.60:
        level = "HIGH"

    elif allocation >= 0.40:
        level = "MEDIUM"

    else:
        level = "LOW"

    return {
        "level": level,
        "largest_asset": concentration["largest_asset"],
        "largest_allocation": allocation
    }