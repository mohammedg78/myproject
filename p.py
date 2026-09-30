while True:
    #Ask the user to enter a number
    user_num = int(input("Enter a number: "))
    #print the number's multiplication table from 1 to 12
    for i in range(1,13):
        print(f"{i} X {user_num} = {user_num*i}")