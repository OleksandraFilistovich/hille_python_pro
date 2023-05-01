class Price:
    # exchange rates on 30.04
    rates_to_usd = {"uah": 0.027, "gbp": 1.26, "usd": 1.0}

    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def __str__(self) -> str:
        return f"{self.amount} {self.currency}"

    # doesn't change original object and returns new, converted one
    def converted(self, new_currency: str) -> "Price":
        if self.currency == "usd":
            new_amount = self.amount
        else:
            new_amount = self.amount * self.rates_to_usd[self.currency]
        new_amount /= self.rates_to_usd[new_currency]
        return Price(round(new_amount, 2), new_currency)

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(self.amount + other.amount, self.currency)
        else:
            converted_other = other.converted(self.currency)
            return Price(self.amount + converted_other.amount, self.currency)

    def __sub__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(self.amount - other.amount, self.currency)
        else:
            converted_other = other.converted(self.currency)
            return Price(self.amount - converted_other.amount, self.currency)

    # used to change class variable, so can be called only via class
    @classmethod
    def exchange_rates(cls, sold_currency: str, rate: float) -> None:
        """Function can add or change exchange rates."""
        cls.rates_to_usd[sold_currency] = rate
        print(f"new rates: {cls.rates_to_usd}\n")


def main():
    Price.exchange_rates(sold_currency="eur", rate=0.025)

    apple = Price(5, "uah")
    peach = Price(10, "uah")
    discount = Price(2.5, "uah")

    chocolate = Price(1, "usd")
    waffle = Price(1.5, "gbp")

    print(f"uah + uah: {apple + peach}")
    print(f"uah - uah: {peach - discount}\n")

    print(f"uah + usd: {peach + chocolate} (single conversion)")
    print(f"gbp + uah: {waffle + peach} (double conversion)")
    print(f"usd + uah: {chocolate + peach} (double conversion)")


if __name__ == "__main__":
    main()
