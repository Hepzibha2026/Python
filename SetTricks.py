# Create a set
# Unordered collection of unique items.
nums = {1, 2, 2, 3}
print(nums)

# Add and Remove items
s = {1, 2}
s.add(3)
s.remove(1)

# Set Operations
# Perfect for comparisons.
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b) # intersection
print( a | b) # union
print(a - b) # difference

# Check membership (super fast)
# Sets are optimized for lookups
a = {1, 3, 2}

if 3 in a:
    print("Found")

# Remove duplicates instantly
unique = set([1, 1, 2, 3, 3])
print(unique) # {1, 2, 3}

