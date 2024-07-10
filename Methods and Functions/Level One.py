#   LEVEL 1 PROBLEMS
# Old Macdonald: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    result = []

    for i, letter in enumerate(name):
        if i == 0 or i == 3:
            result.append(letter.upper())
        else:
            result.append(letter)
    return ''.join(result)


print(old_macdonald('daniel'))
print(old_macdonald('japheth'))

print('')


#Master Yoda: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    result = []
    sentence = text.split()

    for word in sentence:
        result.append(word)

    reversed_sentence = result[::-1]
    return ' '.join(reversed_sentence)


print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print('')


#Almost there: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))