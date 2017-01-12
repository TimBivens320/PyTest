from SpecificFile import SpecificFile
from logic.credit_card_validation.CreditCardValidatorFactory import CreditCardValidatorFactory
from model.enums.CreditCardType import CreditCardType
from model.enums.State import State

someObject = SpecificFile("dummy")

someObject.printSomething(someObject.name)

state = State.MISSISSIPPI
credit_card_type = CreditCardType.VISA

print(state.text)
print(state.abbreviation)
print(credit_card_type.abbreviation)

credit_card_validator = CreditCardValidatorFactory.get(CreditCardType.VISA)
credit_card_validator.is_valid()

