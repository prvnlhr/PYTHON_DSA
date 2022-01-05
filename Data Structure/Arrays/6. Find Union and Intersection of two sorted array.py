# Ex__1.
# Input : arr1[] = {1, 3, 4, 5, 7}
#         arr2[] = {2, 3, 5, 6}
# Output : Union : {1, 2, 3, 4, 5, 6, 7}
#          Intersection : {3, 5}
#
# Ex__2.
# Input : arr1[] = {2, 5, 6}
#         arr2[] = {4, 6, 8, 10}
# Output : Union : {2, 4, 5, 6, 8, 10}
#          Intersection : {6}

def intersection(arr1, arr2):
    interSect_val = -1
    i = 0
    j = 0
    arr = []

    # MERGE TWO SORTED ARRAY CONCEPT
    while i < len(arr1) and j < len(arr2):

        if (arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i = i + 1
        elif (arr1[i] > arr2[j]):
            arr.append(arr2[j])
            j = j + 1


        else:
            # INTERSECTION POINT
            interSect_val = arr1[i]
            arr.append(arr1[i])
            i = i + 1
            j = j + 1

    # LOOP FOR REMAINING ELEMENTS
    while i < len(arr1):
        arr.append(arr1[i])
        i = i + 1
    while j < len(arr2):
        arr.append(arr2[j])
        j = j + 1
    return arr, interSect_val


arr1 = [int(i) for i in input().strip().split()]
arr2 = [int(j) for j in input().strip().split()]

ans = intersection(arr1, arr2)
print(ans[0], ans[1])
