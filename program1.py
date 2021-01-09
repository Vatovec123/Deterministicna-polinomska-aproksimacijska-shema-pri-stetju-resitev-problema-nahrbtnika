import math
import random
import sys
import time
import xlsxwriter
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

    #vsota = sum(teze)
    #if vsota <= C:
    #    return 2 ** n
    
    Q = (1 + (epsilon / (n + 1)))
    s = math.ceil(n * math.log(2,Q))
    T = [[0 for stvari in range(s+1)] for row in range(n+1)]
    #print (n ,s)
    for j in range(1,s+1):
        T[0][j] = float('inf')
    #print(T)
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
            #print(vrednosti) 
    #print(T)
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



#def glavno():
#
#  
#    global resitve
#
#    teze = seznam_tez()
#    C = random.randint(0, 10000)
#    
#    for epsilon in [0.9,0.1, 0.01, 0.0001]:
#        res = resitve(teze, C, epsilon)
#        print(C)
#        print(teze)
#        print(res)

  
#glavno()    

#print(seznam_tez())


#def teze(st, max_teza):
#    randomlist = random.sample(range(1, max_teza), st)
#    return randomlist


#print(teze(5,10))
#print(teze(11,10))

def teze(st, max_teza):
    randomlist = []
    for i in range(0, st):
        n = random.randint(1,max_teza)
        randomlist.append(n)
    return randomlist

#print(teze(11,10))

def generiraj(st, max_teza):
    global seznam, C 

    seznam = teze(st, max_teza)
    vsota = sum(seznam)
    C = random.randint(0, vsota + 1)
    
    #print(C)
    #print(seznam)

#-------------------------Eksperimentalni del----------

#------------------- 1. Primerjava hitrosti pri različnih epsilonih--------------------- 

#-----------------------------------------------------------------------------
#Poskusi na 5 točkah:
# Max teža naj bo 50:

časi = []
rezultati = []
for i in range(10):
    generiraj(5,50)


    tabela_časov = []
    tabela_rezultatov = []
    for epsilon in [0.1 , 0.3, 0.5, 0.7, 0.9]:
        start_time = time.time()
        res = resitve(seznam, C, epsilon)
        #print('Število rešitev je {}'.format(res))
        elapsed_time = time.time() - start_time
        #print('Čas računanja je {}'.format(elapsed_time))
        tabela_časov.append(elapsed_time)
        tabela_rezultatov.append(res)
    print(tabela_časov)
    print(tabela_rezultatov)#

    časi.append(tabela_časov)
    rezultati.append(tabela_rezultatov)


    with xlsxwriter.Workbook('časi.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        for row_num, data in enumerate(časi):
            worksheet.write_row(row_num, 0, data)
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#Poskusi na 10 točkah:
# Max teža naj bo 50:

#časi = []
#rezultati = []
#for i in range(10):
#    generiraj(10,50)
#
#
 #   tabela_časov = []
 #   tabela_rezultatov = []
 #   for epsilon in [0.1 , 0.3, 0.5, 0.7, 0.9]:
 #       start_time = time.time()
 #       res = resitve(seznam, C, epsilon)
 #       #print('Število rešitev je {}'.format(res))
 #       elapsed_time = time.time() - start_time
 #       #print('Čas računanja je {}'.format(elapsed_time))
 #       tabela_časov.append(elapsed_time)
 #       tabela_rezultatov.append(res)
 #   print(tabela_časov)
 #   print(tabela_rezultatov)

  #  časi.append(tabela_časov)
  #  rezultati.append(tabela_rezultatov)


   # with xlsxwriter.Workbook('časi.xlsx') as workbook:
    #    worksheet = workbook.add_worksheet()

    #    for row_num, data in enumerate(časi):
     #       worksheet.write_row(row_num, 0, data)
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#Poskusi na 20 točkah:
# Max teža naj bo 50:

#časi = []
#rezultati = []
#for i in range(10):
#    generiraj(20,50)


 #   tabela_časov = []
 #   tabela_rezultatov = []
 #   for epsilon in [0.5, 0.7, 0.9]:
 ##       start_time = time.time()
  #      res = resitve(seznam, C, epsilon)
  #      #print('Število rešitev je {}'.format(res))
 #       elapsed_time = time.time() - start_time
        #print('Čas računanja je {}'.format(elapsed_time))
 #       tabela_časov.append(elapsed_time)
 #       tabela_rezultatov.append(res)
 #   print(tabela_časov)
 #   print(tabela_rezultatov)

 #   časi.append(tabela_časov)
  #  rezultati.append(tabela_rezultatov)


 #   with xlsxwriter.Workbook('časi.xlsx') as workbook:
 #       worksheet = workbook.add_worksheet()
#
#        for row_num, data in enumerate(časi):
#            worksheet.write_row(row_num, 0, data)
#-----------------------------------------------------------------------------




#---------------2.primerjava natančnosti pri različnih primerih za posebne primere, kadar je vsota tež manjša od kapaciteta, saj lahko 
#izračunamo točno vrednost zelo preprosto

def generiraj_poseben(st, max_teza):
    global seznam, C , vsota

    seznam = teze(st, max_teza)
    vsota = sum(seznam)
    C = random.randint(vsota + 1, vsota + 1000)


#-----------------------------------------------------------------------------

#Poskusi na 5 točkah:
# Max teža naj bo 50:

#časi = []
#rezultati = []
#for i in range(10):
#    generiraj_poseben(5,50)
#    tocna_resitev = 2 ** 5
#
#
 #   tabela_časov = []
 #   tabela_rezultatov = []
 #   for epsilon in [0.1 , 0.3, 0.5, 0.7, 0.9]:
 #       start_time = time.time()
 #       res = resitve(seznam, C, epsilon)
 #       razlika_do_tocne_resitve = abs(res - tocna_resitev)


        #print('Število rešitev je {}'.format(razlika_do_tocne_resitve))
 #       elapsed_time = time.time() - start_time
        #print('Čas računanja je {}'.format(elapsed_time))
#        tabela_časov.append(elapsed_time)
#        tabela_rezultatov.append(razlika_do_tocne_resitve)
#    print(tabela_časov)
#    print(tabela_rezultatov)

 #   časi.append(tabela_časov)
#    rezultati.append(tabela_rezultatov)


  #  with xlsxwriter.Workbook('rezultati.xlsx') as workbook:
   #     worksheet = workbook.add_worksheet()
#
  #      for row_num, data in enumerate(rezultati):
 #           worksheet.write_row(row_num, 0, data)
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#Poskusi na 10 točkah:
# Max teža naj bo 50:

#časi = []
#rezultati = []
#for i in range(10):
#    generiraj_poseben(10,50)
#    tocna_resitev = 2 ** 10
#
 #   tabela_časov = []
 #   tabela_rezultatov = []
 #   for epsilon in [0.1 , 0.3, 0.5, 0.7, 0.9]:
 #       start_time = time.time()
  #      res = resitve(seznam, C, epsilon)
  #      razlika_do_tocne_resitve = abs(res - tocna_resitev)


        #print('Število rešitev je {}'.format(razlika_do_tocne_resitve))
#        elapsed_time = time.time() - start_time
        #print('Čas računanja je {}'.format(elapsed_time))
 #       tabela_časov.append(elapsed_time)
 #       tabela_rezultatov.append(razlika_do_tocne_resitve)
 #   print(tabela_časov)
 #  print(tabela_rezultatov)

 #   časi.append(tabela_časov)
  #  rezultati.append(tabela_rezultatov)
#

#    with xlsxwriter.Workbook('rezultati.xlsx') as workbook:
#        worksheet = workbook.add_worksheet()#

#        for row_num, data in enumerate(rezultati):
 #           worksheet.write_row(row_num, 0, data)



#cas =[[68.39487767219543, 7.1797521114349365, 2.569284439086914, 1.3450424671173096, 0.846217155456543],[67.25358986854553, 6.960428953170776, 2.492492914199829, 1.3788478374481201, 0.8157694339752197],[64.79443216323853, 6.9264326095581055, 2.5935420989990234, 2.4234719276428223, 1.0827598571777344],[64.32608032226562, 7.469868898391724, 2.5722100734710693, 1.329301118850708, 0.8441579341888428],[69.53349113464355, 9.105249404907227, 2.629148244857788, 1.3267595767974854, 0.8190691471099854],[73.47720217704773, 8.119654417037964, 2.565199613571167, 1.352660894393921, 0.8967170715332031],[68.35693597793579, 7.355787992477417, 2.3838305473327637, 1.6605503559112549, 1.167146921157837],[69.35537672042847, 7.02304744720459, 2.7127227783203125, 1.34928560256958, 0.8731367588043213],[64.03194761276245, 8.101060628890991, 2.559208631515503, 1.3685736656188965, 0.8225433826446533],[65.00785851478577, 7.4847986698150635, 2.6315255165100098, 1.4687998294830322, 0.8352563381195068]]


#with xlsxwriter.Workbook('časi.xlsx') as workbook:
#        worksheet = workbook.add_worksheet()
#
#        for row_num, data in enumerate(cas):
 #           worksheet.write_row(row_num, 0, data)

 #-----------------------------------------------------------------------------