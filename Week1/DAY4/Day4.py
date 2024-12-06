import time
#### THIS SOLUTION IS INCOMPLETE AND SHOULD NOT BE USED FOR AOC UNTIL THIS MESSAGE IS REMOVED ####
key = 'XMAS'
apr = []
c = 0

def wordCheck(data):
    return apr.append(data) if key in data or key[::-1] in data else None

def listwordCheck(data):
    print(data)
    if data == "XMAS":
        apr.append(data)
    elif data == "SAMX":
        apr.append(data)
    else:
        False

def FindStuff(l1,word):
    a1,a2,a3,a4 = l1[0], l1[1], l1[2], l1[3]
    a1, a2, a3, a4 = a1.strip(),a2.strip(),a3.strip(),a4.strip()
    for i in range(len(a1) - 3):
        lr = a1[i:i + 4]
        listwordCheck(lr)
        dlr, drl = (a1[i], a2[i + 1], a3[i + 2], a4[i + 3]), (a1[i + 3], a2[i + 2], a3[i + 1], a4[i])
        dlrt, drlt = ''.join(dlr), ''.join(drl)
        wordCheck(dlrt), wordCheck(drlt)

    for i in range(len(a1)):
        tb = (a1[i], a2[i], a3[i], a4[i])
        tbs = ''.join(tb)
        wordCheck(tbs)
    return

#### PART 1 ONLY

def dumAh(wor):
    with open('Day4Data.txt', 'r') as f:
        text = f.readlines()
        lines = len(text)
        for i in range(0, lines - len(wor)+1):
            FindStuff(text[i:i+4], len(wor))

        for line in range(1, 4):
            for i in range(len(text[-line]) - 3):
                wordCheck(text[-line][i:i + len(wor)])


dumAh("XMAS")
print(len(apr))

#### THIS SOLUTION IS INCOMPLETE AND SHOULD NOT BE USED FOR AOC UNTIL THIS MESSAGE IS REMOVED ####

'''
Will not be doing part 2. 
Minus-202412060949
'''