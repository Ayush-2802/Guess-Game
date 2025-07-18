import random

class GuessGame:
    def __init__(self,min_num=1,max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_num = random.randint(min_num,max_num)
        self.attempts = 0
        self.is_guessed = False

    def welcome(self):
        print(f""" 
  ____                       _____ _            _   _                 _               _ 
 / ___|_   _  ___  ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __| |
| |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| |
| |_| | |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  |_|
 \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)   
----------------------------------------------------------------------------------------   

# Computer has chosen the no. between {self.min_num} to {self.max_num}
# guess the no. in minimu attempts   
# start guessing!!!                                                                                                                                                                                                                                                                                                                  
""")
        
    def user_inp(self):
        try:
            guess = int(input("Guess :"))
            return guess
        except ValueError:
            print("Please enter a valid number")
            return self.user_inp()
        
    def check(self,guess):
        self.attempts+=1

        if guess>self.secret_num:
            print(f"Attempt: {self.attempts}")
            print("Your guess is higher than the number | Try Again")
            print("----------------------------------------------------------------------------------------")
            return "high"
        elif guess <self.secret_num:
            print(f"Attempt: {self.attempts}")
            print("Your guess is lower than the number | Try Again")
            print("----------------------------------------------------------------------------------------")
            return "low"
        else:
            self.is_guessed=True
            print(f"Number Guessed Correctly! | Attempts: {self.attempts}")
            return "Correct"
        
    def play(self):
        self.welcome()
        while not self.is_guessed:
            guess = self.user_inp()
            res = self.check(guess)

            if res == "Correct":
                break

    def reset(self):
        self.secret_num = random.randint(self.min_num,self.max_num)
        self.attempts = 0
        self.is_guessed = False



if __name__ == "__main__":
    game = GuessGame()
    game.play()

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        game.reset()
        game.play()