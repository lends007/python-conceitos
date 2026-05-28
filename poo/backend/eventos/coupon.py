from datetime import datetime
from decimal import Decimal
class Coupon:
    def __init__(self, title: str, expires_at: Decimal, discout: Decimal):
        self.tilte = title
        self.expire_at = expires_at
        self.discout = discout
        
    def __repr__(self):
        return f'{self.tilte},\n {self.codigo},\n{self.discout}'