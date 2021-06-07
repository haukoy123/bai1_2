def tim_buoc(x, y):
    sobuoc=0
    buoc=''
    if x > y:
        print('loi!!!, nhap y phai lon hon x')
        return sobuoc, buoc

    while(True):
        if x > y:
            x -= 1
            buoc += "-"
        elif x * 2 <= y:
            x = x * 2
            buoc += '*'
        elif x * 2 > y:
            x = x * 2
            buoc += '*'
        elif x * 2 > y:
            x = x-1
            buoc += '-'
        sobuoc += 1
        if x == y:
            return sobuoc, buoc

sobuoc,buoc=tim_buoc(4,8)
print('so buoc', sobuoc)
print('cac buoc', buoc)
