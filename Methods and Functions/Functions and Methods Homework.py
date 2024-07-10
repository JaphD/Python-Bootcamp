import math


# Write a function that computes the volume of a sphere given its radius.
def vol(radius):
    return (math.pi) * (4 / 3) * radius ** 3


print(vol(2))

print('')


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    if num in range(low, high + 1):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is not in the range between {low} and {high}')


ran_check(27, 16, 25)


# or

def ran_bool(num, low, high):
    if num in range(low, high + 1):
        return True
    else:
        return False


print(ran_bool(27, 16, 25))

print('')


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    uppercase_count = 0
    lowercase_count = 0

    for character in s:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1
    print(f'Original String: {s}')
    print(f'No. of Upper case characters : {uppercase_count}')
    print(f'No. of Lower case characters : {lowercase_count}')


s = 'Hi there, my name is Yafet Daniel'
up_low(s)

print('')


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    unique_elements = set(lst)
    my_list = list(unique_elements)

    return my_list


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

print('')


# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    product = 1

    for num in numbers:
        product *= num
    return product


print(multiply([1, 2, 3, -4]))

print('')


# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    stripped_s = s.replace(' ', '')

    if stripped_s == stripped_s[::-1]:
        return True
    else:
        return False


print(palindrome('racecar'))

print('')

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any
# punctuation)
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphabet_list = []

    for letter in string.ascii_lowercase:
        alphabet_list.append(letter)


    stripped_str1 = str1.replace(' ', '')
    stripped_str1 = set(stripped_str1.lower())
    input_string = list(stripped_str1)

    for character in alphabet_list:
        if character not in stripped_str1:
            return False
        else:
            pass
    return True


print(ispangram('The quick brown fox jumps over the lazy dog'))
