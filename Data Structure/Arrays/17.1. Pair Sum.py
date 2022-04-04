def PairSum(arr, n, x):
    pairCount = 0
    for i in range(len(arr)):

        for j in range(i + 1, len(arr)):

            if (arr[i] + arr[j] == x):
                pairCount = pairCount + 1
    return pairCount


n = int(input())
arr = [int(i) for i in input().split()]
x = int(input())
print(PairSum(arr, n, x))
