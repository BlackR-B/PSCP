"""Duplicate I"""
def main():
    """Main Duplicate I"""
    m = int(input())
    n = int(input())
    group1 = set()
    for _ in range(m):
        group1.add(input().strip())
    group2 = set()
    for _ in range(n):
        group2.add(input().strip())
    common_students = group1.intersection(group2)
    if common_students:
        for student in sorted(common_students, key=int, reverse=True):
            print(student)
    else:
        print("Nope")
main()
