#kandane algorithm to find the maximum sum of sub array

def maxSubArraySum(aArray):
    max_ending_here = 0
    max_so_far = 0

    for i in range(len(aArray)):
        max_ending_here = max_ending_here + aArray[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


a = [-2, -3, -4, 1, -2, 1, 5, -3]
print ("Maximum contiguous sum is" , maxSubArraySum(a))

