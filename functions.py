#-----------------------------------------------------------------------------
# Name:        Functions (functions.py)
# Purpose:     Demonstrating how to define functions with parameters, default
#              values, descriptions and return values, how to call them, and
#              passing lists into functions
#
# Author:      Mr. Kowalczewski
# Created:     28-Sept-2026
# Updated:     16-Nov-2026
#-----------------------------------------------------------------------------

def menu():
    '''Displays a basic menu of options

    '''
    print('Menu')
    print('Vegetables')
    print('Fruit')
    return


def hypotenuse(side_a, side_b):
    '''Calculates the hypotenuse and returns it, based on
       side_a and side_b given

    '''
    # None is returned if an invalid side_a or side_b is given
    if side_a <= 0 or side_b <= 0:
        return None

    # c_square is a local variable used to hold information
    c_square = side_a**2 + side_b**2
    hypotenuse_value = c_square**0.5
    return hypotenuse_value

def late_calculator(grade, lates=0):
    '''Calculates a student's grade, subtracting marks based on their
       number of lates. Default value of 0 is given for lates.
    '''
    # None is returned if we have an invalid grade
    if grade < 0 or grade > 100:
        return None

    # deducts 5% per late
    lates_deduction = lates * 5
    return grade - lates_deduction
   


def greeting(name, greet='Hello'):
    '''Returns a personalized greeting.'''
    # local variable message
    message = greet + " " + name
    return message


def add_number(num):
    num += 1
    print(f"num within function: {num}")
    return


def add_list(my_list):
    # make a copy of the list, so that the original list doesn't get modified
    new_list = my_list.copy()
    new_list.append(1)
    print(f"list within function: {new_list}")
    return

# --- Lists and dictionaries in functions -------------------------------------
# what we're used to: the original variable does not change outside the function
num = 10
add_number(num)
print(f"num outside function: {num}")

# print()
# # a list (or dictionary) parameter could change the original, so the function works on a copy
# number_list = [10, 9, 8]
# add_list(number_list)
# print(f"list outside function: {number_list}")
# The program runs starting here. Above this line, the functions are just defined.

menu()
menu()
print(hypotenuse(8,6))

# variables created inside functions exist only inside the functions
#print(c_square)
triangle_side = hypotenuse(10, 8)
print(triangle_side)
test_grade = late_calculator(80)
print(test_grade)
if test_grade < 50:
    print("This student is now failing.")
print(greeting('Priya'))
print(greeting('Priya', 'Welcome back'))

# # the same function, called several times with different parameters
print(f"Hypotenuse: {hypotenuse(side_b=3, side_a=4)}")
print(f"Hypotenuse: {hypotenuse(13, 12)}")
print(f"Hypotenuse: {hypotenuse(-2, 4)}")



