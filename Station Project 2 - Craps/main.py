import random
import time


class Game:
    def __init__(self, dice_1, dice_2):
        self.dice_1 = dice_1
        self.dice_2 = dice_2
        self.dice_sum = dice_1 + dice_2
        self.user_numbers = [7, 11]
        self.craps = [2, 3, 12]
        self.goal_numbers = [4, 5, 6, 8, 9, 10]

    def game_process(self):

        if self.dice_sum in self.user_numbers:
            return "You Won!"
        elif self.dice_sum in self.craps:
            return "Craps! \nCasino Wins!"
        else:  # elif self.dice_sum in self.goal_numbers:
            print(f"Now your goal number is {self.dice_sum}")
            time.sleep(0.1)
            while True:
                self.dice_1 = random.randint(1, 6)
                self.dice_2 = random.randint(1, 6)
                goal_num_sum = self.dice_1 + self.dice_2
                time.sleep(1)
                print(f'{self.dice_1} + {self.dice_2} = {goal_num_sum}')
                if goal_num_sum == self.dice_sum:
                    return 'You won!'
                elif goal_num_sum == 7:
                    return "Craps! \nCasino Wins!"

    def start_game(self):
        start = 'go'  # input('If you ready, type "go". ')
        while start == 'go' or start == 'Go':
            return f'{self.dice_1} + {self.dice_2} = {self.dice_sum}'
        else:
            raise ValueError("Type 'go' for start game. ")


user_dice_1 = random.randint(1, 6)
user_dice_2 = random.randint(1, 6)
# user_input = input('If you ready, type "go". ')
a = Game(user_dice_1, user_dice_2)
print(a.start_game())
print(a.game_process())
