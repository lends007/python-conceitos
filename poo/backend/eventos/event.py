from user import User
from coupon import Coupon
from datetime import datetime
from decimal import Decimal

class Event:
    def __init__(self, title: str, description: str, date: datetime, regra: str, event: str, user: User):
        self.title = title
        self.description = description
        self.date = date
        self.user = user 
        
 
    def __repr__(self):
        return f'{self.title},\n {self.description},\n {self.price},\n {self.date},\n {self.location},\n {self.user}'

    @classmethod
    def create_event(cls, data: dict):
        new_event = Event(
            title = data['title'],
            description = data.description,
            users = [],
            regras = data.regras

        )