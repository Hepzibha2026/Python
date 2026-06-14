# Finding the longest common substring of two strings

def longest_common_substring(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    prev = [0] * (len(s2) + 1)
    max_len = 0
    end_pos = 0

    for i in range(1, len(s1) + 1):
        curr = [0] * (len(s2) + 1)
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
                if curr[j] > max_len:
                    max_len = curr[j]
                    end_pos = i
        prev = curr

    return s1[end_pos - max_len:end_pos]

print(longest_common_substring("abcdef", "zcdemf"))

