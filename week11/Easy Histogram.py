"""Easy Histogram"""
def main():
    """Main Easy Histogram"""
    letter = input()
    freq = [0] * 52
    for char in letter:
        if 'a' <= char <= 'z':
            freq[ord(char) - ord('a')] += 1
        elif 'A' <= char <= 'Z':
            freq[ord(char) - ord('A') + 26] += 1
    for i in range(26):
        if freq[i] > 0:
            print(chr(i + ord('a')) + " = " + str(freq[i]))
        if freq[i + 26] > 0:
            print(chr(i + ord('A')) + " = " + str(freq[i + 26]))
main()
