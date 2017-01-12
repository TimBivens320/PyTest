from unittest import TestCase

from objectmodel.enums.CreditCardType import CreditCardType


class TestCreditCardType(TestCase):
    def test_text(self):
        self.assertEquals("Visa", CreditCardType.VISA.text)
        self.assertEquals("MasterCard", CreditCardType.MASTERCARD.text)

    def test_abbreviation(self):
        self.assertEquals("V", CreditCardType.VISA.abbreviation)
        self.assertEquals("MC", CreditCardType.MASTERCARD.abbreviation)

    def test_get(self):
        self.assertEquals(CreditCardType.get("V"), CreditCardType.VISA)
        self.assertEquals(CreditCardType.get("MC"), CreditCardType.MASTERCARD)

        self.assertEquals(CreditCardType.get("v"), CreditCardType.VISA)
        self.assertEquals(CreditCardType.get("mc"), CreditCardType.MASTERCARD)

        self.assertIsNone(CreditCardType.get("ZZ"))
