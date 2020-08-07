#imports

class HangMan:
    def __init__(self,  guess_word):
        self.guess_word = guess_word
        self.blank_template = '_' * len(guess_word)
        self.guessed_attempts = 0
        self.guessed_letters = []

    def guesses(self,user_letter):
        if user_letter in self.guess_word:
            letter_position = [pos for pos, char in enumerate(self.guess_word) if char == user_letter]
            for i in letter_position:
                blank_template_list = list(self.blank_template)
                blank_template_list[i] = user_letter    
                self.blank_template = ''.join(blank_template_list)
            print(self.blank_template)
            print(f"Used letters {self.guessed_letters}")

        else:
            self.guessed_attempts += 1
            self.guessed_letters.append(user_letter)
            self.show_hangman()
            print(f"Used letters: {self.guessed_letters}")
            
    def show_hangman(self):
        if self.guessed_attempts == 1:
            print("   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        elif self.guessed_attempts ==2: 
            print("   _____ \n"
                "  |      |\n"
                "  |      |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

        elif self.guessed_attempts ==3: 
            print("   _____ \n"
                "  |      |\n"
                "  |      |\n"
                "  |      |\n"
                "  |      o\n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

        
        elif self.guessed_attempts ==4: 
            print("   _____ \n"
                "  |      |\n"
                "  |      |\n"
                "  |      |\n"
                "  |      o\n"
                "  |      |\n"
                "  |      \n"
                "__|__\n")


        elif self.guessed_attempts ==5: 
            print("   _____ \n"
                "  |      |\n"
                "  |      |\n"
                "  |      |\n"
                "  |      o\n"
                "  |     /|\ \n"
                "  |     /\ \n"
                "__|__\n")

if __name__ == "__main__":
    x = HangMan("fish") 
    while x.guessed_attempts < 5:
        if '_' in x.blank_template:
            user_guess = input("Guess a letter ")
            x.guesses(user_guess)
        else:
           print("you win")
           break





