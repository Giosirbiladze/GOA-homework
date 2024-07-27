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
    
def quarter_of(month):
    if month >= 1 and month <= 3:
        return 1
    elif month >= 4 and month <= 6:
        return 2
    elif month >= 7 and month <= 9:
        return 3
    elif month >= 10 and month <= 12:
        return 4
    else:
        return None


def count_sheep(n):
    result = []
    for i in range(1, n + 1):
        result.append(str(i) + " sheep...")
        return "".join(result)

def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

def rental_car_cost(d):
    daily_rate = 40
    total_cost = d * daily_rate
    
    if d >= 7:
        total_cost -= 50
    elif d >= 3:
        total_cost -= 20    
    return total_cost

def remove_exclamation_marks(s):
     return s.replace('!', '')