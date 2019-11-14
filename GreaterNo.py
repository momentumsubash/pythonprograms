a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
# a, b, c = input('enter no').split(',')

if (a > b) and (a > c):
    temp = a
elif (b > a) and (b > c):
    temp = b
else:
    temp = c

print("The gretest number is", temp)