from unittest import TestCase

from logic.CreditCardValidation.CreditCardValidatorFactory import CreditCardValidatorFactory
from logic.CreditCardValidation.Validators.MasterCardValidator import MasterCardValidator
from logic.CreditCardValidation.Validators.VisaValidator import VisaValidator
from objectmodel.enums.CreditCardType import CreditCardType


class TestCreditCardValidatorFactory(TestCase):
    def test_get(self):
        self.assertIs(VisaValidator, CreditCardValidatorFactory.get(CreditCardType.VISA))
        self.assertIs(MasterCardValidator, CreditCardValidatorFactory.get(CreditCardType.MASTERCARD))
