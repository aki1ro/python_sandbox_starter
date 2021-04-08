class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        while self._lives > 0:
            self._lives = self._lives - 1
            if self._lives == 0:
               print("Game Over")


    # one underscore is = to weakly private vs double underscore meaning the data is strongly private
    # to call private data outside the class you would:
    # ie: print(t.Test_egg) for weakly private vs print(t._Test__egg) for strongly private

p = Player("Cyberpunk77", 3)
p.hit()
p.hit()
p.hit()



