'''
Testing the module
Karina Hoff, 2018
'''
#!/usr/bin/python3

import pytest
from exercises.zoo.zoo import Animal, Bird, Mammal, Parrot, Penguin, Canine, Feline, Dog, HouseCat, BobCat

##Try to change attributes of the instantiated animals? (need get/set)
class TestAnimalsMethods:
    '''Testing module '''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        
    def test_Animal(self):
        with pytest.raises(TypeError) as excinfo:
            animal = Animal('Mammal', 1, 'Black')
        exception_message = excinfo.value.args[0]
        assert exception_message == "Can't instantiate abstract class Animal with abstract methods __init__, sound"
        
    def test_Bird(self):
        with pytest.raises(TypeError) as excinfo:
            bird = Bird('Avian', 1, 'Blue', True)
        exception_message = excinfo.value.args[0]
        assert exception_message == "Can't instantiate abstract class Bird with abstract methods __init__, sound"

    def test_Mammal(self):
        with pytest.raises(TypeError) as excinfo:
            mammal = Mammal('Bear', 1, 'Black', 'Land')
        exception_message = excinfo.value.args[0]
        assert exception_message == "Can't instantiate abstract class Mammal with abstract methods __init__, sound"
        
    def test_Parrot(self):
        parrot = Parrot(5, 'Rainbow', True)
        assert parrot.sound() == "'Polly wants a cracker'"
        parrot = Parrot(5, 'Rainbow', False)
        assert parrot.sound() == "nothing"
        assert parrot.__str__() == "Flying Rainbow Parrot (5 yo)"

    def test_Penguin(self):
        penguin = Penguin(2, 'Black and White')
        assert penguin.sound() == "nothing"
        assert penguin.__str__() == "Non-flying Black and White Penguin (2 yo)"

    def test_Canine(self):
        with pytest.raises(TypeError) as excinfo:
            canine = Canine('Dog', 7, 'Brown', 'House')
        exception_message = excinfo.value.args[0]
        assert exception_message == "Can't instantiate abstract class Canine with abstract methods __init__, sound"
            
    def test_Feline(self):
        with pytest.raises(TypeError) as excinfo:
            feline = Feline('Mammal', 1, 'Grey')
        exception_message = excinfo.value.args[0]
        assert exception_message == "Can't instantiate abstract class Feline with abstract methods __init__"
        
    def test_Dog(self):
        dog = Dog(7, 'Brown')
        assert dog.sound() == "Woof!"
        assert dog.__str__() == "Brown Dog (7 yo)"

    def test_HouseCat(self):
        houseCat = HouseCat(10, 'Grey')
        assert houseCat.sound() == "Meow!"
        assert houseCat.__str__() == "Grey House Cat (10 yo)"

    def test_BobCat(self):
        #Correct values for habitat
        for habitat in ['Land', 'Sea', 'Air', 'Tree']:
            bobCat = BobCat(3, 'Brown', habitat)
            assert bobCat.sound() == "Meow!"
            assert bobCat.__str__() == ("Brown {} Bobcat (3 yo)" .format(habitat))
        #Incorrect value for habitat
        with pytest.raises(ValueError) as excinfo:
            bobCat = BobCat(3, 'Brown', 'House')
        exception_message = excinfo.value.args[0]
        assert exception_message == "Incorrect habitat value"     

if __name__ == '__main__':
    pytest.main(['test_zoo.py'])
