# Ex__1.  [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# O/P --> [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
# Observation , we want at even position(0,2,4.. ) all negative element
#               and at odd position(1,3,5..) all positive element
# EASY QUESTION


# STEPS:
#  for index 0 --> len(arr):
#       check if element is out_of_place
#         (a element is said to be out_of_place if at odd index --> negative element or  even index --> positive element)
#       if we have out_of_place index , that means we need to replace it with correct element
#           now , what is correct replacement for a out_of_place element
#         (if a out_of_place element --> negative , we want a next positive element and vice-versa
#       now, if we find a correct replacement ,
#           we need to replace it and shift all elements one place left


# All Helper functions::
def check_if_element_is_out_of_place(index, element):
    return (element < 0 and index % 2 == 1) or (element >= 0 and index % 2 == 0)


def check_if_element_is_fit_for_replace(curr_element, out_of_place_ele):
    return curr_element >= 0 and out_of_place_ele < 0 or curr_element < 0 and out_of_place_ele >= 0


def left_shift_arr(arr, curr, out_of_place_index):
    temp_save = arr[curr]
    for i in range(curr, out_of_place_index, -1):
        arr[i] = arr[i - 1]
    arr[out_of_place_index] = temp_save
    return arr


def rearrangeAlternateNePo(arr):
    outOfPlaceIndex = -1
    for i, ele in enumerate(arr):

        if outOfPlaceIndex >= 0:

            isCorrectReplacement = check_if_element_is_fit_for_replace(ele, arr[outOfPlaceIndex])
            arr = left_shift_arr(arr, i, outOfPlaceIndex)

        elif outOfPlaceIndex == -1:
            isOutOfPlace = check_if_element_is_out_of_place(i, ele)
            outOfPlaceIndex = i


def rearrangeAlternate(arr):
    out_of_place_index = -1

    for index in range(len(arr)):

        if out_of_place_index >= 0:

            # check if a element is out of place
            if check_if_element_is_fit_for_replace(arr[index], arr[out_of_place_index]):
                arr = left_shift_arr(arr, index, out_of_place_index)

                if index - out_of_place_index > 2:
                    out_of_place_index = out_of_place_index + 2
                else:
                    out_of_place_index = -1

        if out_of_place_index == -1:
            if check_if_element_is_out_of_place(index, arr[index]):
                out_of_place_index = index
    return arr


arr = [int(i) for i in input().strip().split()]
ans = rearrangeAlternate(arr)
print(ans)
