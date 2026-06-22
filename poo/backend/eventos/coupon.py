from datetime import datetime
from decimal import Decimal
from event import Event
from coupon import Coupon

class Coupon:
    def __init__(self, title: str, expires_at: Decimal, discout: Decimal):
        self.tilte = title
        self.expire_at = expires_at
        self.discout = discout
        
    @classmethod
    def create_event(cls, data: dict):
        new_event = Event(
            title = data ["title"],
            description = data ['description'],
            value = data ['value'],
            expiration_data = data ['expiration_data']
        )
        new_coupon = cls(data["title"], data["expires_at"], data["discount"])
        return new_coupon
    
    def add_coupon(self, coupon: Coupon):
        self.coupon.append(coupon)

    coupon1 = Coupon("super25",
    Decimal(datetime(2026, 7, 28).timestamp()),
    Decimal("0.35")
)