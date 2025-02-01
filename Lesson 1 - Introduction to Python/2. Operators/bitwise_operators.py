##########################################################
#                  BITWISE OPERATORS                     #
##########################################################

x = 6 # binary: 110
y = 3 # binary: 011
z = 8
# Bitwise AND
and_result = x & y    # result: 010 output: 2

# Bitwise OR
or_result = x | y    # result: 111 output: 7

# Bitwise XOR
xor_result = x ^ y   # result: 101 output: 5

# Bitwise NOT
not_result = ~z      # result: -111 output: -7
print(not_result)
# ~z = -(z + 1) 

# Left Shift
left_shift = x << 2  # result: 1100 output: 12
print(left_shift)
# x * (2^n)

# Right Shift
right_shift = z >> 1 # result: 011 output: 3
print(right_shift)
# z // (2^n)

