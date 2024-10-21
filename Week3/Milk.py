"""Milk"""
def full_bottles(price, need, cap, money):
    """main MILK"""
    bottles = money // price
    caps = bottles
    while caps >= need > 0:
        new_bottles = (caps // need) * cap
        bottles += new_bottles
        caps = (caps % need) + new_bottles
    print(bottles)
full_bottles(int(input()),int(input()),int(input()),int(input()))
