import random
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)
print('''Welcome to Passwordium!
What kind of password do you want to generate?
         1. Only numeric
         2. Only alphabetic
         3. Alphanumeric
         4. Random
         5. Exit''')
while True:
  choice = int(input("Enter your choice: "))
  if choice == 1:
    n1 = int(input("Enter how long you want the password to be: "))
    password1 = ""
    for _ in range(n1):
      Numeric = random.randint(0, 9)
      password1 = password1 + str(Numeric)
    password1 = shuffle(password1)
    print("Your numeric password is: ", password1)
    print("Thank you for using Password Generator!")
  elif choice == 2:
    n2 = int(input("Enter how long you want the password to be: "))
    password2 = ""
    for _i in range(n2):
      uppercaseLetter2 = chr(random.randint(65, 90))
      password2 = password2 + uppercaseLetter2
    password2 = shuffle(password2)
    new_password2 = ""
    for j in range(0, len(password2)):
      if j % 2 != 0:
        new_password2 += password2[j].lower()
      else:
        new_password2 += password2[j]
    print("Your alphabetic password is: ", new_password2)
    print("Thank you for using Password Generator!")
  elif choice == 3:
    n3 = int(input("Enter how long you want the password to be: "))
    password3 = ""
    for _k in range(n3):
      characters = chr(random.randint(48, 90))
      password3 = password3 + characters
    password3 = shuffle(password3)
    new_password3 = ""
    for j in range(0, len(password3)):
      if j % 2 != 0:
        new_password3 += password3[j].lower()
      else:
        new_password3 += password3[j]
    for m in range(0, len(new_password3)):
      if new_password3[m].isalnum() == True:
        pass
      else:
        new_password3_list = list(new_password3)
        new_password3_list[m] = chr(random.randint(65, 90))
        new_password3 = ''.join(new_password3_list)
    print("Your alphanumeric password is:", new_password3)
    print("Thank you for using Password Generator!")
  elif choice == 4:
    n4 = int(input("Enter how long you want the password to be: "))
    password4 = ""
    for _i in range(n4):
      uppercaseLetter4 = chr(random.randint(48, 112))
      password4 = password4 + uppercaseLetter4
    password4 = shuffle(password4)
    print("Your alphabetic password is: ", password4)
    print("Thank you for using Password Generator!")
  elif choice == 5:
    print('''Please rate our service: 
         1- Very Poor
         2- Poor
         3- Average
         4- Good
         5- Excellent''')
    rating = int(input("Enter your rating: "))
    if rating == 1 or rating == 2:
      print("We are sorry to hear that. We will try to improve our service.")
    elif rating == 3:
      print("We are always working to make our service better.")
    elif rating == 4 or rating == 5:
      print("Thank you for your feedback. We are glad to hear that.")
    else:
      print("Thank you for your feedback.")
      break
    break
  else:
    print('Invalid Choice!')








