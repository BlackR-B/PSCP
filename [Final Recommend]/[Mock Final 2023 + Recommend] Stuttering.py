"""[Mock Final 2023 + Recommend] Stuttering"""
def main():
    """[Mock Final 2023 + Recommend] Stuttering"""
    words = input().split()
    result = []
    for word in words:
        if not result or result[-1] != word:
            result.append(word)
    print(' '.join(result))
main()
