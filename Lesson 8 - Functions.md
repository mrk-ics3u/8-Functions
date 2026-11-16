# Lesson 8 - Functions

The example code for this lesson is in `functions.py`. Open it alongside these
notes and run it as we go.

A function packages up reusable code that performs a single action. You have
been using one all along: `print()`.

Functions are structured differently from anything we have written so far. The
basic setup is:

```python
def function_name(parameter1, parameter2, ...):
    '''Description of what the function does

    '''
    # body of the function (whatever the function needs to do)
    return expression
```

- `def` is required to define a function.
- `function_name` should make the purpose of the function clear.
- `parameter1, parameter2, ...` are the values the function receives and uses
  inside. There can be none (`def function_name():`), and some can have default
  values (see `late_calculator` below).
- `'''Description'''` describes the purpose of the function. We will go further
  with this later; for now, just write a description.
- The body does the work (if statements, calculations and so on).
- `return` sends a value back to wherever the function was called.

A function must be defined before it can be used, so functions go at the top of
the file.

```python
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
    grade = grade - lates_deduction
    return grade


def greeting(name, greet='Hello'):
    '''Returns a personalized greeting.'''
    # local variable message
    message = greet + " " + name
    return message


# The program runs starting here. Above this line, the functions are just defined.
menu()
print(hypotenuse(3, 4))

# variables created inside functions exist only inside the functions
#print(c_square)
triangle_side = hypotenuse(10, 8)
print(triangle_side)
test_grade = late_calculator(80)
print(test_grade)
print(greeting('Priya'))
print(greeting('Priya', 'Welcome back'))
```

Because the code is in functions, we can reuse it as often as we like. For
example, `late_calculator()` works for every student without rewriting the
calculation.

## Why use functions?

Imagine a program that calculates a hypotenuse several times, in different
places (so a loop will not help). Which is easier to follow?

```python
side_a = 5
side_b = 8
if side_a <= 0 or side_b <= 0:
    print('No result can be found')
else:
    c_square = side_a**2 + side_b**2
    hypotenuse_value = c_square**0.5
    print(f"Hypotenuse: {hypotenuse_value}")

# ... more code

side_a = 12
side_b = 4
if side_a <= 0 or side_b <= 0:
    print('No result can be found')
else:
    c_square = side_a**2 + side_b**2
    hypotenuse_value = c_square**0.5
    print(f"Hypotenuse: {hypotenuse_value}")

# ... more code

side_a = -2
side_b = 4
if side_a <= 0 or side_b <= 0:
    print('No result can be found')
else:
    c_square = side_a**2 + side_b**2
    hypotenuse_value = c_square**0.5
    print(f"Hypotenuse: {hypotenuse_value}")
```

Or this?

```python
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


print(f"Hypotenuse: {hypotenuse(side_b=3, side_a=4)}")
# ... more code
print(f"Hypotenuse: {hypotenuse(13, 12)}")
# ... more code
print(f"Hypotenuse: {hypotenuse(-2, 4)}")
```

Another benefit: if the calculation needs to change, it only changes in one
place, which reduces errors.

## Important notes about functions

- Function code does not run until the function is called with its required
  parameters. Keep functions at the top of the program so they are available
  everywhere.
- Parameters are given in the stated order. You can also write
  `parameter = value` to give them in a different order.
- Variables created inside a function exist only inside it. `c_square` and
  `lates_deduction` above are examples. These are called local variables.
- For now, we return `None` when a function cannot work with the parameters it
  was given. `None` means the absence of a value. Later in the course we will
  learn a better way.
- You can `print()` inside a function, but returning the result is preferred.
  That lets you use the result in different ways, as we will see next lesson.
- A function should receive information through its parameters, do some quick
  work and return the result. Do not use `input()` inside a function except in
  very special circumstances.
- As soon as `return` is reached, the function ends. Several returns are fine,
  but only one applies each time the function runs.

## Lists and dictionaries in functions

This will not be on the upcoming test or exam, but it may come up in your
programming assignment.

Strings, integers and floats are immutable: they cannot be changed. When we
write `x = x + 10`, we are not changing the original value of `x`; we are giving
`x` a new value. So passing a variable like `x` into a function leaves the
original untouched.

Lists and dictionaries are mutable: the actual data can change. If you pass a
list or dictionary into a function, the function can change the original. We
want to avoid that.

```python
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


# what we're used to: the original variable does not change outside the function
num = 10
add_number(num)
print(f"num outside function: {num}")

# a list (or dictionary) parameter could change the original, so the function works on a copy
number_list = [10, 9, 8]
add_list(number_list)
print(f"list outside function: {number_list}")
```

Use `.copy()` inside the function to make a copy of the original list or
dictionary, and work with the copy.

## Lab

That is it for the lesson. Move on to Lab 8, in `README.md`.
