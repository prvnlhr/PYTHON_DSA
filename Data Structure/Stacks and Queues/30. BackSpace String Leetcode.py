# Example 1:
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:
#
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:
#
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#
# O(N),O(1)
def backspaceCompare(self, S, T):
    i = len(S) - 1  # Traverse from the end of the strings
    j = len(T) - 1

    skipS = 0  # The number of backspaces required till we arrive at a valid character
    skipT = 0

    while i >= 0 or j >= 0:

        while i >= 0:  # Ensure that we are comparing a valid character in S
            if S[i] == "#":
                skipS += 1  # If not a valid character, keep times we must backspace.
                i = i - 1

            elif skipS > 0:
                skipS -= 1  # Backspace the number of times calculated in the previous step
                i = i - 1

            else:
                break

        while j >= 0:  # Ensure that we are comparing a valid character in T
            if T[j] == "#":
                skipT += 1  # If not a valid character, keep times we must backspace.
                j = j - 1

            elif skipT > 0:
                skipT -= 1  # Backspace the number of times calculated in the previous step
                j = j - 1

            else:
                break

        print("Comparing", S[i], T[j])  # Print out the characters for better understanding.

        if i >= 0 and j >= 0 and S[i] != T[j]:  # Compare both valid characters. If not the same, return False.
            return False

        if (i >= 0) != (j >= 0):  # Also ensure that both the character indices are valid. If it is not valid,
            return False  # it means that we are comparing a "#" with a valid character.

        i = i - 1
        j = j - 1

    return True  # This means both the strings are equivalent.
    #


# O(M+N), O(M+N)
def backspaceCompare(S, T):
    def build(S):
        ans = []

        for c in S:
            # if curr != "#' append into stack
            if c != '#':
                ans.append(c)
            # if curr =='#' stack pop
            elif ans:
                ans.pop()
        # return string of stack
        return "".join(ans)

    return build(S) == build(T)
