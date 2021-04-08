class Wolf: #superclass
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):#class
        print("Grr...")

class Dog(Wolf):#subclass
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()

'''
-------------------------------------------------------------------------------------------------------
'''

class Enemy:
  name = ""
  lives = 0
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(f'{self.name} has {self.lives} lives')

class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)

class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == 'exit':
        break
    if x == "laser":
      a.hit()
    if x == "gun":
      m.hit()
      

