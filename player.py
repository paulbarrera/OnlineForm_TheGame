# Implement a "master loop" console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program


class Player:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), font=("Arial", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()


player = Player