from config.config_loader import load_config


class CommissionCalculator:
    """
    CommissionCalculator class. It calculates the commission based on the sales amount.
    """

    def __init__(self, sales_amount: float, n_salespeople: int, location: str):
        self.config = load_config("COMMISSION_CONFIG")["commission_rates"]
        self.salespeople_key = str(n_salespeople)

        if self.salespeople_key not in self.config.keys():
            raise ValueError(
                f"Invalid number of salespeople. Choose between {', '.join(self.config.keys())}."
            )

        if location not in self.config[self.salespeople_key].keys():
            raise ValueError(
                f"Invalid location. Choose between {', '.join(self.config[self.salespeople_key].keys())}."
            )
        self.location = location
        self.sales_amount = sales_amount

    def calculate_commission(self) -> float:
        """
        Calculate the commission based on the number of salespeople, location, and sales amount.
        """
        commission_rate = self.get_commission_rate()
        return self.sales_amount * commission_rate

    def get_commission_rate(self) -> float:
        """
        Get the commission rate based on the location and on the number of salespeople.

        Returns:
        - commission_rate: float
        """
        return self.config[self.salespeople_key][self.location]
