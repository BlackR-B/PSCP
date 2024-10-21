"""Parity"""
def bits_of_data(data, parity_type):
    """main bits_of_data"""
    count_ones = 0
    for i in data:
        if i == "1":
            count_ones += 1
    if parity_type == "Even":
        parity_bit = "1" if count_ones % 2 else "0"
    else:
        parity_bit = "0" if count_ones % 2 else "1"
    print(data + parity_bit)
bits_of_data(input(), input())
