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

# The Dutch National Flag Algorithm, proposed by Edsger Dijkstra, is used to sort an array containing only 
# three distinct elements (commonly 0s, 1s, and 2s) in a single traversal with constant extra space.
# It works by maintaining three pointers: low, mid, and high.

# Imagine you have balls of three colors: red, white, and blue. You want to arrange them in order: 
# red first, then white, then blue.

# low pointer → keeps track of the boundary for 0s.

# mid pointer → traverses the array.

# high pointer → keeps track of the boundary for 2s.

# Steps:

# Start with low = 0, mid = 0, high = n-1.

# Traverse while mid <= high:

# If arr[mid] == 0 → swap with arr[low], increment both low and mid.

# If arr[mid] == 1 → just move mid.

# If arr[mid] == 2 → swap with arr[high], decrement high.

# Continue until all elements are partitioned correctly.

def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

arr = [2, 0, 2, 1, 1, 0]
print("Sorted Array:", dutch_national_flag(arr))

# TC : O(n)
# SC : O(1)