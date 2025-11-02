import random 
while True:
    try:
            
        attempt =7 
        rand= random.randint(1, 100)
        while attempt:
            attempt-=1
            guess= int(input(f"attempt {7-attempt}: your guessed number: "))
            if guess> rand:
                print("high, guess again")
            elif guess <rand:
                print("low, guess agian")
            else:
                print(f"congratulations! ypu guesed it in {7-attempt} attempts")
                break
        inpu= input("Play again? (yes/no)")
        if inpu=="yes":
            continue
        else:
            break
    except ValueError:
        print ("enter valid value")



