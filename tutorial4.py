#a function to calculate the sum of 2 numbers
def add_two(a,b):
    """function to add 2 numbers"""
    sum_ = a + b
    return sum_

#ways to call/invoke a function

#print(add_two.__doc__)
#print(add_two(23,3))

#print("The sum of 100 and 100 is",add_two(100,100))
#ans = add_two(1,1)
#print(ans)

#num1 = int(input("Enter a num: "))
#num2 = int(input("Enter another num: "))
#print("Their sum is",add_two(num1,num2))


#function to find out whether a number is prime or not
def prime(n):
    ans = True 
    for i in range(2,n): 
        if n % i == 0:
            ans = False
            break
    return ans

#n = int(input("enter n: "))
#print(prime(n))
#print(prime(12))
'''
for number in range(2,21):
    if prime(number) == True:
        print(number,"is prime")
    else:
        print(number,"is not prime")

'''

primes = [] #empty list
for number in range(2,101):
    if prime(number) == True:
        primes.append(number) #add to list if prime
        
print(primes)

#ask numbers from user and put in a list
numbers = []
ans = "y" #set default to "y" to run loop
while ans == "y":
    n = int(input("Enter a number: "))
    numbers.append(n)
    ans = input("Continue (y/n): ")
print(numbers)

#iterating through a list
print("----") 
for i in range(len(numbers)):
    print(numbers[i])
print("----")
for number in numbers:
    print(number)
'''
