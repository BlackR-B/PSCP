"""Run Length Encoding"""
def main(endcoding):
    """main"""
    if not endcoding:
        print("")
        return
    encoded_string = ""
    current_char = endcoding[0]
    count = 1
    for char in endcoding[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_string += f"{count}{current_char}"
            current_char = char
            count = 1

    encoded_string += f"{count}{current_char}"
    print(encoded_string)
main(input().strip())
