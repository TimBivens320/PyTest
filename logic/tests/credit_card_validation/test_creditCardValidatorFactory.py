from unittest import TestCase

from logic.credit_card_validation.CreditCardValidatorFactory import CreditCardValidatorFactory
from logic.credit_card_validation.validators.MasterCardValidator import MasterCardValidator
from logic.credit_card_validation.validators.VisaValidator import VisaValidator
from model.CreditCard import CreditCard
from model.enums.CreditCardType import CreditCardType


class TestCreditCardValidatorFactory(TestCase):
    @staticmethod
    def setup_credit_card(credit_card_type, card_number):
        return CreditCard(credit_card_type, card_number)

    def test_visa(self):
        credit_card = self.setup_credit_card(CreditCardType.VISA, None)
        self.assertIs(VisaValidator, CreditCardValidatorFactory.get(credit_card))

    def test_mastercard(self):
        credit_card = self.setup_credit_card(CreditCardType.MASTERCARD, None)
        self.assertIs(MasterCardValidator, CreditCardValidatorFactory.get(credit_card))
