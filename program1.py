import math
import random
import sys

#def odstrani(teze,C):
##    nove = []
#    for i in teze:
##        if i <= C:
#            nove.append(i)
#        else:
#            pass
#    teze = nove    
#    print(teze) 

def seznam_tez():
    n = random.randint(1, 20)
    randomlist = random.sample(range(1, 500), n)
    return randomlist



def odstrani(teze,C):
    teze = [x for x in teze if x <= C]
    print(teze)



def resitve(teze,C, epsilon):
    teze = [x for x in teze if x <=C]
    n = len(teze)

    vsota = sum(teze)
    if vsota <= C:
        return 2 ** n
    
    Q = (1 + (epsilon / (n + 1)))
    s = math.ceil(n * math.log(2,Q))
    T = [[0 for stvari in range(s+1)] for row in range(n+1)]
    print (n ,s)
    for j in range(1,s+1):
        T[0][j] = float('inf')
    print(T)
    for i in range(1,n+1):
        for j in range(s+1):
            vrednosti = []
            for k in range(j,-1,-1):
                alpha1 = Q **(-k) 
                if math.floor(j + math.log(alpha1,Q)) < 0:
                    prva1 = 0
                else:
                    prva1 = T[i-1][math.floor(j + math.log(alpha1,Q))]
                if 1- alpha1 !=0:
                    if math.floor(j + math.log(1-alpha1,Q)) < 0:
                        druga1 = 0 + teze[i-1]
                if 1-alpha1 == 0:
                    druga1 = 0 + teze[i-1]
                elif math.floor(j + math.log(1-alpha1,Q)) > 0:
                     druga1 = T[i-1][math.floor(j + math.log(1-alpha1,Q))] + teze[i-1]
                vrednosti.append(max(prva1,druga1))
                
                alpha2 = 1-(Q ** (-k))
                if math.floor(j + math.log(1-alpha2,Q)) < 0:
                    druga2 = 0 + teze[i-1]
                else:
                    druga2 = T[i-1][math.floor(j + math.log(1-alpha2,Q))] + teze[i-1]
                if alpha2 !=0:
                    if math.floor(j + math.log(alpha2,Q)) < 0:
                        prva2 = 0 
                if alpha2 == 0:
                    prva2 = 0 
                elif math.floor(j + math.log(alpha2,Q)) > 0:
                     prva2 = T[i-1][math.floor(j + math.log(alpha2,Q))] 
                vrednosti.append(max(prva2,druga2))
            T[i][j] = min(vrednosti)    
            print(vrednosti) 
    print(T)
    mozni_j_crta = []   
    for j in range(s+1):
        if T[n][j] <= C:
            mozni_j_crta.append(j) 
    if mozni_j_crta == []:
        return 1 #ne daš nič v nahrbntik     
    j_crta = mozni_j_crta[-1]                
    resitev = Q ** (j_crta + 1)
    return resitev

    
#print(resitve([73, 3, 56, 2, 79, 6, 43, 51, 45, 13, 4, 58, 36, 87, 63, 63, 95, 59, 75, 76],1000,0.2))



def glavno():

  
    global resitve

    teze = seznam_tez()
    C = random.randint(0, 10000)
    
    for epsilon in [0.9,0.1, 0.01, 0.0001]:
        res = resitve(teze, C, epsilon)
        print(C)
        print(teze)
        print(res)

  
glavno()    

