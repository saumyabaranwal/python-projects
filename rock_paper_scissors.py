from random import randint

print('''Hello!
Wanna relive your childhood?
Let's see if you can beat the computer!
        Welcome to Rock/Paper/Scissors!''')
print('''The rules are simple:
        1. Rock beats Scissors
        2. Scissors beats Paper
        3. Paper beats Rock
        BEWARE: Do not make spelling errors!
        LET US BEGIN!''')
t = ["Rock", "Paper", "Scissors"]
comp = t[randint(0, 2)]
n = int(input("How many chances do you want to play? "))
for i in range(n):
  player = 0
  player = input("Rock, Paper, Scissors?")
  if player == comp:
    print("Tie!")
  elif player == "Rock":
    if comp == "Paper":
      print("You lose!", comp, "covers", player)
    else:
      print("You win!", player, "smashes", comp)
  elif player == "Paper":
    if comp == "Scissors":
      print("You lose!", comp, "cut", player)
    else:
      print("You win!", player, "covers", comp)
  elif player == "Scissors":
    if comp == "Rock":
      print("You lose...", comp, "smashes", player)
    else:
      print("You win!", player, "cut", comp)
  else:
    print("That's not a valid play. Check your spelling!")
  player = 0
  comp = t[randint(0, 2)]
print('Thanks for playing! See you next time!')
