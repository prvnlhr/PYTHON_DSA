def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    ans = (n + m) * [0]
    i = 0
    j = 0
    k = 0
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            ans[k] = nums1[i]
            k = k + 1
            i = i + 1
        else:
            ans[k] = nums2[j]
            k = k + 1
            j = j + 1

    while i < n:
        ans[k] = nums1[i]
        k = k + 1
        i = i + 1

    while j < m:
        ans[k] = nums2[j]
        k = k + 1
        j = j + 1

    print(ans)
    l = len(ans)
    mid = l // 2
    if (l % 2 == 0):
        median = ans[mid] + ans[mid - 1]
        return median / 2
    else:
        return ans[mid]


nums1 = [int(i) for i in input().split()]
nums2 = [int(i) for i in input().split()]
print(findMedianSortedArrays(nums1, nums2))
