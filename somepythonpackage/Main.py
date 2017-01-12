from objectmodel.enums.CreditCardType import CreditCardType
from objectmodel.enums.State import State
from SpecificFile import SpecificFile

someObject = SpecificFile("dummy")

someObject.printSomething(someObject.name)

state = State.MISSISSIPPI
credit_card_type = CreditCardType.VISA

print (state.text)
print (state.abbreviation)
print (credit_card_type.abbreviation)