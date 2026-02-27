def main():
    difficulty = input("Difficulty: (Difficult, Casual) ")
    if not(difficulty == 'Difficult' or difficulty == 'Casual'):
        print("Invalid input for difficulty.")
        return
    
    players = input("Players: (Multiplayer, Singleplayer) ")
    if not(players == 'Multiplayer' or players == 'Singleplayer'):
        print("Invalid input for players.")
        return

    if difficulty == 'Difficult' and players == 'Multiplayer':
        recommend("Dark Souls")

    elif difficulty == 'Difficult' and players == 'Singleplayer':
        recommend("Sekiro")

    elif difficulty == 'Casual' and players == 'Multiplayer':
        recommend("Mario Kart")
    
    else:
        recommend("Animal Crossing")

def recommend(game):
    print("We recommend: " + game)

main()