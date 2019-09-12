# Slicing Tutorial

#Learning how to extract a substring (Part of a String) from a string by using the Slice method.

# 1.   [:] will extract the entire sequence from the beginning to end.
# 2.  [start :] specify start offset to end of string
# 3.  [: end] specifies from the beginning to the end offset minus 1.
# 4.  [start : end] indicates from the start offset to the end offset minus 1
# 5.  [start : end : step] extracts from the start offset to the end minus 1, skipping characters by the step

numbers = '1234567890'

print('1. ' + numbers[:])
print('2. ' + numbers[3:])
print('3. ' + numbers[:3])
print('4. ' + numbers[1:2])
print('5. ' + numbers[0:10:2])

print(numbers[2])