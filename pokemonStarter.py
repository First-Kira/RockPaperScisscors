import random

def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "Water" and player2 == "Fire") or \
         (player1 == "Fire" and player2 == "Grass") or \
         (player1 == "Grass" and player2 == "Water"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def main():
    choices = ["Water", "Fire", "Grass"]
    print("Welcome to Water, Fire, Grass!")
    print("Choices: Water, Fire, Grass")
    
    player1_choice = input("Player 1, enter your choice: ")
    
    if player1_choice not in choices:
        print("Invalid choice. Please choose Water, Fire, or Grass.")
        return
    
    # Computer randomly selects its choice
    player2_choice = random.choice(choices)
    
    print("Player 2 chooses:", player2_choice)
    
    result = determine_winner(player1_choice, player2_choice)
    print(result)

if __name__ == "__main__":
    main()

