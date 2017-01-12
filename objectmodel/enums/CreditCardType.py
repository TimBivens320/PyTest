from enum import Enum


class CreditCardType(Enum):
    VISA = ("Visa", "V")
    MASTERCARD = ("MasterCard", "MC")

    def __init__(self, text, abbreviation):
        self.text = text
        self.abbreviation = abbreviation

    @classmethod
    def get(cls, abbreviation):
        for credit_card_type in cls:
            if credit_card_type.abbreviation == abbreviation.upper():
                return credit_card_type
        return None
