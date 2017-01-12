from objectmodel.enums.State import State
from SpecificFile import SpecificFile

someObject = SpecificFile("dummy")

someObject.printSomething(someObject.name)

state = State.MISSISSIPPI

print (state.text)
print (state.abbreviation)