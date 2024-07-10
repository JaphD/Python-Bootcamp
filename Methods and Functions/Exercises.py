'''Lesser of two evens: Write a function that returns the lesser of two given numbers
if both numbers are even, but returns the greater if one or both numbers are odd.'''
def lesser_of_two_evens(a, b):
    if (a % 2 == 0) and (b % 2 == 0):
        if a < b:
            return a
        else:
            return b
    elif (a % 2 != 0) or (b % 2 != 0):
        if a < b:
            return b
        else:
            return a


print(lesser_of_two_evens(7, 5))
print(lesser_of_two_evens(20, 30))
print(lesser_of_two_evens(6, 5))

print('')


'''Animal Crackers: Write a function that takes a two-word string and returns True
    if both words begin with same letter'''
def animal_crackers(text):
    words = text.title()
    letters = []

    for character in words:
        if character.isupper():
            letters.append(character)
        else:
            pass

    for letter in letters:
        if letter == letters[1]:
            return True
        else:
            return False


print('levelheaded Llama')
print('Crazy Kangaroo')

print('')


'''Makes Twenty: Given two integers, return True if the sum of the integers is 20
    or if one of the integers is 20. If not, return False'''
def makes_twenty(n1, n2):
    if (n1 + n2 == 20) or (n1 == 20) or (n2 == 20):
        return True
    else:
        return False


print(makes_twenty(10, 10))
print(makes_twenty(20, 10))
print(makes_twenty(2, 3))