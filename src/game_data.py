# Code for the rock paper scissors game


# code for the stats choice
import random


def calculate_stats(wins, losses, ties):
    total_games = wins + losses + ties

    if total_games > 0:
        win_percentage = (wins / total_games) * 100
    else:
        win_percentage = 0

    return total_games, win_percentage


def view_stats(wins, losses, ties):
    total_games, win_percentage = calculate_stats(wins, losses, ties)


def start_game(ties, wins, losses):
    player_choice = input("Choose Rock, Paper  Scissors").strip().lower()
    VALID_CHOICES = ["rock", "paper", "scissors"]
    while player_choice not in VALID_CHOICES:
        print("Invalid Option.")
        player_choice = input("Choose Rock, Paper  Scissors").strip().lower()
    computer_choice = random.choice(VALID_CHOICES)

    if player_choice == computer_choice:
        print("It's a tie")
        ties += 1
    elif player_choice == "rock" and computer_choice == "scissors":
        print(" Player won!!!")
        wins += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print(" Player won!!!")
        wins += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print(" Player won!!!")
        wins += 1
    else:
        print("You Lose!!")
        losses += 1
