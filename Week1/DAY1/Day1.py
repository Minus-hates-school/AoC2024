File = 'Day1Data.txt'

with open(File, 'r') as f:
    x, y, dif, sim, fin = [],[],[],[], []
    for line in f:
        set = line.split('   ')
        x.append(set[0]), y.append(set[1].strip())
    x.sort(), y.sort()
    for num in range(1000):
        l, r = int(x[num]), int(y[num])
        dif.append(abs(l - r))
        c = y.count(str(l))
        sim.append(c)
    for S in range(1000):
        n, s = int(x[S]), int(sim[S])
        fin.append(n*s)
    print(sum(dif))
    print(sum(fin))


