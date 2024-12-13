store = {}
while True:
  print(''' Welcome to Store Management System!
          1) Add product
          2) Remove product
          3) Search product
          4) Display all products
          5) Calculate total bill
          6) Exit''')
  choice = int(input("Enter your choice: "))
  if choice == 1:
    Name = input("Enter product name: ")
    SNo = int(input("Enter serial no: "))
    P = float(input("Enter price:"))
    store[SNo] = ["Name", Name, "Price", P]
  if choice == 2:
    SNo = int(input("Enter serial no of product to be removed: "))
    del store[SNo]
  if choice == 3:
    s = input("Enter product name: ")
    for i in store:
      if store[i][1] == s:
        print(store[i])
      else:
        print('Not found')
  if choice == 4:
    print(store)
  if choice == 5:
    for j in store:
      q = sum(store[j][3])
      print(q)