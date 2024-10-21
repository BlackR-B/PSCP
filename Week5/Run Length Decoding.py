"""Run Length Decoding"""
def main(encoded):
    """main Run Length Decoding"""
    decoded = ""
    count = 0
    for char in encoded:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            decoded += char * count
            count = 0
    print(decoded)
main(input().strip())
