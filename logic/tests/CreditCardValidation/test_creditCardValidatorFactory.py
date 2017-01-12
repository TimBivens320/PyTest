from unittest import TestCase

from logic.CreditCardValidation.CreditCardValidatorFactory import CreditCardValidatorFactory
from logic.CreditCardValidation.Validators.MasterCardValidator import MasterCardValidator
from logic.CreditCardValidation.Validators.VisaValidator import VisaValidator
from objectmodel.CreditCard import CreditCard
from objectmodel.enums.CreditCardType import CreditCardType


class TestCreditCardValidatorFactory(TestCase):
    @staticmethod
    def setup_credit_card(credit_card_type):
        return CreditCard(credit_card_type)

    def test_visa(self):
        credit_card = self.setup_credit_card(CreditCardType.VISA)
        self.assertIs(VisaValidator, CreditCardValidatorFactory.get(credit_card))

    def test_mastercard(self):
        credit_card = self.setup_credit_card(CreditCardType.MASTERCARD)
        self.assertIs(MasterCardValidator, CreditCardValidatorFactory.get(credit_card))
