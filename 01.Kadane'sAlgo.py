# /* ----------------------------------------------------------------------------  */
# /*   ( The Authentic JS/JAVA/PYTHON CodeBuff )
#  ___ _                      _              _ 
#  | _ ) |_  __ _ _ _ __ _ __| |_ __ ____ _ (_)
#  | _ \ ' \/ _` | '_/ _` / _` \ V  V / _` || |
#  |___/_||_\__,_|_| \__,_\__,_|\_/\_/\__,_|/ |
#                                         |__/ 
#  */
# /* --------------------------------------------------------------------------   */
# /*    Youtube: https://youtube.com/@code-with-Bharadwaj                        */
# /*    Github : https://github.com/Manu577228                                  */
# /*    Portfolio : https://manu-bharadwaj-portfolio.vercel.app/portfolio      */
# /* -----------------------------------------------------------------------  */

# Kadane’s Algorithm is a dynamic programming approach to find
# the maximum sum of a contiguous subarray in an array.
# It efficiently solves the problem in O(n) time using a single pass.
#
# Explanation
#
# The idea is to scan through the array and keep track of the maximum subarray sum ending at each position.
#
# At every index, we have two choices:
# 1) Extend the previous subarray with the current element.
# 2) Start a new subarray from the current element.
#
# We take the maximum of these choices and update the global maximum.

def kadane(arr):
    max_so_far = arr[0]
    curr_max = arr[0]
    for i in range(1, len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum Subarray Sum:", kadane(arr))

# TC : O(n)
# SC : O(1)
