import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
    elif comp == 'g':
        return True
    elif comp == 'w':
        if you == 's':
            return True
    elif comp == 'g':
        return False
    elif comp == 'g':
        if you == 'g':
            return True
    elif comp == 's':
        return False


a = print("Computer' turn : Snake(s) Water (w) or gun(g)")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 's'

running = True

while running:

    you = input("Player 2 : Snake(s) Water (w) or gun(g) ")
    a = gameWin(comp, you)
    print(f"Computer choose {comp}")
    print(f"You choose {you}")
    if a == None:
        print("The game is tie")
    elif a:
        print("You win!!")
    else:
        print("You lose!!")

    if not input("Play again? (y/n): ").lower() == "y":
      running = False

print("Thanks for playing!")
