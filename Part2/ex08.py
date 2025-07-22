import random

def print_intro():
    print("🎰 Welcome to the High-Low Gambling Game!")
    print("You start with $100. Try to grow your money by guessing high or low.")
    print("If the random number is above 50, 'high' wins. Below 50, 'low' wins.")
    print("If it's 50 exactly, house wins! Let's play.\n")

def get_bet(balance):
    while True:
        try:
            bet = int(input(f"💰 Your balance is ${balance}. Enter your bet: $"))
            if 1 <= bet <= balance:
                return bet
            else:
                print("❌ Invalid bet amount.")
        except ValueError:
            print("❌ Please enter a valid number.")

def get_guess():
    while True:
        guess = input("🃏 Do you bet on 'high' or 'low'? ").lower()
        if guess in ['high', 'low']:
            return guess
        else:
            print("❌ Invalid choice. Type 'high' or 'low'.")

def play_round(balance):
    bet = get_bet(balance)
    guess = get_guess()
    number = random.randint(1, 100)
    print(f"🎲 The number is: {number}")

    if number == 50:
        print("🏚️ It's exactly 50! House wins!")
        return balance - bet
    elif (number > 50 and guess == 'high') or (number < 50 and guess == 'low'):
        print("✅ You win!")
        return balance + bet
    else:
        print("❌ You lose.")
        return balance - bet

def main():
    balance = 100
    print_intro()

    while balance > 0:
        balance = play_round(balance)
        if balance <= 0:
            print("💀 You're broke. Game over.")
            break
        again = input("🔁 Play another round? (y/n): ").lower()
        if again != 'y':
            break

    print(f"🏁 You ended the game with ${balance}. Thanks for playing!")

if __name__ == "_main_":
    main()

                
