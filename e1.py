def tt1 (x,xx,xxx):
    xx.clear()
    xxx.clear()
    for q in range (0,len(x)):
        xx.append(int())
        xxx.append(int())

    
    for q in range (1,len(x)):
        xx[q] = x[q] - x[q-1]
    
    xx[0] = xx[1] - (xx[2]-xx[1])

    for q in range(1,len(x)):
        xxx[q] = xx [q] - xx [q-1]

    xxx [0] = xxx[1]



def mo1 (x,xx):
    xx [0] = xx [1]
    d = xx [0]
    b = x[0] - xx[0]
    if b < 0 :
        return ("t.n = %in - %i" %(d,abs(b)) )  
    elif b == 0 :
        return ("t.n = %in" %(d))
    else:  
        return ("t.n = %in + %i" %(d,b) )

def mo2 (x,xx,xxx) :
    a = xxx[0]/2
    d = xx[0] - a
    b = x[0] - xx[0]
    return [a,d,b]
    






t = [int(input('t.1   ')),int(input('t.2   ')),int(input('t.3   '))]
tt = []#[int(),t[1]-t[0],t[2]-t[1]]
ttt = []#[int(),int(),tt[2]-tt[1]]
tt1 (t,tt,ttt)


if ttt[2] == 0 :
    print (mo1 (t,tt))
else:
    t.append(int(input('t.4   ')))
    tt1(t,tt,ttt)
    if ttt[2] < 0:
        z =0
    else:
        www = mo2 (t,tt,ttt)























q =1











