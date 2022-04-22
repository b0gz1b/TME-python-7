#======================================================================#
# UE Calculabilite L3                                                  #
# TME Machines de Turing : Machines de Turing deterministes a k bandes #
# Mathieu.Jaume@lip6.fr                                                #
#======================================================================#

from Turing_compos import *
        
# Machine de Turing deterministe a k bandes
#
# M = (d,q0,qok,qko)
#
# d = [((q,(a1,...,an)),(q',(a'1,...,a'n),(m1,...,mn))),...]
#
# bandes : L = [L1,...,Ln]
#

# Affichage d'une configuration pour une machine de Turing a k bandes
#--------------------------------------------------------------------

def print_config_k(L,T,q,qok,qko,k):
    for i in range(k):
        print_config_1(L[i],T[i],q,qok,qko)


def exec_MT_k(M,k,L,T):
    # M : machine de Turing deterministe a k bandes
    # k : nombre de bandes
    # L : liste des representations des bandes initiales
    # T : positions initiales des k tetes de lecture
    d,q0,qok,qko = M
    q = q0
    while True:
        print_config_k(L,T,q,qok,qko,k)
        A = assoc_f(d,(q,tuple([L[i][T[i]] for i in range(len(T))])))
        print(T)
        if A != None:
            q, nS, M = A
            for i in range(k):
                bande_courante = L[i]
                bande_courante[T[i]] = nS[i]
                if M[i] == "R":
                    T[i] += 1
                    if T[i] >= len(bande_courante):
                        bande_courante.append("Z")
                elif M[i] == "L":
                    T[i] -= 1
                    if T[i] < 0:
                        T[i] = 0
                        bande_courante.insert(0,"Z")
        else:
            break
    return (q == qok,T,L)

# mots sur {a,b} contenant autant de a que de b
#

d2_ex1 = [((0,("a","Z")),(1,("a","X"),("R","R"))),\
          ((0,("b","Z")),(2,("b","X"),("R","R"))),\
          ((0,("Z","Z")),(3,("Z","Z"),("S","S"))),\
          ((1,("a","X")),(1,("a","X"),("R","R"))),\
          ((1,("a","Z")),(1,("a","Z"),("R","R"))),\
          ((1,("b","Z")),(1,("b","Z"),("R","L"))),\
          ((1,("b","X")),(2,("b","X"),("R","R"))),\
          ((1,("Z","X")),(3,("Z","X"),("S","S"))),\
          ((2,("a","X")),(1,("a","X"),("R","R"))),\
          ((2,("a","Z")),(2,("a","Z"),("R","L"))),\
          ((2,("b","Z")),(2,("b","Z"),("R","R"))),\
          ((2,("b","X")),(2,("b","X"),("R","R"))),\
          ((2,("Z","X")),(3,("Z","X"),("S","S")))]


M2_ex1 = (d2_ex1,0,3,4)


d2_palin_bin = [((0,("0","Z")),(0,("0","0"),("R","R"))),\
                ((0,("1","Z")),(0,("1","1"),("R","R"))),\
                ((0,("Z","Z")),(1,("Z","Z"),("L","S"))),\
                ((1,("0","Z")),(1,("0","Z"),("L","S"))),\
                ((1,("1","Z")),(1,("1","Z"),("L","S"))),\
                ((1,("Z","Z")),(2,("Z","Z"),("R","L"))),\
                ((2,("0","0")),(2,("0","0"),("R","L"))),\
                ((2,("1","1")),(2,("1","1"),("R","L"))),\
                ((2,("Z","Z")),(3,("Z","Z"),("S","S")))]
                
M2_palin_bin = (d2_palin_bin,0,3,4)


d2_un_to_bin = [((0,("$","Z")),(1,("$","$"),("R","R"))),\
                ((1,("I","Z")),(1,("I","1"),("R","S"))),\
                ((1,("I","0")),(2,("I","0"),("S","R"))),\
                ((1,("I","1")),(2,("I","1"),("S","R"))),\
                ((1,("Z","0")),(6,("Z","0"),("S","S"))),\
                ((1,("Z","1")),(6,("Z","1"),("S","S"))),\
                ((1,("Z","Z")),(6,("Z","0"),("S","S"))),\
                ((2,("I","0")),(2,("I","0"),("S","R"))),\
                ((2,("I","1")),(2,("I","1"),("S","R"))),\
                ((2,("I","Z")),(3,("I","Z"),("S","L"))),\
                ((3,("I","1")),(3,("I","0"),("S","L"))),\
                ((3,("I","0")),(4,("I","1"),("S","L"))),\
                ((3,("I","$")),(5,("I","1"),("S","L"))),\
                ((4,("I","0")),(4,("I","0"),("S","L"))),\
                ((4,("I","1")),(4,("I","1"),("S","L"))),\
                ((4,("I","$")),(1,("I","$"),("R","R"))),\
                ((5,("I","Z")),(1,("I","$"),("R","R")))]

M2_un_to_bin = (d2_un_to_bin,0,6,7)