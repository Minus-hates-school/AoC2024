import time
#### THIS SOLUTION IS INCOMPLETE AND SHOULD NOT BE USED FOR AOC UNTIL THIS MESSAGE IS REMOVED ####
key = 'XMAS'
apr = []


def wordCheck(data):
    return apr.append(data) if key in data or key[::-1] in data else None


def FindStuff(l1,word):
    a1,a2,a3,a4 = l1[0], l1[1], l1[2], l1[3]
    a1, a2, a3, a4 = a1.strip(),a2.strip(),a3.strip(),a4.strip()
    for i in range(len(a1)-3):
        lr = a1[i:i+word]
        dlr, drl = (a1[i], a2[i + 1], a3[i + 2], a4[i + 3]), (a1[i + 3], a2[i + 2], a3[i + 1], a4[i])
        dlrt, drlt = ''.join(dlr), ''.join(drl)
        wordCheck(lr), wordCheck(dlrt), wordCheck(drlt)
    for i in range(len(a1)):
        tb = (a1[i], a2[i], a3[i], a4[i])
        tbs = ''.join(tb)
        wordCheck(tbs)
    return

#### THIS SOLUTION IS INCOMPLETE AND SHOULD NOT BE USED FOR AOC UNTIL THIS MESSAGE IS REMOVED ####

def dumAh(wor):
    with open('Day4Data.txt', 'r') as f:
        text = f.readlines()
        lines = len(text)
        for i in range(lines - len(wor) + 1):
            FindStuff(text[i:i+4], len(wor))


dumAh("XMAS")
print(len(apr))

#### THIS SOLUTION IS INCOMPLETE AND SHOULD NOT BE USED FOR AOC UNTIL THIS MESSAGE IS REMOVED ####

'''
Day 4 will be revisited at a later date as well as day 2. 
2258 is current count. 
Minus-202412051159
'''