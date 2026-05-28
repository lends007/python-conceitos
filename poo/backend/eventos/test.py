from .user import User
from .coupon import Coupon
from datetime import datetime
from decimal import Decimal
class Event:
    def __init__(self, title: str, description: str, price: Decimal, date: datetime, location: str, user: User):
        self.title = title
        self.description = description
        self.price = price
        self.date = date
        self.location = location
        self.user = user 

    def __repr__(self):
        return f'{self.title},\n {self.description},\n {self.price},\n {self.date},\n {self.location},\n {self.user}'

    def apply_discount(self, coupon: Coupon):
        new_price = self.price - (self.price * coupon.discout)
        self.price = new_price

user1 = User('kleber', 'bletinho232@gmail.com', 'kekeber21343')    
coupon1 = Coupon('super25', datetime(2026, 7, 28), 0.35)
print(coupon1)
event1 = Event('evento legar', '', Decimal (350), datetime(2026, 7, 9), 'curitiba', user1)
print(event1)
event1.apply_discount(coupon1)
print(event1)


evento3 = Event.create_event(
    {
        'title': 'hackaton',
        'description': 'vai ter jogo',
        'regras': {
            'regra1': 'nao pode briga',
            'regra2': 'nao pode faca'
        }
    }
)
