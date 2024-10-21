"""[Mock Midterm 2023 + Recommend] Bad Keyboard"""
def main(text):
    """Main [Mock Midterm 2023 + Recommend] Bad Keyboard"""
    swap = ""
    for i in text:
        if i == "i":
            i = "o"
        elif i == "o":
            i = "i"
        elif i == "I":
            i = "O"
        elif i == "O":
            i = "I"
        swap += i
    print(swap)
main(input())
