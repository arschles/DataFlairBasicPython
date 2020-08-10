#imports
import random   

class RPS:
    def __init__(self, user_input):
        self.user_input = user_input.lower()
        self.rock = "rock"
        self.paper = "paper"
        self.scissors = "scissors"

        if self.user_input not in {self.rock,self.scissors,self.paper}:
            raise ValueError("Please choose either rock, paper or scissors")

        self.game_input = random.choice([self.rock,self.paper,self.scissors])

    def game(self):
        print(f"opponent picked {self.game_input}")

        if self.user_input == self.game_input:
            return print("It's a Draw!")
        elif self.user_input == self.scissors and self.game_input == self.rock:
            return print("you lose")
        elif self.user_input == self.scissors and self.game_input == self.paper:
            return print("you win")
        elif self.user_input == self.rock and self.game_input == self.paper:
            return print("you lose")
        elif self.user_input == self.rock and self.game_input == self.scissors:
            return print("you lose")
        elif self.user_input == self.paper and self.game_input == self.scissors:
            return print("you lose")
        elif self.user_input == self.paper and self.game_input == self.rock:
            return print("you lose")
        else:
            return print("Game brok")


if __name__ == "__main__":
    user_input = input("type what you want to play with: (rock, paper, or scissors) ")
    x = RPS(user_input)
    x.game()
