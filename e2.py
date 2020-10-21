




def print_j(x):
    wer = 0
    n = 0
    vaz = 1
    dicl = list()
    dic = {1:'+',2:'|',3:'|'}
    while x[n] != '!?':
        if x[n] == '':
            dic[1] += '_'*3
            wer += 3
        else:
            rty = len(x[n])+1
            dic[1] += '_'*(rty)
            wer += rty
        n += 1
    n = 2
    for q in x :
        if q != '!?':
            if q == '':
                dic[n] += ('   ')
                dic[n+1] += ('   ')
                vaz = 0
            else:
                if vaz == 0:
                    dic[n] += '|'
                    dic[n+1] += '|'
                dic[n] += (q+'|')
                dic[n+1] += (('-'*2)+'|')
                vaz = 1
        else:
            n += 2
            dic[n] = '|'
            dic[n+1] = '|'
    qwe = 0
    for q in x:
        if q == '!?':
            qwe += 2
    for q in range(1,int((len(dic)-1)/2)):
        r = (q*2) + 1
        #dic[r] += '-'
        if len (dic.get(r-1,100000)) < len (dic.get(r+1,0)):
            dic[r] = dic.get(r) + ('_' * int(len (dic.get(r+1,0)) - len (dic.get(r-1,100000)))) 
    dic[1] += '+'
    for q1 in range(0,qwe):
        q = list(dic.keys()) [q1]
        dicl.append(dic[q])
    dicl.append('+' + str('_'*(wer))+'+')
    dicl[len(dicl)-2] = dicl[len(dicl)-2] [:len(dicl[len(dicl)-2])] + '|'
    print ('\n'.join(dicl))








def print_l (x):
    lis = list()
    
    m = 0
    for t in x :
        if len(t) > m:
            m = len(t)
    lis.append('_'*(m+2))
    for t in x:
        if( m - len(t)) > 0 :
            if ( m - len(t))%2 == 0:
                zzz = str(' '*int( (m - len(t))/2))
                
                lis.append('|' + zzz + str(t) + zzz + '|')
            else :
                
                zzz = str(' '*int( (m - len(t))/2))
                lis.append('| ' + zzz + t + zzz + '|') 
        else:
            lis.append('|'+t+'|')
    lis.append('#'*(m+2))
    q = '\n'.join(lis)
    print(q)




def print_all ():
    w = list()
    for t in ac :
        for tt in range(1,19) :
            #tt = list(t.keys()) [t1]
            qqq = t.get(tt,'')
            if qqq != '':
                aaq = qqq[1]
            else :
                aaq = ''
            if len(aaq) == 1:
                aaq += ' '

            w.append (aaq)
        w.append('!?')
    print_j(w)
        
        













H = [1,'H']
He = [2,'He']
Li = [3,'Li']
Be = [4,'Be']
B = [5,'B']
C = [6,'C']
N = [7,'N']
O = [8,'O']
F = [9,'F']
Ne = [10,'Ne']
Na = [11,'Na']
Mg = [12,'Mg']
Al = [13,'Al']
Si = [14,'Si']
P = [15,'P']
S = [16,'S']
Cl = [17,'Cl']
Ar = [18,'Ar']
K = [19,'K']
Ca = [20,'Ca']
Ga = [31,'Ga']
Ge = [32,'Ge']
As = [33,'As']
Se = [34,'Se']
Br = [35,'Br']
Kr = [36,'Kr']
Rb = [37,'Rb']
Sr = [38,'Sr']
In = [49,'In']
Sn = [50,'Sn']
Sb = [51,'Sb']
Te = [52,'Te']
I = [53,'I']
Xe = [54,'Xe']
Cs = [55,'Cs']
Ba = [56,'Ba']
Tl = [81,'Tl']
Pb = [82,'Pb']
Bi = [83,'Bi']
Po = [84,'Po']
At = [85,'At']
Rn = [86,'Rn']
Fr = [87,'Fr']
Ra = [88,'Ra']
Ni = [28,'Ni']
Cu = [29,'Cu']
Zn = [30,'Zn']
Cd = [48,'Cd']
Ag = [47,'Ag']
Au = [79,'Au']
Pd = [46,'Pd']
Pt = [78,'Pt']
Hg = [80,'Hg']























all1 = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Ga','Ge','As','Se','Br','Kr','Rb','Sr','In','Sn','Sb','Te','I','Xe','Cs','Ba','Tl','Pb','Bi','Po','At','Rn','Fr'88,'Ra'28,'Ni'29,'Cu','Zn','Cd','Ag','Au','Pd','Pt','Hg']

dic = {1:H,2:He,3:Li,4:Be,5:B,6:C,7:N,8:O,9:F,10:Ne,11:Na,12:Mg,13:Al,14:Si,15:P,16:S,17:Cl,18:Ar,19:K,20:Ca,28:Ni,29:Cu,30:Zn,31:Ga,32:Ge,33:As,34:Se,35:Br,36:Kr,37:Rb,38:Sr,46:Pd,47:Ag,48:Cd,49:In,50:Sn,51:Sb,52:Te,53:I,54:Xe,55:Cs,56:Ba,78:Pt,79:Au,80:Hg,81:Tl,82:Pb,83:Bi,84:Po,85:At,86:Rn,87:Fr,88:Ra}

dicq = dict()

for q in dic :


ac = [{1:H,18:He},{1:Li,2:Be,13:B,14:C,15:N,16:O,17:F,18:Ne},{1:Na,2:Mg,13:Al,14:Si,15:P,16:S,17:Cl,18:Ar},{1:K,2:Ca,10:Ni,11:Cu,12:Zn,13:Ga,14:Ge,15:As,16:Se,17:Br,18:Kr},{1:Rb,2:Sr,10:Pd,11:Ag,12:Cd,13:In,14:Sn,15:Sb,16:Te,17:I,18:Xe},{1:Cs,2:Ba,10:Pt,11:Au,12:Hg,13:Tl,14:Pb,15:Bi,16:Po,17:At,18:Rn},{1:Fr,2:Ra}]











code = "\n\n\n   &> "
print_all()
in2 = input(code)
while in2 !='exit':
    if in2[0] == 'p':
        q2 = in2[2:]
        if q2 == 'tan':
            print_all()
        elif q2 in all1 :
            print_l ()




    in2 = input(code)






