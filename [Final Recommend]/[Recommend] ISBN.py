"""[Recommend] ISBN"""
def main(x):
    """[Recommend] ISBN"""
    code = x.replace("-", "")
    check = code[-1]
    new = code[:len(code)-1]
    result = 0
    for i, j in enumerate(new):
        result += (10-i)*int(j)
    final = (-result)%11
    if final == 10:
        final = "X"
    print("Yes"if str(final) == check else f"No {final}")
main(input())
