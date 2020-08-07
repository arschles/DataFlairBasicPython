#imports
import random
import variables

class Magic8Ball:
    def __init__(self):
        random_num = random.randint(0,20)
        print(variables.responses[random_num])

if __name__ == '__main__':
    user_input = input("ask me a question and I will answer: ")
    x=Magic8Ball()
