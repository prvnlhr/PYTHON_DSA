def manachers(S):
   SS = '#' + '#'.join(S) + '#'
   Z = [0] * len(SS)
   center = right = 0
   for i in range(1, len(SS)):
       if i < right:
           Z[i] = min(right - i, Z[2 * center - i])
       while (min(len(SS) - i - 1, i) > Z[i] and
              SS[i + Z[i] + 1] == SS[i - Z[i] - 1]):
           Z[i] += 1
       if i + Z[i] > right:
           center, right = i, i + Z[i]
   return Z

def solve(S):
   M = manachers(S)[1: -1]
   ans = set()
   for center, expand in enumerate(M):
      for e in range(expand + 1):
        ans.add(S[(center - e)/2 : (center + e)/2])
   return ans



s  = input()
ans = solve(s)
print(ans)