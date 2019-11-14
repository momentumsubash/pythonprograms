# #find out whether a number is prime or not
# n = int(input("enter n: "))
# ans = True
# for i in range(2,n):
#     if n % i == 0:
#         ans = False
#         break
# print(ans)


#find the prime numbers of a certain range
# for n in range(2,21):
#     ans = True
#     for i in range(2,n):
#         if n % i == 0:
#             ans = False
#             break
#     if ans == True:
#         print(n,"is prime")
#     else:
#         print(n,"is not prime")


# find the prime numbers of a certain range
# and put them in a list
primes = []  # empty list
n=int(input('enter the range'))
for n in range(2, n):
    ans = True
    for i in range(2, n):
        if n % i == 0:
            ans = False
            break
    if ans == True:
        primes.append(n)  # add to list if prime

print(primes)





#program to print list with itetration
# numbers = [1,2,3,5,6]
#iterating through a list

# for i in range(len(numbers)):
#     print(i,numbers[i])

# for num in numbers:
#     print(num)


#ask numbers from user and put in a list
# numbers = []
# ans = "y" #set default to "y" to run loop
# while ans == "y":
#     n = int(input("Enter a number: "))
#     numbers.append(n)
#     ans = input("Continue (y/n): ")
# print(numbers)

#program for factorial using while
# n = 5
# f = 1
# while n > 1:
#     f = f * n
#     n = n - 1
# print(f)

