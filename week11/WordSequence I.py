"""WordSequence I"""
def main():
    """Main WordSequence I"""
    word = input()
    for i in range(1, len(word) + 1):
        print(word[:i])
main()
