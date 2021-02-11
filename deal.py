from abc import ABC


class Sell(ABC):
    def __init__(self, price_per_meter, discountable=False, convertable=False, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f'sell {self.price_per_meter}')


class Rent(ABC):
    def __init__(self, initial_price, monthly_price, discountable=False, convertable=False, *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f'initial price:  {self.initial_price} \t monthly_price {self.monthly_price}')
