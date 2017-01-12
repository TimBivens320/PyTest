from logic.credit_card_validation.validators.MasterCardValidator import MasterCardValidator
from logic.credit_card_validation.validators.VisaValidator import VisaValidator
from model.enums.CreditCardType import CreditCardType


class CreditCardValidatorFactory(object):
    @staticmethod
    def get(credit_card):
        validation_services = {CreditCardType.VISA: VisaValidator,
                               CreditCardType.MASTERCARD: MasterCardValidator}
        return validation_services[credit_card.credit_card_type]
