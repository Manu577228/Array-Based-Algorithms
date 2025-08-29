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

# The two pointers technique uses two indices that move through a sequence to solve problems more efficiently,
# often in linear time.
# Typically, pointers either start at opposite ends (closing in) or move in the same direction (fast/slow).

# Two pointers shine when your data has structure (often sorted).
# Common patterns:

# Opposite ends: Start l at the beginning and r at the end; move them inward based on a condition
# (e.g., sum too small → move l, sum too big → move r).

# Same direction (slow/fast): Use a slow pointer to build/track results and a fast pointer to scan
# (e.g., removing duplicates, partitioning).
# Why it’s good: usually O(n) time, O(1) extra space.
# Gotchas: If you sort first, you might lose original indices unless you keep (value, index) pairs.

def two_sum_sorted(a, t):
    l = 0
    r = len(a) - 1
    while l < r:
        s = a[l] + a[r]
        if s == t:
            return (l, r)
        if s < t:
            l += 1
        else:
            r -= 1
    return (-1, -1)


arr = [-2, 1, 2, 4, 7, 11]
T = 9
idx = two_sum_sorted(arr, T)
print("Array:", arr)
print("Target:", T)
print("PairIndices:", idx)
if idx != (-1, -1):
    i, j = idx
    print("Pair Values:", (arr[i], arr[j]))
