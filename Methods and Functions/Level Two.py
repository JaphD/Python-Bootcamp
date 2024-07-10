#   LEVEL 2 PROBLEMS
# Find 33 : Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.'''
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

print('')


'''Paper Doll: Given a string, return a string where for every character in the original there 
    are three chracters'''
def paper_doll(text):
    result = []

    for character in text:
        result.append(character * 3)
    return ''.join(result)


print(paper_doll('hello'))
print(paper_doll('Mississippi'))

print('')


'''Blackjack: Given three integers between 1 and 11, if their sum is less than or equal to 21, return
    their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if 
    the sum(even after adjustment) exceeds 21, return 'BUST'. '''
def blackjack(a, b, c):
    total = a + b + c

    if total <= 21:
        return total
    elif 11 in (a, b, c):
        total -= 10

        if total > 21:
            return 'BUST'
        else:
            return total
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

print('')


'''Summer of '69: Return the sum of the numbers in the array, except ignore sections of numbers starting
    a 6 and extending to the next 9 (every 6 will be followed by atleast one 9). Return 0 for no numbers.'''
def summer_69(arr):
    sum = 0

    for num in arr:
        if num in range(6, 10):
            continue
        else:
            sum += num
    return sum

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))
