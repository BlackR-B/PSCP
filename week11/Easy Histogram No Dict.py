"""Easy Histogram No Dict"""
def main():
    """main Easy Histogram No Dict"""
    letter = input()
    counts = [0] * 52
    for char in letter:
        if 'a' <= char <= 'z':
            counts[ord(char) - ord('a')] += 1
        elif 'A' <= char <= 'Z':
            counts[ord(char) - ord('A') + 26] += 1
    for i in range(26):
        if counts[i] > 0:
            print(chr(i + ord('a')) + " = " + str(counts[i]))
        if counts[i + 26] > 0:
            print(chr(i + ord('A')) + " = " + str(counts[i + 26]))
main()
