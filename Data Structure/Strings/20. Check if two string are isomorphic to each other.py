



# a one-to-one mapping possible for every character of str1 to
# every character of str2. And all occurrences of every character
# in ‘str1’ map to the same character in ‘str2’.
#
# Examples:
#
# Input:  str1 = "aab", str2 = "xxy"
# Output: True
# 'a' is mapped to 'x' and 'b' is mapped to 'y'.
#
# Input:  str1 = "aab", str2 = "xyz"
# Output: False
# One occurrence of 'a' in str1 has 'x' in str2 and
# other occurrence of 'a' has 'y'.

def isIsomorphic(s1, s2):
    m = len(s1)
    n = len(s2)

    if m != n:
        return 'Not isomorphic'
    map_s1_s2 = {}
    map_s2_s1 = {}

    for c1, c2 in zip(s1, s2):
        # case 1: no mapping exists in either of dictionaries
        if c1 not in map_s1_s2 and c2 not in map_s2_s1:
            map_s1_s2[c1] = c2
            map_s2_s1[c2] = c1
        # case 2: Either mapping doesn't exist in one of the
        # dictionaries or Mapping exists and it doesn't match
        # in either of the dictionaries or both
        elif map_s1_s2.get(c1) != c2 or map_s2_s1.get(c2) != c1:
            return False

    return True
