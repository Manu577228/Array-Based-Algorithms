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

# Prefix Sum (aka cumulative sum) is an array where each element
# at index i stores the sum of all elements from the original array up to i.
# It allows answering range-sum queries (sum of arr[l..r]) in O(1) after an O(n) preprocessing.

# Compute a prefix array where prefix[i] = arr[0] + arr[1] + ... + arr[i].
# Then the sum of any subarray arr[l..r] (inclusive) is:

# prefix[r] if l == 0, otherwise

# prefix[r] - prefix[l-1].

# Use-cases: fast range-sum queries, converting repeated range queries from O(length) to
# O(1), 1D & 2D cumulative sums, and difference-array tricks for fast range updates.

def build_prefix(arr):
    pref = [0] * len(arr)
    for i, val in enumerate(arr):
        if i == 0:
            pref[i] = val
        else:
            pref[i] = pref[i - 1] + val
    return pref


def range_sum(pref, l, r):
    if l == 0:
        return pref[r]
    return pref[r] - pref[l - 1]


arr = [3, 1, 4, 1, 5, 9]
print("Original Array:", arr)

pref = build_prefix(arr)
print("Prefix Sums: ", pref)

queries = [(0, 2), (2, 4), (1, 5)]
for l, r in queries:
    s = range_sum(pref, l, r)
    print(f"Sum arr[{l}..{r}] = {s}")

# Preprocessing: O(n) , Extra space : O(n)
# Query Time : O(1)
