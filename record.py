def record():
    yn = True
    while yn:
        l = input('name, date, set, raps, weight : \n')
        k = list(l.split(','))
        k[0] = str(k[0])
        k[1] = int(k[1])
        k[2] = int(k[2])
        k[3] = float(k[3])
        k[4] = float(k[4])
        kt = (k[0], k[1], k[2], k[3], k[4])
        print('{0} transform success \nData is {1} Right? (Y/N)'.format(type(kt), kt))
        s = input()
        if s == 'Y':
            c.execute("INSERT INTO Record(name, 'date', 'set', raps, weight) VALUES(?,?,?,?,?)", kt)
            yn = False
        elif s == 'N':
            pass