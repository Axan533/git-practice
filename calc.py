class CompoundInterest:
    """Calculate compound interest year by year."""

    def __init__(self, principal, rate, years):
        self.principal = principal   # Principal amount
        self.rate = rate             # Annual interest rate
        self.years = years           # Number of years

    def calculate(self):
        amount = self.principal
        for year in range(1, self.years + 1):
            amount = amount * (1 + self.rate)
            print(f"Year {year}: {amount:.2f} Yuan")


if __name__ == "__main__":
    principal = float(input("Enter principal: "))
    rate = float(input("Enter annual rate (e.g. 0.05): "))
    years = int(input("Enter years: "))
    CompoundInterest(principal, rate, years).calculate()