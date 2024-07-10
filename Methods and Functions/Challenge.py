'''Spy Game: Write a function that takes in a list of integers and returns True
    if it contains 007 in order'''
def spy_game(nums):
    code = [0, 0, 7]
    code_idx = 0

    for num in nums:
        if num == code[code_idx]:
            code_idx += 1
        if code_idx == len(code):
            return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

print('')

'''Count Primes: Write a function that returns the number of prime numbers that exist
    up to and including a given number'''
def count_primes(num):
    prime_count = 0

    if num < 2:
        return prime_count

    for i in range(2, num + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1

    return prime_count

print(count_primes(100))

print('')

'''Print Big: Write a function that takes in a single letter, and returns a 5*5 representation of
    the letter'''
def print_big(letter):
    patterns = {
        'A': ["  *  ", " * * ", "*****", "*   *", "*   *"],
        'B': ["**** ", "*   *", "**** ", "*   *", "**** "],
        'C': [" ****", "*    ", "*    ", "*    ", " ****"],
        'D': ["**** ", "*   *", "*   *", "*   *", "**** "],
        'E': ["*****", "*    ", "*****", "*    ", "*****"],
        'F': ["*****", "*    ", "*****", "*    ", "*    "],
        'G': [" ****", "*    ", "*  **", "*   *", " ****"],
        'H': ["*   *", "*   *", "*****", "*   *", "*   *"],
        'I': ["*****", "  *  ", "  *  ", "  *  ", "*****"],
        'J': ["  ***", "   * ", "   * ", "*  * ", " **  "],
        'K': ["*   *", "*  * ", "***  ", "*  * ", "*   *"],
        'L': ["*    ", "*    ", "*    ", "*    ", "*****"],
        'M': ["*   *", "** **", "* * *", "*   *", "*   *"],
        'N': ["*   *", "**  *", "* * *", "*  **", "*   *"],
        'O': [" *** ", "*   *", "*   *", "*   *", " *** "],
        'P': ["**** ", "*   *", "**** ", "*    ", "*    "],
        'Q': [" *** ", "*   *", "*   *", "*  **", " ****"],
        'R': ["**** ", "*   *", "**** ", "*  * ", "*   *"],
        'S': [" ****", "*    ", " *** ", "    *", "**** "],
        'T': ["*****", "  *  ", "  *  ", "  *  ", "  *  "],
        'U': ["*   *", "*   *", "*   *", "*   *", " *** "],
        'V': ["*   *", "*   *", "*   *", " * * ", "  *  "],
        'W': ["*   *", "*   *", "* * *", "** **", "*   *"],
        'X': ["*   *", " * * ", "  *  ", " * * ", "*   *"],
        'Y': ["*   *", " * * ", "  *  ", "  *  ", "  *  "],
        'Z': ["*****", "   * ", "  *  ", " *   ", "*****"]
    }

    letter = letter.upper()
    if letter in patterns:
        return "\n".join(patterns[letter])
    else:
        return "Letter not supported."

print(print_big('a'))
print(print_big('z'))