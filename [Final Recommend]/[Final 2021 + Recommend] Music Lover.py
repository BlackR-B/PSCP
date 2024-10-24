'''musiclover'''
def musiclover():
    '''music'''
    list_dict = {}
    for _ in range(int(input())):
        name = input().split('-')
        if name[0] not in list_dict:
            list_dict[name[0]] = []
            list_dict[name[0]].append(name[1].strip())
        else:
            list_dict[name[0]].append(name[1].strip())
    for j in list_dict.items():
        print(j[0])
        for x in j[1]:
            print(x)
musiclover()
