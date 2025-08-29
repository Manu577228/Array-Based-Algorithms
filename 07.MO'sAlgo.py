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

# MO’s Algorithm is a query optimization technique used on 
# static arrays to answer range queries (like sum, frequency, distinct count, etc.) efficiently.
# It sorts the queries in a special order and answers them in approximately O((N + Q) * √N) time.

# Imagine you are asked multiple queries on an array:

# Example query: "What is the sum of elements from index L to R?"
# If you compute each query separately, it may take O(N * Q), which is too slow.

# MO’s Algorithm improves efficiency by:

# Dividing array into blocks of size √N.

# Sorting queries by block index and then by R.

# Maintaining a current range [currL, currR].

# Expand or shrink the range while moving from one query to another.

# Update results efficiently in O(1) or O(logN) time per shift.

# This way, instead of recalculating for each query, 
# we re-use previous calculations by moving the range endpoints smartly.

import math

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
queries = [(0, 4), (1, 3), (2, 8), (0, 8)]

n = len(arr)
block_size = int(math.sqrt(n))

queries_with_index = [(l, r, idx) for idx, (l, r) in enumerate(queries)]
queries_with_index.sort(key=lambda x: (x[0] // block_size, x[1]))

currL, currR, currSum = 0, -1, 0
answers = [0] * len(queries)

for l, r, idx in queries_with_index:
    while currL > l:
        currL -= 1
        currSum += arr[currL]

    while currR < r:
        currR += 1
        currSum += arr[currR]
       
    while currL < l:
        currSum -= arr[currL]
        currL += 1

    while currR > r:
        currSum -= arr[currR]
        currR -= 1

    answers[idx] = currSum

for i, ans in enumerate(answers):
    print(f"Query {i}: Sum = {ans}")
