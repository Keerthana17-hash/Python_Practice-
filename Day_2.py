#Write a program to print the given number is even number or odd number.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

#2.	Write a program to find out the maximum among given two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

maximum = max(num1, num2)
print(f"The maximum number is {maximum}")
#3.	Write a program to print given string is palindrome or not.
string = input("Enter a string: ")
if string == string[::-1]:
    print(f'"{string}" is a Palindrome.')
else:
    print(f'"{string}" is not a Palindrome.')

#4.	Write a program to find out the maximum of 3 given numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

maximum = max(num1, num2, num3)
print(f"The maximum number is {maximum}")

