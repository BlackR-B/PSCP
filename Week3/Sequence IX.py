"""Sequencepoint"""
def main(point):
    """function"""
    for i in range(point,0,-1):
        num = 1
        for j in range(1,point+1*(point-i+1)):
            if j < i:
                print("  ",end =" ")
            else:
                if j > point:
                    num -= 1
                    print(f"{num:02}", end=" ")
                else:
                    print(f"{num:02}", end=" ")
                    if j == point:
                        continue
                    num += 1
        print()
main(int(input()))
