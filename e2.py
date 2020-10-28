


n = lambda x: print ('\n'*x)

iton = lambda x : dic[int(x)] [4]
itos = lambda x : dic[int(x)] [1]
stoi = lambda x : dicq[str(x)]
ston = lambda x : dic[dicq[str(x)]][4]











def b_list(x,y):
    for q in x:
        y.append(q)












def randlist(x):
    from random import randint
    y = x
    z = list()
    for q in range(0,len(x)):
        im = randint (0,len(y)-1)
        z.append (y[im])
        del (y[im])
    return z











def list_get (lis,x,y):
    if len(lis) > x :
        return  lis[x]
    else:
        return  y














def print_j(x,m):
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
    if m == 'r':
        return ('\n'.join(dicl))
    print ('\n'.join(dicl))














def print_l (a):
    lis = list()
    x = list()
    for q in a:
        x.append(str(q))
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
    return(lis)












def q_name(m):
    from time import sleep



    t = list()

    print ('name exam:')
    if m == 'f':
        qwer = list()
        b_list(dici,qwer)
        x = randlist(qwer)
        for q in x:
            b = 0
            n(1)

            print ('|   ' + dic[int(q)][int(4)] + ':')
            print ('_'*len(dic[int(q)][int(4)]))
            print ('|   insert '+'It'+"'"+'s number.')

            j = input ('       ?^>> ')
            
            if j == 'exit' or j == 'back':
                t = []
                break
            if j == str(dic[int(q)][0]):
                print (ok)
            else:
                print (ooh)
                n(2)
                b = 1
            
            print ('|   insert '+'It'+"'"+'s symbol.')
            j = input ('       ?^>> ')
            
            if j == 'exit' or j == 'back':
                t = []
                break
            
            if j == dic[int(q)][1]:
                print (ok)
            else :
                print (ooh)
                b = 1
            
            if b == 1:
                print_une(dic[int(q)][1])
                t.append(q)
                if input('are you ok?') == 'no':
                    n(3)
                    sleep (1)
                    n(3)
                    print ("Not important")
                    
                    n(3)

                    sleep (2)

                    
            else :
                print (ook)

        if t == []:
            print(oook)


        tt = list()

        while t != [] :

            for q1 in range(0,len(t)):
                q = t[q1]
                b = 0
                n(1)

                print ('|   ' + dic[int(q)][int(4)] + ':')
                print ('_'*len(dic[int(q)][int(4)]))
                print ('|   insert '+'It'+"'"+'s number.')

                j = input ('       ?^>> ')
            
                if j == 'exit' or j == 'back':
                    t = []
                    break
                if j == str(dic[int(q)][0]):
                    print (ok)
                else:
                    print (ooh)
                    n(2)
                    b = 1
            
                print ('|   insert '+'It'+"'"+'s symbol.')
                j = input ('       ?^>> ')
            
                if j == 'exit' or j == 'back':
                    t = []
                    break
            
                if j == dic[int(q)][1]:
                    print (ok)
                else :
                    print (ooh)
                    b = 1
            
                if b == 1:
                    print_une(dic[int(q)][1])
                    tt.append(q)
                    if input('are you ok?') == 'no':
                        n(3)
                        sleep (1)
                        n(3)
                        print ("Not important")
                    
                        n(3)

                        sleep (2)

                    
                else :
                    print (ook)

            t = []
            
            for q2 in tt :
                t.append(q2)
            if t == []:
                print(oook)

                
              
            





















def q_number(m):
    from time import sleep

    

    t = list()
    
    
    print ('number exam:')
    if m == 'f':
        vv = 1
        qwer = list()
        b_list(dici,qwer)
        x = randlist(qwer)
        

        for q in x:

            examer = q
            #aj = iton(examer)
            jas = itos(examer)


            b = 0
            n(1)

            print ('|   ' + examer + ':')
            print ('_'*len('|   insert ' + 'It'+"'"+'s name.'))
            #print ('|   insert ' + 'It'+"'"+'s name.')

            #j = input ('       ?^>> ')
            
            #if j == 'exit' or j == 'back':
            #    t = []
            #    break
            #if j == aj:
            #    print (ok)
            #else:
            #    print (ooh)
            #    n(2)
            #    b = 1
            
            print ('|   insert '+'It'+"'"+'s sambol.')
            j = input ('       ?^>> ')
            
            if j == 'exit' or j == 'back':
                vv = 0
                t = []
                break
            
            if j == jas:
                print (ok)
            else :
                print (ooh)
                b = 1
            
            if b == 1:
                print_une(jas)
                t.append(q)
                if input('are you ok?') == 'no':
                    n(3)
                    sleep (1)
                    n(3)
                    print ("Not important")
                    
                    n(3)

                    sleep (2)

                    
            else :
                print (ook)

        if t == [] and vv == 1 :
            print(oook)


        tt = list()

        while t != [] :



            

            for q1 in range(0,len(t)):

                examer = q
                aj = iton(examer)
                jas = itos(examer)




                q = t[q1]
                b = 0
                n(1)

                print ('|   ' + examer + ':')
                print ('_'*len(examer))
                #print ('|   insert '+'It'+"'"+'s name.')

                #j = input ('       ?^>> ')
            
                #if j == 'exit' or j == 'back':
                #    vv = 0
                #    t = []
                #    break
                #if j == aj :
                #    print (ok)
                #else:
                #    print (ooh)
                #    n(2)
                #    b = 1
            
                print ('|   insert '+'It'+"'"+'s sambol.')
                j = input ('       ?^>> ')
            
                if j == 'exit' or j == 'back':
                    vv = 0
                    t = []
                    break
            
                if j == jas :
                    print (ok)
                else :
                    print (ooh)
                    b = 1
            
                if b == 1:
                    print_une(jas)
                    tt.append(q)
                    if input('are you ok?') == 'no':
                        n(3)
                        sleep (1)
                        n(3)
                        print ("Not important")
                    
                        n(3)

                        sleep (2)

                    
                else :
                    print (ook)

            t = []
            
            for q2 in tt :
                t.append(q2)

        
            if t == [] and vv == 1:
                print(oook)
















def q_sambol(m):
    from time import sleep

    

    t = list()
    
    
    print ('symbol exam:')
    if m == 'f':
        
        vv = 1

        qwer = list()
        b_list(dici,qwer)
        x = randlist(qwer)
        

        for q in x:

            examer = itos(q)
            #aj = ston(examer)
            jas = str(stoi(examer))


            b = 0
            n(1)

            print ('|   ' + examer + ':')
            print ('_'*len(examer))
            #print ('|   insert ' + 'It'+"'"+'s name.')

            #j = input ('       ?^>> ')
            
            #if j == 'exit' or j == 'back':
            #    t = []
            #    break
            #if j == aj:
            #    print (ok)
            #else:
            #    print (ooh)
            #    n(2)
            #    b = 1
            
            print ('|   insert '+'It'+"'"+'s number.')
            j = input ('       ?^>> ')
            
            if j == 'exit' or j == 'back':
                t = []
                vv = 0
                break
            
            if j == jas:
                print (ok)
            else :
                print (ooh)
                b = 1
            
            if b == 1:
                print_une(itos(jas))
                t.append(q)
                if input('are you ok?') == 'no':
                    n(3)
                    sleep (1)
                    n(3)
                    print ("Not important")
                    
                    n(3)

                    sleep (2)

                    
            else :
                print (ook)

        if t == [] and vv == 1:
            print(oook)


        tt = list()

        while t != [] :





            for q1 in range(0,len(t)):

                examer = itos(q)
                #aj = ston(examer)
                jas = str(stoi(examer))




                q = t[q1]
                b = 0
                n(1)

                print ('|   ' + examer + ':')
                print ('_'*len('|   insert '+'It'+"'"+'s number.'))
                #print ('|   insert '+'It'+"'"+'s name.')

                #j = input ('       ?^>> ')
            
               # if j == 'exit' or j == 'back':
                #    t = []
                #    break
                #if j == aj :
                #    print (ok)
                #else:
                #    print (ooh)
                #    n(2)
               #     b = 1
            
                print ('|   insert '+'It'+"'"+'s number.')
                j = input ('       ?^>> ')
            
                if j == 'exit' or j == 'back':
                    vv = 0
                    t = []
                    break
            
                if j == jas :
                    print (ok)
                else :
                    print (ooh)
                    b = 1
            
                if b == 1:
                    print_une(itos(jas))
                    tt.append(q)
                    if input('are you ok?') == 'no':
                        n(3)
                        sleep (1)
                        n(3)
                        print ("Not important")
                    
                        n(3)

                        sleep (2)

                    
                else :
                    print (ook)

            t = []
            
            for q2 in tt :
                t.append(q2)

            if vv == 1 and t == []:
                print(oook)













def quese(ms):
    
    for m in ms:
        if m[0] == 'f':
            if m[1:] == 'na':
                q_name('f')
            elif m[1:] == 'nu':
                q_number('f')
            elif m[1:] == 'sy':
                q_sambol('f')
        elif m[0] == 'm':
            if m[1:] == 'na':
                q_name('m')
            elif m[1:] == 'nu':
                q_number('m')
            elif m[1:] == 'sy':
                q_sambol('m')
        
















def print_all (m):
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
    if m == 'r':
        return print_j(w,m)
    print_j(w,m)
        








        
def print_une (x):
    a = int()
    b = int()
    c = int()
    lis = ['',''] + print_l ([x , dicq[x]])

    if list_get(dic[dicq[x]],5,'') == '':
        a = 3
        b = 4
        c = 0
    else:
        a = 3
        b = 4
        c = 0
        




    lis[5] += '    ' + list_get(dic[dicq[x]],5,'') 
    
    lis[a] += ("    tanavob = %i" % (dic[dicq[x]] [2] [0]))
    
    lis[b] += ("    gorop = %i" % (dic[dicq[x]] [2] [1])) 
    
    lis[a] += '    ' + (dic[dicq[x]][3]) 
    
    lis[c] += (dic[dicq[x]][4]) + ':' 
    
    lis[4].split()






    wwwe = len(lis[3])+1
    lis[1] += ('_'*(wwwe)) + '.'
    

   
    for q in range(2,len(lis)):
        lis[q] += (' '* (wwwe-len(lis[q]))) + '|'
    


    lis.append(("_"*wwwe) + '|' )
    


    print ('\n\n'+('\n'.join(lis)))



def err (x):
    print_all('')
    print(' <%s>   ??????' % x)


























































H = [1,'H',[1,1],'Gas','Hydrogen']
He = [2,'He',[1,18],'Gas','Helium']
Li = [3,'Li',[2,1],'Solid','Lithium']
Be = [4,'Be',[2,2],'Solid','Beryllium']
B = [5,'B',[2,13],'Solid','Boron']
C = [6,'C',[2,14],'ُSolid','Carbon']
N = [7,'N',[2,15],'Gas','Nitrogen']
O = [8,'O',[2,16],'Gas','Oxygen']
F = [9,'F',[2,17],'Gas','Fluorine']
Ne = [10,'Ne',[2,18],'Gas','Neon']
Na = [11,'Na',[3,1],'Solid','Sodium']
Mg = [12,'Mg',[3,2],'Solid','Magnesium']
Al = [13,'Al',[3,13],'Solid','Aluminum']
Si = [14,'Si',[3,14],'Solid','Silicon']
P = [15,'P',[3,15],'ُSolid','Phosphorus']
S = [16,'S',[3,16],'Solid','Sulfur']
Cl = [17,'Cl',[3,17],'Solid','Chlorine']
Ar = [18,'Ar',[3,18],'Gas','Argon']
K = [19,'K',[4,1],'Solid','Potassium']
Ca = [20,'Ca',[4,2],'Solid','Calcium']
Ga = [31,'Ga',[4,13],'Solid','Gallium']
Ge = [32,'Ge',[4,14],'Solid','Germanium']
As = [33,'As',[4,15],'Solid','Arsenic']
Se = [34,'Se',[4,16],'Solid','Selenium']
Br = [35,'Br',[4,17],'Liquid','Barium']
Kr = [36,'Kr',[4,18],'Gas','Krypton']
Rb = [37,'Rb',[5,1],'Solid','Rubidium']
Sr = [38,'Sr',[5,2],'Solid','Strontium']
In = [49,'In',[5,13],'Solid','Indium']
Sn = [50,'Sn',[5,14],'Solid','Tin']
Sb = [51,'Sb',[5,15],'Solid','Antimony']
Te = [52,'Te',[5,16],'Solid','Tellurium']
I = [53,'I',[5,17],'Solid','Iodine']
Xe = [54,'Xe',[5,18],'Gas','Xenon','radio active !!!!!']
Cs = [55,'Cs',[6,1],'Solid','Cesium']
Ba = [56,'Ba',[6,2],'Solid','Barium']
Tl = [81,'Tl',[6,13],'Solid','Thallium']
Pb = [82,'Pb',[6,14],'Solid','Lead']
Bi = [83,'Bi',[6,15],'Solid','Bismuth','radio active !!!!!']
Po = [84,'Po',[6,16],'Solid','Polonium','radio active !!!!!']
At = [85,'At',[6,17],'Solid','Astatine','radio active !!!!!']
Rn = [86,'Rn',[6,18],'Gas','Radon','radio active !!!!!']
Fr = [87,'Fr',[7,1],'Liquid','Francium','radio active !!!!!']
Ra = [88,'Ra',[7,2],'Solid','Radium','radio active !!!!!']
Ni = [28,'Ni',[4,10],'Solid','Nickel']
Cu = [29,'Cu',[4,11],'Solid','Copper']
Zn = [30,'Zn',[4,12],'Solid','Zinc']
Cd = [48,'Cd',[5,10],'Solid','Cadmium']
Ag = [47,'Ag',[5,11],'Solid','Silver']
Au = [79,'Au',[5,12],'Solid','Gold']
Pd = [46,'Pd',[6,10],'Solid','Palladium']
Pt = [78,'Pt',[6,11],'Solid','Platinum']
Hg = [80,'Hg',[6,12],'Liquid','Mercury']




ok = '''


                   /
                  /
                \/



                
'''


ook = '''                       

                           ______                _________
                |\   |     |           \   /         |
                | \  |     |_____       \ /          | 
                |  \ |     |            / \          |
                |   \|     |_____      /   \         |



'''



ooh = '''
                
                 \  /
                  \/
                  /\ 
                 /  \ 
'''



oook = '''

            __                      
           |  |    | /    __        __    ---|--- 
           |__|    |/    /  \       __\      |
              |    |     \__/      /  |      |  
            __/    |      \__      \__|      |
                                  


'''          






all1 = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Ga','Ge','As','Se','Br','Kr','Rb','Sr','In','Sn','Sb','Te','I','Xe','Cs','Ba','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ni','Cu','Zn','Cd','Ag','Au','Pd','Pt','Hg']

dic = {1:H,2:He,3:Li,4:Be,5:B,6:C,7:N,8:O,9:F,10:Ne,11:Na,12:Mg,13:Al,14:Si,15:P,16:S,17:Cl,18:Ar,19:K,20:Ca,28:Ni,29:Cu,30:Zn,31:Ga,32:Ge,33:As,34:Se,35:Br,36:Kr,37:Rb,38:Sr,46:Pd,47:Ag,48:Cd,49:In,50:Sn,51:Sb,52:Te,53:I,54:Xe,55:Cs,56:Ba,78:Pt,79:Au,80:Hg,81:Tl,82:Pb,83:Bi,84:Po,85:At,86:Rn,87:Fr,88:Ra}

dicq = dict()
dici = list()
dicn = list()

for q in dic :
    dicq[dic[q][1]] = dic[q][0]

for q in all1 :
    dici.append(str(dicq[q]))

for q in all1 :
    dicn.append(dic[dicq[q]][4])



ac = [{1:H,18:He},{1:Li,2:Be,13:B,14:C,15:N,16:O,17:F,18:Ne},{1:Na,2:Mg,13:Al,14:Si,15:P,16:S,17:Cl,18:Ar},{1:K,2:Ca,10:Ni,11:Cu,12:Zn,13:Ga,14:Ge,15:As,16:Se,17:Br,18:Kr},{1:Rb,2:Sr,10:Pd,11:Ag,12:Cd,13:In,14:Sn,15:Sb,16:Te,17:I,18:Xe},{1:Cs,2:Ba,10:Pt,11:Au,12:Hg,13:Tl,14:Pb,15:Bi,16:Po,17:At,18:Rn},{1:Fr,2:Ra}]














































code = "\n\n\n   &>  "
print_all('')
in2 = input(code)
while in2 != "exit" and in2 != "quit" :
    if in2 != '' and  in2[0] == 'p':
        if len (in2) == 1:
            q2 = input('mode:'+"  ^>> ")
        else:
            q2 = in2[2:]
        if q2 == 'tan':
            print_all('')
        elif q2 in all1 :
            print_une (q2)
        elif q2 in dici :
            print_une (dic[int(q2)][1])
        else:
            err ('p.%s' %q2)
    elif  in2 == 'q' or in2 == 'quese' :
        sssq = 1

        rrr = input ('mode:'+"  ^>> ").split()
        for rq in rrr :
            if not (rq in ['fna','fnu','fsy','mna','mnu','msy']):
                err('quese.%s' %rrr)
                sssq = 0
                break
        if sssq == 1 :
            quese (rrr)
    elif in2 in all1 :
        print_une (in2)
    elif in2 == 'tan':
        print_all('')
    elif in2 in dici :
        print_une (dic[int(in2)][1])
    else:
        err(in2)        

    in2 = input(code)
    code = "\n\n\n   &>  "
    




