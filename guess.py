import random 
num = random.randint(1,100)

print(""" 
  ____                       _____ _            _   _                 _               _ 
 / ___|_   _  ___  ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __| |
| |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| |
| |_| | |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  |_|
 \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)   
----------------------------------------------------------------------------------------   

# Computer has chosen the no. between 1 to 100
# guess the no. in minimu attempts   
# start guessing!!!                                                                                                                                                                                                                                                                                                                  
""")

guessed = False
attempt = 0

while guessed == False:
    guess = int(input("Guess :"))
    if guess > num:
        print("Attempt : ",attempt)
        print("Your guess is higher than the Number | Try Again")
        print("----------------------------------------------------------------------------------------")
        attempt+=1
        continue
    
    elif guess < num:
        print("Attempt : ",attempt)
        print("Your guess is lower than the Number | Try Again")
        print("----------------------------------------------------------------------------------------")
        attempt+=1
        continue

    else:
        guessed = True
        print("Number Guessed Correctly! | Attempts :",attempt)