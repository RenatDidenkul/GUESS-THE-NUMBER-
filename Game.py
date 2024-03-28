import random

n_comp = random.randint(1, 100)

while True:
    n = int(input("ENTER NUMBER FROM 1 TO 100: "))
    if n==n_comp:
        print("YOU GUESSED IT!")
        break
    elif n>n_comp:
        print("YOU ENTERED MORE THAN THE COMPUTER REMEMBERED! TRY AGAIN!")
    elif n<n_comp:
        print("YOU ENTERED LESS THAN THE COMPUTER REMEMBERED! TRY AGAIN!")