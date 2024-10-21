"""Fever"""
def main():
    """Main Fever"""
    cold = float(input())
    if 36 <= cold < 38:
        print("No Fever")
    elif 38 <= cold < 39:
        print("Mild Fever")
    elif 39 <= cold < 40:
        print("High Fever")
    else:
        print("Very High Fever")
main()
