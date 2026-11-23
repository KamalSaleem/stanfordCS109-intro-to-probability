import random

def win(x, y):
  if y > x:
    return True
  elif y == x:
    return None
  return False

def game():
  x = 0
  y = 0
  sum = 0
  while sum <= 100:
    x = random.randint(1, 100)
    sum += x
  while sum <= 200:
    y = random.randint(1, 100)
    sum += y

  return x, y

x_wins = 0
y_wins = 0
for i in range(1000000):
  x, y = game()
  if win(x, y) == True:
    y_wins += 1
  elif win(x, y) == False:
    x_wins += 1

draws = i+1 - x_wins - y_wins
prob_x = x_wins / (i+1)
prob_y = y_wins / (i+1)
prob_d = draws / (i+1)

print(f"the probability of x winning is {prob_x:.3f}")
print(f"the probability of y winning is {prob_y:.3f}")
print(f"the probability of a draw {prob_d:.3f}")
print(f"total games: {i+1}")
print(f"x won: {x_wins}")
print(f"y won: {y_wins}")
print(f"draws : {draws}")