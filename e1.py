def mo (x,xx):
    xx [0] = xx [1]
    d = xx [0]
    b = x[0] - xx[0]
    if b < 0 :
        return ("t.n = n.(%i) - %i" %(d,abs(b)) )  
    elif b == 0 :
        return ("t.n = n.(%i)" %(d))
    else:  
        return ("t.n = n.(%i) + %i" %(d,b) )



t = [int(input('t.1   ')),int(input('t.2   ')),int(input('t.3   '))]
tt = [int(),t[1]-t[0],t[2]-t[1]]
ttt = [int(),int(),tt[2]-tt[1]]

if ttt[2] == 0 :
    print (mo (t,tt))
else:
    if ttt[2] > 0:

    else:
        






















q =1











