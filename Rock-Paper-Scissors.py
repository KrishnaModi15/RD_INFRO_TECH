import random

def play_round():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid input. Try again.")
        return None, None

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "Tie", computer_choice
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "Win", computer_choice
    else:
        return "Lose", computer_choice

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        rounds += 1
        print(f"\nRound {rounds}:")
        result, computer_choice = play_round()

        if result == "Tie":
            print("It's a tie!")
        elif result == "Win":
            user_score += 1
            print("You win!")
        elif result == "Lose":
            computer_score += 1
            print("You lose!")

        print(f"Scores - You: {user_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\nFinal Scores - You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
