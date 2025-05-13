
def is_balanced(string):
    letters = {}
    for letter in string:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
        if len(letters) > 2:
            return False
   
    if len(letters) != 2:
        return False

    values = list(letters.values())
    return values[0] == values[1]


def find_longest_balanced_substring(string):
    longest = 0
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if is_balanced(string[i:j]):
                longest = max(longest, j - i)
    return longest



string = input("Input your string: ")
print(find_longest_balanced_substring(string))  

















