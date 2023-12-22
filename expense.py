"""Represents an individual financial expense"""

import uuid
from datetime import datetime, timezone
from tzlocal import get_localzone


class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        local_tz = get_localzone()
        self.created_at = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(local_tz)
        self.updated_at = self.created_at
        
        
    def update(self, title=None, amount=None):
        """Allows updating the title and/or amount, updating the updated_at timestamp"""
        
        self.title = title if title is not None else self.title
        self.amount = amount if amount is not None else self.amount
        local_tz = get_localzone()
        self.updated_at = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(local_tz)
        
        
    def to_dict(self):
        """ Returns a dictionary representation of the expense """
        
        created_at_str = self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        updated_at_str = self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }