'''rasamee'''
def circle(r):
    '''calculation pizza circle'''
    pe = 3.14159265358979323846
    area = pe * (r ** 2)
    circeo = 2 * pe * r
    return area ,circeo
def main():
    '''INPUT DEEEE'''
    r = float(input())
    area ,circeo = circle(r)
    print(f"Area: {area:.3f}")
    print(f"Circumference: {circeo:.3f}")
main()
