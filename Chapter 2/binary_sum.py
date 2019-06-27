def binary_length(number):
    return len(bin(number)) - 2

def to_binary_list(number, length=None):
    if length is None:
        length = binary_length(number)

    result = [0] * length

    for i, digit in enumerate(reversed(bin(number)[2:])):
        result[(length - 1) - i] = int(digit)

    return result
    
def from_binary_list(list):
    return int(''.join(map(str, list)), 2)

def binary_sum(a, b):
    carry = 0
    result = [0] * (len(a) + 1)

    for i in range(len(a) - 1, -1, -1):
        result[i + 1] = a[i] + b[i] + carry
        carry = 1 if result[i + 1] > 1 else 0
        result[i + 1] %= 2

    result[0] = carry
    return result