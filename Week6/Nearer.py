"""Nearer"""
def main(alice, bob, x):
    """main Nearer"""
    pigut_alice = abs(alice - x)
    pigut_bob = abs(bob - x)
    if pigut_alice > pigut_bob:
        print(f"Bob {pigut_bob}")
    elif pigut_bob > pigut_alice:
        print(f"Alice {pigut_alice}")
    else:
        print(f"Sundaes {pigut_bob}")
main(int(input()), int(input()), int(input()))
