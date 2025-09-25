#square a number
def square(x):
    ans = x*x
    print(x, ' squared is ', ans)


#check a number is odd or even
def is_odd(x):
    if x%2 != 0:
        print(x, 'is an odd number')
    else:
        print(x, 'is an even number')


#calculates average of a list of numbers
def average(x):
    ans2 = sum(x)/len(x)
    print('The average of the numbers is ', ans2)

