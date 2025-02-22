import random
import time
import os

# ASCII Art for visual appeal
art = {
    "rock": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.___(___)
    ''',
    "paper": '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''',
    "scissors": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
}

# Function to determine the winner 
def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function for a loading effect
def loading_effect():
    print("\nRock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissors...")
    time.sleep(0.5)
    print("Shoot!\n")
    time.sleep(0.3)

# Main game function
def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    rounds = 5  # Best of 5 rounds

    print("\n🎮 Welcome to Rock-Paper-Scissors! Best of 5 Rounds! 🎯")

    for round_num in range(1, rounds + 1):
        print(f"\n🔹 Round {round_num} 🔹")

        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
        if user_choice not in choices:
            print("❌ Invalid choice! Try again.")
            continue

        computer_choice = random.choice(choices)

        loading_effect() 

        print(f"\nYou chose: {user_choice}")
        print(art[user_choice]) 

        print(f"\nComputer chose: {computer_choice}")
        print(art[computer_choice])  

        result = get_winner(user_choice, computer_choice)
        print(f"\n🎉 {result} 🎉")

        if "You win!" in result:
            user_score += 1
        elif "Computer wins!" in result:
            computer_score += 1

        print(f"📊 Score: You {user_score} - {computer_score} Computer")

        # Stop early if someone reaches 3 wins first
        if user_score == 3 or computer_score == 3:
            break  

    print("\n🎖 FINAL RESULT 🎖")
    if user_score > computer_score:
        print("🏆 Congratulations! You won the game! 🏆")
    else:
        print("💀 Computer wins! Better luck next time! 💀")

    print("Thanks for playing! 👋")

# Run the game
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    play_game()