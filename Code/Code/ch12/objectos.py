
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Eu sou uma pessoa e meu nome é ' + self.name

class DogWalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def walk_the_dogs(self, dogs):
        for dog_name in dogs:
            dogs[dog_name].walk()
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'diz WOOF WOOF')
        else:
            print(self.name, 'diz woof woof')

    def human_years(self):
        years = int(self.age) * 7
        return years

    def walk(self):
        print(self.name, 'está andando')

    def __str__(self):
        return "Eu sou um cachorro chamado " + self.name


class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.is_working = False

    def walk(self):
        if self.is_working:
            print(self.name, 'está ajudando', self.handler, 'a passear.')
        else:
            Dog.walk(self)

    def bark(self):
        if self.is_working:
            print(self.name, 'diz: "Eu não posso latir, estou trabalhando."')
        else:
            Dog.bark(self)


class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee != None:
            print(self.name, 'diz: "Eu não posso latir, tenho um frisbee na boca."')
        else:
            Dog.bark(self)

    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, 'pegou um frisbee', frisbee.color )

    def give(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.name, 'devolve o frisbee', frisbee.color)
            return frisbee
        else:
            print(self.name, 'não tem um frisbee.')
            return None

    def walk(self):
        if self.frisbee != None:
            print(self.name, 'diz: "Eu não posso andar, tenho um frisbee na boca."')
        else:
            Dog.walk(self)

    def __str__(self):
        str = 'Eu sou um cachorro chamado ' + self.name
        if self.frisbee != None:
            str = str + ' e eu tenho um frisbee'
        return str


class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'O frisbee diz: "Eu sou um frisbee ' + self.color + '"'


class Hotel:
    def __init__(self, name):
        self.name = name
        self.kennel = {}

    def check_in(self, dog):
        if isinstance(dog, Dog):
            self.kennel[dog.name] = dog
            print(dog.name, 'fez checkin no', self.name)
        else:
            print('Desculpe, apenas cachorros são permitidos no Hotel.')

    def check_out(self, dog):
        if dog.name in self.kennel:
            temp = self.kennel[dog.name]
            del self.kennel[dog.name]
            print(dog.name, 'fez checkout com sucesso.')
            return temp
        else:
            print('Desculpe,', dog.name, 'não está no hotel.')
            return None

    def bark_time(self):
        for dog_name in self.kennel:
            dog = self.kennel[dog_name]
            dog.bark()

    def walk_time(self):
        for dog_name in self.kennel:
            dog = self.kennel[dog_name]
            dog.walk()

    def hire_walker(self, walker):
        if isinstance(walker, DogWalker):
            self.walker = walker
        else:
            print('Desculpe, contratamos apenas Dog Walkers')

    def walk_with_dogs(self):
        if self.walker != None:
            self.walker.walk_the_dogs(self.kennel)


class Cat():
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name, 'diz: "Meow."')

def test_code():
    codie = Dog('Codie', 12, 38)
    jackson = Dog('Jackson', 9, 12)
    sparky = Dog('Sparky', 2, 14)
    rody = ServiceDog('Rody', 8, 38, 'Joseph')
    rody.is_working = True
    dude = FrisbeeDog('Dude', 5, 20)
    frisbee = Frisbee('vermelho')
    dude.catch(frisbee)
    kitty = Cat('Kitty')

    hotel = Hotel('Doggie Hotel')
    hotel.check_in(codie)
    hotel.check_in(jackson)
    hotel.check_in(sparky)
    hotel.check_in(dude)
    hotel.check_in(rody)
    hotel.check_in(kitty)

    hotel.bark_time()

    joe = DogWalker('Joe')
    hotel.hire_walker(joe)
    hotel.walk_with_dogs()
    hotel.check_out(codie)
    hotel.check_out(jackson)
    hotel.check_out(sparky)
    hotel.check_out(dude)
    hotel.check_out(kitty)


test_code()
