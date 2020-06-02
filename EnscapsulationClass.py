class ProtectedCharacterHP:
    def __init__(self):
        self.__privateVar = 100

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = ProtectedCharacterHP()
obj.getPrivate()
obj.setPrivate(100)
obj.getPrivate()
