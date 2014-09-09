high = 100
low = 0
guess = (high + low) / 2
instruct = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
sorry = "Sorry, I did not understand your input."
hlc = "a"

print ("Please think of a number between 0 and 100!")

while hlc != "c":
    print ("Is your secret number " + str(guess) + "?")
    hlc = raw_input(instruct)
    if hlc == "l":
        low = guess
        guess = (guess + high) / 2
    elif hlc == "h":
        high = guess
        guess = (guess + low) / 2
    else:
        if hlc == "c":
            break
        else:
            print sorry
    
print ("Game over. Your secret number was: " + str(guess))
