from enum import Enum


class OrderStatus(Enum):
    """string enumeration that represents the status of an order, possible values of 'pending', 'completed', and 'cancelled'"""

    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    @classmethod
    def is_valid_status(cls, status: str):
        return status.lower() in [i.name.lower() for i in cls]




