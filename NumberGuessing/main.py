#imports
import random
    

class NumberGuessing:
    def __init__(self, user_input, random_number):
        self.user_input = user_input 
        self.random_number = random_number 

        try:
            self.user_input = int(self.user_input)
        except:
            raise TypeError("Not a numer")

    def match_numbers(self):
        if self.user_input == self.random_number:
            return True 
        else:
            return False 

if __name__ == '__main__':
    count = 0
    random_number = random.randint(0,10)
    while count < 3:
        user_input = input("Pick a number")
        x = NumberGuessing(user_input, random_number)
        if x.match_numbers():
            print("You got the correct number")
            break

        else:
            if x.user_input < random_number:
                print("you gotta guess higher")
            else:
                print("you gotta guess lower")
            count +=1
            print(f"wrong number! {count}/3")


