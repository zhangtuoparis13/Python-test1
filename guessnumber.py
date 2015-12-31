import random
secret = random.randint(1,10)
print('-------------------I love you------------------')
temp = input("Please guess a number : ")
guess = int(temp)
while guess != secret :
    temp = input("Please repeat your guess: ")
    guess = int(temp)
    if guess == secret:
        print("well done, you got it!")
    else:
        if guess < secret:
            print("It\'s too small!!")
        else:
            print(r"It's too big!!")
print("finish!!")
