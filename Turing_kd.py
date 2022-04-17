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
    return

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












