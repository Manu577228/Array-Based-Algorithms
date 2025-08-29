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

# The Merge Intervals algorithm is used to combine overlapping intervals into a single interval.
# It ensures that the final result contains only non-overlapping intervals covering the same ranges.

# Explanation :

# We are given a list of intervals (each interval has a start and end).

# Two intervals overlap if the start of one lies within the other.

# To merge intervals:

# Sort intervals by their starting time.

# Compare the current interval with the last merged interval.

# If they overlap → merge them (take min start, max end).

# If not → add the interval as it is.

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])

        else:
            merged.append(current)

    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Input:", intervals)

result = merge_intervals(intervals)
print("Merged Intervals:", result)
