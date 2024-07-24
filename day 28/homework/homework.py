def digitize(n):
    return [int(digit) for digit in str(n)][::-1]

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

def determine_winner(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"