print("Welcome to the COMPUTER QUIZ GAME!")
name = input("Enter your name: ")
print(''' The rules are simple:
1) There will be 10 questions in the quiz.
2) For each correct answer, 7 points will be added.
3) For every wrong answer, 0 points will be added.
4) Incorrect spelling will be treated as a wrong answer.''')
playing = input("Do you want to play? (YES/NO) ")
if (playing.upper()!="YES"):
    quit()
else:
    print("Let's play :D")
points = 0
q1 = input("Who is known as the father of the computer? ")
if (q1.upper()=="CHARLES BABBAGE"):
    print("Great job! 10 points to",name)
    points = points + 10
else:
    print("Oh no! The correct answer  is Charles Babbage.")
q2 = input("What is the full form of CPU? ")
if (q2.upper()== "CENTRAL PROCESSING UNIT"):
    print("Great job! 10 points to",name)
    points = points + 10
else:
    print("Oh no! The correct answer  is Central Processing Unit.")
q3 = input("Who is the founder of Microsoft? ")
if (q3.upper()== "BILL GATES"):
    print("Great job! 10 points to",name)
    points = points + 10
else:
    print("Oh no! The correct answer  is Bill Gates.")  
q4 = input("How many bits are there in a byte? ")
if (q4 == "8" or (q4.upper() == "EIGHT")):
    print("Great job! 10 points to",name)
    points = points + 10
else:
    print("Oh no! The correct answer  is Eight.")
q5 = input("What does ALU stand for? ")
if (q5.upper() == "ARITHMETIC LOGIC UNIT"):
    print("Great job! 10 points to",name)
    points = points + 10
else:
    print("Oh no! The correct answer  is Arithmetic Logic Unit.")
q6 = input("What was India's first supercomputer named as? ")
if (q6.upper() == "PARAM" or (q6.upper() == "PARAM 8000")):
    print("Great job! 10 points to",name)
    points = points + 10
else:
    print("Oh no! The correct answer  is PARAM 8000.")
q7 = input("Which computer program converts assembly language to machine language?")
if (q7.upper()== "ASSEMBLER"):
    print("Great job! 10 points to", name)
    points = points + 10
else:
    print("Oh no! The correct answer  is Assembler.")
print ("Total points =",points, "/70")
if points == 70:
    print("You are a champion!")
if points<=20:
    print('''Looks like you never paid attention to the computer classes!
Thank you for playing!''')