l1 = ['a', 'i', 'y', 'e', 'o', 'u']
l2 = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
len_1 = len(l1)
len_2 = len(l2)

while True:
    try:
        s = input().strip()
        for i in s:
            up = 0
            if i.isupper():
                up = 1
                i = i.lower()
            if i in l1:
                if up == 1:
                    print(l1[l1.index(i) - 3 % len_1].upper(), end='')
                else:
                    print(l1[l1.index(i) - 3 % len_1], end='')
            elif i in l2:
                if up == 1:
                    print(l2[l2.index(i) - 10 % len_2].upper(), end='')
                else:
                    print(l2[l2.index(i) - 10 % len_2], end='')
            else:
                print(i, end='')
        print()
    except:
        break