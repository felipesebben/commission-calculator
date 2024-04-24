from dotenv import load_dotenv

from config.config_loader import load_config
from modules.calculator import CommissionCalculator

load_dotenv(".env.dev")
config = load_config("COMMISSION_CONFIG")["commission_rates"]

# Add user input
while True:
    try:
        sales_amount = float(input("Enter the sales amount: $"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        n_salespeople = int(
            input(
                f"Enter the number of salespeople. \nValid entries:\n - {'\n - '.join(config.keys())}\n "
            )
        )
        if str(n_salespeople) not in config.keys():
            raise ValueError(
                f"Invalid number of salespeople. Choose between:\n - {'\n - '.join(config.keys())}."
            )
        break
    except ValueError as e:
        print(e)

while True:
    try:
        location = input(
            f"Enter the location. \nValid entries:\n - {'\n - '.join(config[str(n_salespeople)].keys())}\n "
        )
        if location not in config[str(n_salespeople)].keys():
            raise ValueError(
                f"Invalid location. Choose between:\n - {'\n - '.join(config[str(n_salespeople)].keys())}."
            )
        calculator = CommissionCalculator(sales_amount, n_salespeople, location)
        break
    except ValueError as e:
        print(e)

# Create an instance of the calculator
# calculator = CommissionCalculator(sales_amount, n_salespeople, location)

# Calculate the commission
commission = calculator.calculate_commission()
print(
    f"""
      Output:
        - Sales amount: ${sales_amount:.2f}
        - Number of salespeople: {n_salespeople}
        - Location: {location}
        - Commission rate: {calculator.get_commission_rate() * 100:.2f}%
      Estimated commission: ${commission:.2f}"""
)
