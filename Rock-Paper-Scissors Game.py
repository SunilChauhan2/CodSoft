import random   #for computer's choice

def play_game():    #fuction user and computer input
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
        return 0
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        return 1
    else:
        print("You lose!")
        return -1

def main():   
    print("Welcome to Rock-Paper-Scissors!")
    
    #score tracking
    user_score = 0   
    computer_score = 0
    while True:
        result = play_game()
        if result == 1:
            user_score += 1
        elif result == -1:
            computer_score += 1
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        # User to play again or not
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()