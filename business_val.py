class BusinessValuation:
    def __init__(self):
        self.__initial_revenue = 0.0
        self.__final_revenue = 0.0
        self.__years = 1
        self.__cost_of_capital = 0.1  # default 10%

    def set_initial_revenue(self, value):
        self.__initial_revenue = float(value)

    def set_final_revenue(self, value):
        self.__final_revenue = float(value)

    def set_years(self, value):
        self.__years = int(value)

    def set_cost_of_capital(self, value):
        self.__cost_of_capital = float(value)

    def calculate_cagr(self):
        cagr = ((self.__final_revenue / self.__initial_revenue) ** (1 / self.__years)) - 1
        return cagr

    def calculate_valuation(self):
        cagr = self.calculate_cagr()
        terminal_cash_flow = self.__final_revenue * (1 + cagr)
        dcf = terminal_cash_flow / ((1 + self.__cost_of_capital) ** self.__years)
        return dcf

    def __str__(self):
        return (f"Initial Revenue: ${self.__initial_revenue:,.2f}\n"
                f"Final Revenue: ${self.__final_revenue:,.2f}\n"
                f"Years: {self.__years}\n"
                f"Cost of Capital: {self.__cost_of_capital:.2%}\n"
                f"CAGR: {self.calculate_cagr():.2%}\n"
                f"Estimated Valuation: ${self.calculate_valuation():,.2f}")
