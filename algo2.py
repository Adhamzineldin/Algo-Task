
def find_longest_balanced_substring(s):
    n = len(s)
    longest = 0

    for i in range(n):
        count1 = count2 = 0
        char1 = s[i]
        char2 = None

        for j in range(i, n):
            if s[j] == char1:
                count1 += 1
            elif char2 is None:
                char2 = s[j]
                count2 += 1
            elif s[j] == char2:
                count2 += 1
            else:
                break  

            if count1 == count2 and count1 > 0:
                longest = max(longest, j - i + 1)

    return longest


string = "aabbaaabbb"
print(find_longest_balanced_substring(string))