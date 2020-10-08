
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
    out = str()
    a = xxx[0]/2
    d = xx[0] - a
    b = x[0] - xx[0]
    if a % 1 != 0:
        if a == 0.5:
            d -= 0.5
            out += ("((n.(n + 1)) /2) ")
        else:
            d -= 0.5
            out += ("%sn^2 + ((n.(n + 1)) /2) " %str(a//1))
    else:
        out += ("%sn^2 " %str(int(a)))
    
    if round(d,0) == d:
        d = int(d)


    if round(b,0) == b:
        b = int(b)

    
    if d > 0 :
        out += ("+%sn " %str(d))
    elif d < 0 :
        out += ("-%sn " %str(abs(d)))
    
    if b > 0 :
        out += ("+%s" %str(b))
    elif b < 0 :
        out += ("-%s" %str(abs(b)))
    
    return out
    






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
        print (mo2 (t,tt,ttt))























#q =1











