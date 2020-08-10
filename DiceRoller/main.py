#imports
import random

class DiceRoller:
    def __init__(self, user_option):
        self.user_option = user_option
        self.quit_words = ["stop","quit","done","finished"]

    def game(self):
        while self.user_option not in self.quit_words:
            dice_roll = random.randint(1,6)
            print(dice_roll)

            self.user_option = input("play again? ")

        

if __name__ == "__main__":
    user_option = input("Ready to roll? ")
    x = DiceRoller(user_option)
    x.game()
    