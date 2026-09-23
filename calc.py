class CompoundInterest:                          # Category: Financial Calculation
    def __init__(self, principal, rate, years):  # Constructor method to initialize the principal, rate, and years
        self.principal = principal   # Principal amount
        self.rate = rate             # Annual interest rate
        self.years = years           # Number of years

    def calculate(self):
        amount = self.principal
        for year in range(1, self.years + 1):
            amount = amount * (1 + self.rate)
            print(f"Year {year}: {amount:.2f} Yuan")


if __name__ == "__main__":                        # Entry point of the program
    CompoundInterest(10000, 0.05, 3).calculate()