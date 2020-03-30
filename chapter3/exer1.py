#lottery game
winning_number = 12
guess_number=int(input("Guess the number :"))
if winning_number==guess_number :
    print('YOU WIN !!')
if guess_number<winning_number :
    print("to low")
if guess_number>winning_number :
    print("to high")
