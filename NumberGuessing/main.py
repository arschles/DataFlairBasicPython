#imports
import random
    

class NumberGuessing:
    def __init__(self, user_input):
        self.user_input = user_input 
        self.random_number = random.randint(0,10) 

        try:
            self.user_input = int(self.user_input)
        except:
            raise TypeError("Not a numer")

    def match_numbers(self):
        if self.user_input == self.random_number:
            return print("you selected corectly")
        else:
            return print("you're wrong try again")

if __name__ == '__main__':
    user_input = input("Pick a number")
    x = NumberGuessing(user_input)
    x.match_numbers()


