from game_data import view_stats
from game_data import start_game


def show_menu():
    is_running = True
    while is_running:
        print("\nGame Menu:")
        print("1. Play")
        print("2. View Stats")
        print("3. Quit")
        choice = input("Choose Your Option [1-3]: ")
        if choice == "1":
            print("Rock!... Paper!... Scissors!... Sayyyy!... Shooot!!!")
            start_game()
        elif choice == "2":
            view_stats()
        elif choice == "3":
            break
        else:
            print("invalid")
