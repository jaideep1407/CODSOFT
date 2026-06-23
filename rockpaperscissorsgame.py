import random

user_score = 0
computer_score = 0

print("=== Rock Paper Scissors Game ===")

while True:
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    # Computer's choice
    computer = random.choice(["rock", "paper", "scissors"])

    print("You chose:", choice)
    print("Computer chose:", computer)

    # Game Logic
    if choice == computer:
        print("It's a Tie!")

    elif (choice == "rock" and computer == "scissors") or \
         (choice == "paper" and computer == "rock") or \
         (choice == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nScore:")
    print("You:", user_score)
    print("Computer:", computer_score)

    # Play again
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break