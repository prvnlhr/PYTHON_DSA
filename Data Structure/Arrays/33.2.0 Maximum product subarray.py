# Input: arr[] = {6, -3, -10, 0, 2}
# Output:   180  // The subarray is {6, -3, -10}
#
# Input: arr[] = {-1, -3, -10, 0, 60}
# Output:   60  // The subarray is {60}
#
# Input: arr[] = {-2, -40, 0, -2, -3}
# Output:   80  // The subarray is {-2, -40}


def maximumProductSubArray(arr, n):
    min_pro_ending_here = arr[0]
    max_pro_ending_here = arr[0]

    max_product_so_far = arr[0]

    # This problem is same as maximum sum ,
    # where we calculated the max_sum_ending ,of a subarray
    # and if at a point max_sum_ending decreased, we would reset it to arr[i]

    # but here the difference, is that,
    # if a negative sum is multiplied with -ve num it can become max product
    # so we will maintain max_product and min_product at every point.

    for i in range(1, n):
        # 1. first find mi product and ma product
        mi = arr[i] * min_pro_ending_here
        ma = arr[i] * max_pro_ending_here

        # 2. now decide min_pro and max_pro ,
        min_pro_ending_here = min(arr[i], mi, ma)
        max_pro_ending_here = max(arr[i], mi, ma)

        # 3. update our ans max_product_so_far
        max_product_so_far = max(max_product_so_far, max_pro_ending_here)

    return max_product_so_far


arr = [1, -2, -3, 0, 7, -8, -2]
ans = maximumProductSubArray(arr, len(arr))
print(ans)
