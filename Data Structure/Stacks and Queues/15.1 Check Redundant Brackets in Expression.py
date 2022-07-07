# O(n) and O(1) simple sol:
def checkRedundancy(s):
    bracketCount = 0
    operatorCount = 0

    for i in range(len(s)):
        if s[i] == '(' and s[i + 2] == ')':
            return True
        if s[i] == '*' or s[i] == '-' or s[i] == '+' or s[i] == '/':
            operatorCount += 1
        if s[i] == '(':
            bracketCount += 1
    if bracketCount > operatorCount:
        return True
    return False


# O(n) and O(n) stack:
def checkRedundant(string):
    s = []
    l = len(string)
    flag = False
    for i in range(l):

        if i != ')':
            s.append(i)

        else:
            while s[-1] != '(':
                s.pop()
                flag = True
                if len(s) == 0:
                    break

            if len(s) == 0:
                continue
            if flag:
                s.pop()
                flag = False
            else:
                return True
    return


def checkRedundancy(Str):
    # create a stack of characters
    st = []

    # Iterate through the given expression
    for ch in Str:
        # if current character is close parenthesis ')'
        if (ch == ')'):
            top = st[-1]
            st.pop()
            # If immediate pop have open parenthesis '(' duplicate brackets found
            flag = True

            while (top != '('):
                # Check for operators in expression
                if (top == '+' or top == '-' or top == '*' or top == '/'):
                    flag = False
                # Fetch top element of stack
                top = st[-1]
                st.pop()

            # If operators not found
            if (flag == True):
                return True
        else:
            st.append(ch)  # append open parenthesis '(',  operators and operands to stack
    return False


string = input()
ans = checkRedundancy(string)
if ans is True:
    print('true')
else:
    print('false')
