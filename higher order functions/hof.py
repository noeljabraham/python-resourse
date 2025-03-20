# Function as a Parameter

# def sum_of_numbers(nums):
#     return sum(nums)
# def higher_order_functions(f, last):
#     summation = f(last)
#     return  summation
#
# result = higher_order_functions(sum_of_numbers,([1,2,3,4,5]))
# print(result)
# def square(x):          # a square function
#     return x ** 2
#
# def cube(x):            # a cube function
#     return x ** 3
#
# def absolute(x):        # an absolute value function
#     if x >= 0:
#         return x
#     else:
#         return -(x)
#
# def higher_order_function(type): # a higher order function returning a function
#     if type == 'square':
#         return square
#     elif type == 'cube':
#         return cube
#     elif type == 'absolute':
#         return absolute
#
# result = higher_order_function('square')
# print(result(3))       # 9
# result = higher_order_function('cube')
# print(result(3))       # 27
# result = higher_order_function('absolute')
# print(result(-3))      # 3