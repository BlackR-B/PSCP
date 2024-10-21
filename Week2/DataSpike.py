"""DataSpike"""
def more(a,b):
    """PPAP"""
    if a > b:
        return a
    return b
def main():
    """Calculation DataSpike"""
    Data1 = int(input())
    Data2 = int(input())
    Data3 = int(input())
    Data4 = int(input())
    Data5 = int(input())
    Data6 = int(input())
    Data7 = int(input())
    Data8 = int(input())
    ans = more(Data8,more(Data7,more(Data6,more(Data5,more(Data4,more(Data3,more(Data2,Data1)))))))
    print(ans)
main()
