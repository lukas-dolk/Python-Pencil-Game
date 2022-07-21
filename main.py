import random

losing = [1]
players = ["John", "Jack"]
allowed_amounts = ["1", "2", "3"]
starting_player = None
pencils = None
tracker = True


def pencil_logic():
    if pencils == 1:
        return 1
    if pencils - 1 in losing:
        return 1
    if pencils - 2 in losing:
        return  2
    if pencils - 3 in losing:
        return 3
    return random.choice([1, 2, 3])



while True:
    if tracker:
        try:
            pencils = int(input("How many pencils would you like to use: "))
            if pencils == 0:
                print("The number of pencils should be positive")
                continue
            elif pencils < 0:
                print("The number of pencils should be numeric")
                continue
        except ValueError:
            print("The number of pencils should be numeric")
            continue
    tracker = False
    starting_player = input(f"Who will be the first ({players[0]}, {players[1]}): ")
    if starting_player not in players:
        print(f"Choose between '{players[0]}' and '{players[1]}'")
        continue
    break


for i in range(pencils):
        losing.append(losing[i] + 4)


index = players.index(starting_player)

while pencils > 0:
    x = True
    print("|" * pencils)
    if players[index] == "Jack":
        print(f"{players[index]}'s turn:", end="")
    else:
        print(f"{players[index]}'s turn!", end="")
    if players[index] == "Jack":
        print(" ")
        x = False
        remove_pencils = pencil_logic()
        print(remove_pencils)
    while x:
        remove_pencils = input(" ")
        if remove_pencils not in allowed_amounts:
            print("Possible values: '1', '2' or '3'")
            continue
        elif int(remove_pencils) > pencils:
            print("Too many pencils were taken")
            continue
        break

    pencils -= int(remove_pencils)

    if index < len(players) - 1:
        index += 1
    elif index == len(players) - 1:
        index = 0

print(f"{players[index]} won!")
