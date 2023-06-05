class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    
    def get_friends(self):
        return self.friends
    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    
    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(f"{self.name} is {diff} years older than  {other.name}")  
        else:
            print(f"{self.name} is {diff} years younger than   {other.name} ")
    def __str__(self):
        return f"Person name: {self.name}, person age {self.age} "
    
class Student(Person):
    def __init__(self, name, age, major = None)
        Person.__init__(self,name,age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):

        r = random.random()
        if r < 0.25:
            print("I have hımework")
        elif 0.25 <= r <= 0.5:
            print("I need to sleep")

        elif 0.5 <= r <= 0.75:
            print("I need to eat")

        else:
            print("I want to play")


class Animal(object):
  def __init__(self, age):
    self.age = age
    self.name = None
  def set_name(self, newname=""):
    self.name = newname
# class instance method
class Cat(Animal):
  def speak(self):
    print("meow")
    jelly = Cat(4)
    jelly.speak()
    jelly.set_name('Jelly')

john = Student('John', 25, 'IT Dept')
jack = Student('Jack', 27, 'IT Dept')
print(john)
john.speak()
print(jack)
jack.speak()
john.age_diff(jack)
jack.add_friend('John')
print(jack.get_friends())
print(john+jack)
print(john == jack)