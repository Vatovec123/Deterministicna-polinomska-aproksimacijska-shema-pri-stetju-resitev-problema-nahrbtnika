import math
import random



def resitve(teze,C, epsilon):
    global n,Q,s
    n = len(teze)
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
        else:
            pass 
    if mozni_j_crta == []:
        return 1 #ne daš nič v nahrbntik     
    j_crta = mozni_j_crta[-1]                
    resitev = Q ** (j_crta + 1)
    return resitev

    
print(resitve([2,3,6],10,0.1))

