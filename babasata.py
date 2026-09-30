#test_01

# while True:
#     #Check if the input is int
#     try:
#         #Ask the user for a number
#         user_num = int(input("Entr a number: "))
#     except ValueError:
#         continue
#     #Check if number is even or odd
#     if user_num % 2 == 0:
#         print("Your number is Even")
#     else:
#         print("Your number is Odd")

#test_02

# #Ask a user for 3 numbers
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# #Check the numbers
# if num1 == num2 == num3:
#     print("the numbers is Equal")
# else:
#     if num1 > num2 and num1 > num3 :
#         print(f"{num1} is the largest number")
#     elif num2 > num1 and num2 > num3:
#         print(f"{num2} is the largest number")
#     else:
#         print(f"{num3} is the largest number")

#test_03

# #Ask the user for a number
# user_num = int(input("Enter a Number: "))
# #list
# numbers = 0
# #appent the number to the list
# for i in range(1,user_num+1):
#     numbers += i
# #print the list of numbers
# print(f"Sum from 1 to {user_num} is: {numbers}")

#test_04

# while True:
#     #Ask the user to enter a number
#     user_num = int(input("Enter a number: "))
#     #print the number's multiplication table from 1 to 12
#     for i in range(1,13):
#         print(f"{i} X {user_num} = {user_num*i}")


#test_05

# #Ask user to enter a word or sentance
# user_input = input("Enter a word ar sentance: ")
# #revesed the text
# print(user_input[::-1])

# test_06

# #Ask user to enter nums
# user_input = [int(i)for i in input("Type several numbers separated by spaces:").split()]

# #Check if user enter nums or no.
# if user_input:
#     print(sum(user_input) / len(user_input))
# else:
#     print("NO Numbers Entered")

#test_07

# user_nums = [int(i) for i in input("Enter the number by saparated by spaces: ").split()]

# count = [0,0,0]
# for i in user_nums:
#     if i % 2 == 0 and i != 0:
#         count[0] += 1
#     elif i == 0:
#         count[2] += 1
#     else:
#         count[1] += 1

# print(f"+: {count[0]}")
# print(f"-: {count[1]}")
# print(f"0: {count[2]}")

#test_08

# user_inputs = [int(i) for i in input("Enter a list of values saparated by spaces: ").split()]

# numbers = []
# for i in user_inputs:
#     if i in numbers:
#         continue
#     else:
#         numbers.append(i)

# print(numbers)

#test_09












