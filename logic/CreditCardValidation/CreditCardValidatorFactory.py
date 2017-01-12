from logic.CreditCardValidation.Validators.MasterCardValidator import MasterCardValidator
from logic.CreditCardValidation.Validators.VisaValidator import VisaValidator
from objectmodel.enums.CreditCardType import CreditCardType


class CreditCardValidatorFactory(object):
    @staticmethod
    def get(credit_card):
        validation_services = {CreditCardType.VISA: VisaValidator,
                               CreditCardType.MASTERCARD: MasterCardValidator}
        return validation_services[credit_card.credit_card_type]
