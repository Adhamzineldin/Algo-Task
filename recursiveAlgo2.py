def find_longest_balanced_substring(s, i=0, j=0):
    if i >= len(s):
        return 0
    if j >= len(s):
        return find_longest_balanced_substring(s, i + 1, i + 1)

    count1 = count2 = 0
    char1 = s[i]
    char2 = None

    for k in range(i, j + 1):
        if s[k] == char1:
            count1 += 1
        elif char2 is None:
            char2 = s[k]
            count2 += 1
        elif s[k] == char2:
            count2 += 1
        else:
            return max(find_longest_balanced_substring(s, i, j + 1),
                       find_longest_balanced_substring(s, i + 1, i + 1))

    if count1 == count2 and count1 > 0:
        return max(j - i + 1, find_longest_balanced_substring(s, i, j + 1))
    else:
        return find_longest_balanced_substring(s, i, j + 1)

# Test
print(find_longest_balanced_substring("aabbaaabbb"))  # Output: 6
