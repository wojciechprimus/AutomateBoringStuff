import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = int(input())
    toss=random.randint(0,1) # 0 is tails and 1 is heads
    if toss == guess:
        print("You got it!")
        break
    else:
        print("Nope")
        guess = int(input())
        if toss == guess:
            print("You got it")
            break
        else:
            print("Nope")
            break
