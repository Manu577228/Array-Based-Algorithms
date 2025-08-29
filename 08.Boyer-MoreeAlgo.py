# The Boyer-Moore Majority Vote Algorithm is a linear-time algorithm used 
# to find the majority element in an array (the element that appears more than ⌊n/2⌋ times).
# It works by maintaining a candidate and a counter while traversing the array in one pass.

# Explanation

# The idea is to keep track of a candidate element that could be the majority.

# We maintain a count:

# If count becomes 0, we pick the current element as the new candidate.

# If the current element equals the candidate → increment count.

# Otherwise → decrement count.

# At the end, the candidate is the potential majority element (needs a second pass to verify in some variations).

def majority_element(nums):
    candidate, count = None, 0

    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

arr = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(arr)
print("Majority Element:", result)

        
