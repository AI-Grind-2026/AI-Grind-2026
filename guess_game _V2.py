while True:
    import random
    number=random.randint(1, 10)
    welcome_message="Welcome to the guessing game!!!"
    print(welcome_message)
    attempts=0
    max_attempts=3
    Lost_message="Youve lost! Good luck next time!"
    while attempts < max_attempts:
        Guess=int(input("Guess a number between 1 and 10: "))
        attempts += 1
        print(f"attempt {attempts} of {max_attempts}")
        if Guess == number:
            print(f"Congratulations! You needed {attempts} attempts, to guess the number!!!")
            break
        elif Guess < number:
            print("whoops, too low!!!")
        elif Guess > number:
            print("Whoops! Too high!")
    if attempts == max_attempts:
            print(Lost_message)
    if attempts >= max_attempts and Guess +- 1 == number:
            print("So close! One of your guesses missed just by 1!!!")
    play_again=input("Do you want to play again? (yes/no):")
    if play_again.lower()== 'yes':
         continue
    if play_again.lower()== 'no':
         print("thanks for playing")
         break
    
       

            
        
            


    