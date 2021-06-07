
pheptinh = []
def tinh(string,string2,sum):
    if not string:
        return
    if sum + int(string) == 100:
        pheptinh.append(string2+'+'+string)
        return
    for i in range(len(string)):
        tinh(string[i+1:], string2+'+'+string[:i+1], sum +
                  int(string[:i+1]))
        tinh(string[i+1:], string2+'-'+string[:i+1], sum -
                  int(string[:i+1]))

tinh("123456789",'',0)
for i in pheptinh:
    print(i)
