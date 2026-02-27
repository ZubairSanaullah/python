def main():
    difficulty = input("Difficulty: (Difficult, Casual) ")
    players = input("Players: (Multiplayer, Singleplayer) ")

    if difficulty == 'Difficult':
        if players == 'Multiplayer':
            recommend('Dark Souls')
        elif players == 'Singleplayer':
            recommend('Sekiro')
        else:
            print("Invalid input for players.")

    elif difficulty == 'Casual':
        if players == 'Multiplayer':
            recommend('Mario Kart')
        elif players == 'Singleplayer':
            recommend('Stardew Valley')
        else:
            print("Invalid input for players.")
    else:
        print("Invalid input for difficulty.")

def recommend(game):
    print("We recommend: " + game)

main()