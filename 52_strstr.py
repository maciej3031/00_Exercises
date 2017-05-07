# Avoid using built-in functions to solve this challenge. Implement them yourself.
#
# Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x
# in s. The function should return an integer indicating the index in s of the first occurrence of x. If there are
#  no occurrences of x in s, return -1.
#
# Example:
#
# For s = "CodefightsIsAwesome" and x = "IA", the output should be
# strstr(s, x) = -1;
# For s = "CodefightsIsAwesome" and x = "IsA", the output should be
# strstr(s, x) = 10


def strstr(x, s):
    if x in s:
        for num, letter in enumerate(s):
            if letter == x[0] and x == s[num: num + len(x)]:
                return num
    return -1

print(strstr("IA", "CodefightsIsAwesome"))
print(strstr("ghi", "abcdefghabcdefghi"))