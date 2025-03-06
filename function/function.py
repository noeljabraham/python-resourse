#Function Returning a Value - Part 1
def generate_full_name():
    first_name ="Noel"
    last_name ="Abraham"
    full_name = first_name + last_name
    return full_name
print(generate_full_name())

#Function with Parameters
def add_num(num):
    number=90
    return num + number

print(add_num(10))

def sum_of_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
print((sum_of_numbers(20)))

def sum_of_two(num1, num2):
    sum = num1 + num2
    return sum
print('Sum of two numbers:' ,sum_of_two(1,2))

#Passing Arguments with Key and Value
def sum_of_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(sum_of_numbers(num2=2, num1=1))

#Function with Default Parameters
def suming(first_name='noel', last_name='abraham'):
    full_name= first_name + last_name
    return full_name
print(suming())
print((suming('raju', 'badar')))

#Arbitrary Number of Arguments

def sumofnumbers(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print(sumofnumbers(2,3,5))

#Function as a Parameter of Another Function
def square(x):
    return x * x
def something(f,x):
    return  f(x)

print(something(square,19))
