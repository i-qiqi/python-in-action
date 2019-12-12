class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class People():
    def run(self):
        print('People do not extends Animal...')

def run_twice(animal):
    animal.run()
    animal.run()

if __name__ == '__main__':
    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())
    run_twice(People()) # 鸭子类型