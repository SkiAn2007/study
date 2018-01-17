import sys

temp = 0
good = 0
result = []
rangedata = []
maskalist = []
calc = 0


def maincheck(oktet):
    good = 0
    try:
        temp = int(oktet)
    except ValueError:
        good = 0
    except Exception:
        good = 0
    else:
        good = 1
    return good


def bit2dec(bit):
    otvet = 0
    bit = 8 - int(bit)
    for bitt in range(bit, 8):
        otvet += (2 ** bitt)
    return int(otvet)


def checkoktet(oktet):
    otvet = 0
    good = maincheck(oktet)
    if (good):
        temp = int(oktet)
        if ((temp >= 0) and (temp <= 255)):
            otvet = 1
    return int(otvet)


def checkrange2(iprange2):
    ipstr = ''
    ipstr2 = ''
    zaza = 0
    for x in iprange2:
        if (zaza <= 3):
            ipstr += str(format(int(x), '08b'))
        else:
            ipstr2 += str(format(int(x), '08b'))
        zaza += 1
    if ((int(ipstr, 2) < int(ipstr2, 2))):
        print("this is subnet")
    else:
        print("unknown")


def checkrange(oktet):
    data = str(oktet)
    rangeflag = 0
    otvet = 0
    rangeflag = oktet.count('-')
    if (rangeflag == 1):
        res = data.split('-')
        if (checkoktet(res[0]) == 1):
            otvet += 1
            rangeip.append(int(res[0]))
        if (checkoktet(res[1]) == 1):
            otvet += 1
            rangeip.append(int(res[1]))
    if (otvet == 2):
        otvet = 1
    return int(otvet)


def checkmask2(bit):
    otvet = 0
    maska = 1
    bit = int(bit)
    maskstr = ''
    ipstr = ''
    for bitt in maskalist:
        ipstr += str(format(int(bitt), '08b'))
    for bitt in range(32):
        if (maska <= bit):
            maskstr += '1'
        else:
            maskstr += '0'
        maska += 1
    if ((int(ipstr, 2) & int(maskstr, 2)) == int(ipstr, 2)):
        return 1
    else:
        return 0


def checkmask(oktet):
    data = str(oktet)
    maskflag = 0
    otvet = 0
    maskflag = oktet.count('/')
    if (maskflag == 1):
        res = data.split('/')
        if (checkoktet(res[0]) == 1):
            otvet += 1
            maskalist.append(int(res[0]))
        if (checkoktet(res[1]) == 1):
            if ((int(res[1]) >= 0) and (int(res[1]) <= 32)):
                otvet += 1
    if (otvet == 2):
        otvet = checkmask2(int(res[1]))
    return int(otvet)


i = 0
for args in sys.argv:
    if i > 0:
        print(i, ": ", args)
        inputdata = args.split('.')
        maskalist = []
        rangedata = []
        rangeip = []
        calc = 0
        if (len(inputdata) == 4):
            j = 0
            flag = 0
            for okto in inputdata:
                if ((j != 3) and (checkoktet(okto) == 1)):
                    calc += 1
                    maskalist.append(int(okto))
                elif ((j == 3) and (checkoktet(okto) == 0)):
                    flag = checkmask(okto)
                elif (checkoktet(okto) == 1):
                    calc += 1
                    maskalist.append(int(okto))
                j += 1
            if (calc == 4):
                print('this is ip')
            if ((calc == 3) and (flag == 1)):
                print('this is subnet')
            if ((calc < 4) and (flag == 0)):
                print('unknown')
        if (len(inputdata) == 7):
            j = 0
            flag = 0
            for okto in inputdata:
                if (j == 3):
                    flag = okto.count('-')
                    if (flag == 1):
                        temp = okto.split('-')
                        if (checkoktet(temp[0]) == 1):
                            rangeip.append(int(temp[0]))
                        if (checkoktet(temp[1]) == 1):
                            rangeip.append(int(temp[1]))
                elif ((j != 3) and (checkoktet(okto) == 1)):
                    rangeip.append(int(okto))
                j += 1
            if (len(rangeip) == 8):
                checkrange2(rangeip)
            else:
                print("unknown")

        if ((len(inputdata) != 7) and (len(inputdata) != 4)):
            print('unknown')
    i += 1
