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

# Sliding Window is a technique to process contiguous subarrays/substrings by “sliding” 
# a window over the input and updating answers in O(1) per move.
# It turns many brute-force O(n·k) scans into O(n) by reusing work from the previous window.

# Think of a window as two pointers over a linear structure (array/string):

# Fixed-size window: window length is constant (e.g., “max sum of any k-length subarray”). 
# Move the right edge one step right and drop the leftmost element—update your running state in O(1).

# Variable-size window: expand the right edge while a condition holds; 
# when it breaks (e.g., duplicates appear), shrink from the left until the condition is restored. 
# Track the best window during the process.

# Fixed size Sliding Window : Max sum of any subarray of length k
def max_sum_k(a, k):
    n = len(a)
    if k <= 0 or k > n:
        return 0, -1, -1
    s = 0
    for i in range(k):
        s += a[i]
    best = s
    bi = 0
    for i in range(k, n):
        s += a[i]
        s -= a[i - k]
        if s > best:
            best = s
            bi = i - k + 1
    bj = bi + k - 1
    return best, bi, bj

# Variable-size Sliding Window : Longest substring without repeating characters
def longest_unique_substr(t):
    pos = {}
    l = 0
    best_len = 0
    bl = 0
    for r, ch in enumerate(t):
        if ch in pos and pos[ch] >= l:
            l = pos[ch] + 1
        pos[ch] = r
        cur_len = r - l + 1
        if cur_len > best_len:
            best_len = cur_len
            bl = l
    return t[bl:bl + best_len], bl, best_len

if __name__ == "__main__":
    a = [2, 1, 5, 1, 3, 2]
    k = 3
    best_sum, i, j = max_sum_k(a, k)

    s = "abccabb"
    sub, st, ln = longest_unique_substr(s)

    print("Example 1 (Fixed-size):")
    print("Array:", a, "k:", k)
    print("MaxSum:", best_sum, "Window:", a[i:j+1], "StartIndex:", i, "EndIndex", j)

    print("Example 2 (Variable-Size):")
    print("String:", s)
    print("LongestUniqueLen:", ln, "Substring:", repr(sub), "StartIndex:", st)

