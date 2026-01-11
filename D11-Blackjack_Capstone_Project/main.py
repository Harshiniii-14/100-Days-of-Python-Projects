import random
import art


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    """Calculates the score and adjusts Ace if needed"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    print(art.logo)

    player = []
    computer = []

    for _ in range(2):
        player.append(deal_card())
        computer.append(deal_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player)
        computer_score = calculate_score(computer)

        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {computer[0]}")

        if player_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == "y":
                player.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer.append(deal_card())
        computer_score = calculate_score(computer)

    print(f"\nYour final hand: {player}, final score: {player_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(player_score, computer_score))
