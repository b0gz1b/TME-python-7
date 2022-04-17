#============================================================#
# UE Calculabilite L3                                        #
# TME Machines de Turing : Composition de machines de Turing #
# Mathieu.Jaume@lip6.fr                                      #
#============================================================#

from Turing_1d import *

# Machines de Turing utiles pour le TME
#---------------------------------------

# complement binaire et repositionnement de la tete de lecture au debut
# bande = mot binaire  se terminant par Z

d_compl_bin = [((0,"0"),(0,"1","R")), ((0,"1"),(0,"0","R")),\
               ((0,"Z"),(1,"Z","L")), ((1,"0"),(1,"0","L")),\
               ((1,"1"),(1,"1","L")), ((1,"Z"),(2,"Z","R"))]

M_compl_bin = (d_compl_bin,0,2,3)

# successeur d'un entier en representation binaire (bit de poids faibles a gauche)
# et repositionnement de la tete de lecture sur le bit de poids faible
# bande = mot binaire avec bits de poids faibles a gauche et se terminant par Z

d_succ_bin = [((0,"0"),(1,"1","L")), ((0,"1"),(0,"0","R")),\
              ((0,"Z"),(2,"1","R")), ((1,"0"),(1,"0","L")),\
              ((1,"1"),(1,"1","L")), ((1,"Z"),(3,"Z","R")),\
              ((2,"Z"),(1,"Z","L"))]

M_succ_bin = (d_succ_bin,0,3,4)

# fonction identite

M_id =([],0,0,1)

# Fonction qui construit une machine de Turing permettant de determiner
# si le symbole sous la tete de lecture est le caractere x et ne modifie
# pas la position de la tete de lecture
# C'est la MT qui accepte le langage { x }

def make_test_eq(c,alphabet):
    d = []
    for x in alphabet:
        if c==x:
            d = d + [((0,c),(1,c,"R"))]
        else:
            d = d + [((0,x),(2,x,"R"))]
        d = d + [((1,x),(3,x,"L")), ((2,x),(4,x,"L"))]
    M = (d,0,3,4)
    return M

# exemple

M_eq_0 = make_test_eq("0",["0","1","Z"])

def make_test_neq(c,alphabet):
    (d,q0,qok,qko) = make_test_eq(c,alphabet)
    return (d,q0,qko,qok)

M_neq_1 = make_test_neq("1",["0","1","Z"])

# deplacement de la tete de lecture a droite :

def make_MTright(alphabet):
    d = []
    for a in alphabet:
        d = d + [((0,a),(1,a,"R"))]
    M = (d,0,1,2)
    return M

M_Right_bin = make_MTright(["0","1","Z"])

# (propagation du bit de signe) : duplication du dernier bit d'un mot binaire


d_prop1 = [((0,"0"),(1,"0","R")), ((0,"1"),(2,"1","R")), \
           ((1,"0"),(1,"0","R")), ((1,"1"),(2,"1","R")), ((1,"Z"),(3,"0","L")),\
           ((2,"0"),(1,"0","R")), ((2,"1"),(2,"1","R")), ((2,"Z"),(3,"1","L")),\
           ((3,"0"),(3,"0","L")), ((3,"1"),(3,"1","L")), ((3,"Z"),(4,"Z","R"))]


M_prop1 =(d_prop1,0,4,5)

# Composition de machines de Turing : sequence
#---------------------------------------------

def exec_seq_MT_1(M1,M2,L,i1):
    (b,i2,L2)=exec_MT_1(M1,L,i1)
    if b:
        return exec_MT_1(M2,L2,i2)
    else:
        return (b,i2,L2)

def make_seq_MT(M1,M2):
    # M1,M2 : machines de Turing deterministes a 1 bande
    return

# Composition de machines de Turing : conditionnelle
#---------------------------------------------------

def exec_cond_MT_1(MC,M1,M2,L,i0):
    (bc,ic,Lc)=exec_MT_1(MC,L,i0)
    if bc:
        return exec_MT_1(M1,Lc,ic)
    else:
        return exec_MT_1(M2,Lc,ic)


def make_cond_MT(MC,M1,M2):
    # MC, M1, M2 : machines de Turing deterministes a 1 bande
    return

# Composition de machines de Turing : boucle
#-------------------------------------------

def exec_loop_MT_1(MC,M,L,i0):
    (bc,ic,Lc)=exec_MT_1(MC,L,i0)
    if bc:
        (bM,iM,LM) = exec_MT_1(M,Lc,ic)
        if bM:
            return exec_loop_MT_1(MC,M,LM,iM)
        else:
            return (False,iM,LM)
    else:
        return (True,ic,Lc)

def make_loop_MT(MC,M):
    # MC,M : machines de Turing deterministes a 1 bande
    return



