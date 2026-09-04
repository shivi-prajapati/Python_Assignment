'''Assignment 3: E-Commerce Currency Converter'''
class PriceAmount:
    def __init__(self,value,currency):
        self.value=value
        self.currency=currency.upper()

    def __str__(self):
        return f"{self.currency} {round(self.value,2)}"

    def  __repr__(self):
        return f"PriceAmount(value={self.value},currency={self.currency!r})"

    def __add__(self, other):    
        if not isinstance(other,PriceAmount):
            return NotImplemented
        if self.currency!=other.currency:
            raise ValueError(f"Cannot add price amounts with different currencies: {self.currency} and {other.currency}'")
        else:
            return PriceAmount(self.value + other.value,self.currency)

    def __eq__(self, other):
        if not isinstance(other,PriceAmount):
            return False
        return self.currency==other.currency and self.value==other.value
def main():
    p1 = PriceAmount(19.99, "usd")
    p2 = PriceAmount(10.01, "USD")
    p3 = PriceAmount(15.00, "EUR")

    print(str(p1))      # Output: USD 19.99
    print(repr(p1))     # Output: PriceAmount(value=19.99, currency='USD')

    total = p1 + p2
    print(str(total))   # Output: USD 30.00

    print(p1== PriceAmount(19.99, "USD")) # Output: True
    
main()