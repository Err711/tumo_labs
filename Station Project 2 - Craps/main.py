import random


class Game:
    def __init__(self, dice_1, dice_2):
        self.dice_1 = dice_1
        self.dice_2 = dice_2

    @staticmethod
    def player_win(dice_1, dice_2):
        if dice_1 + dice_2 == 7 or 11:
            return "You Win!"
        if dice_1 + dice_2 == 2 or 3 or 12:
            return "Craps! \n Casino Wins!"

    def start_game(self):
        start = 'go'  # input('If you ready, type "go". ')
        while start == 'go' or start == 'Go':
            return self.dice_1, self.dice_2
        else:
            raise ValueError("Type 'go' for start game. ")


user_dice_1 = random.randint(1, 6)
user_dice_2 = random.randint(1, 6)
# user_input = input('If you ready, type "go". ')
a = Game(user_dice_1, user_dice_2)
print(a.start_game())
