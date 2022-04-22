#============================================================#
# UE Calculabilite L3                                        #
# TME Machines de Turing : Composition de machines de Turing #
# Mathieu.Jaume@lip6.fr                                      #
#============================================================#

from Turing_1d import *

from ensembles import *

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
    d1,q1_0,q1_ok,q1_ko = M1
    d2,q2_0,q2_ok,q2_ko = M2

    if d1 == []:
        return M2
    if d2 == []:
        return M1

    eq_assoc = make_eq_set(make_eq_set(eq_atom))

    d_2 = []

    for (q1,a1),(q2,a2,m) in d2:
        d_2 = ajout(eq_assoc,(((2,q1),a1),((2,q2),a2,m)),d_2)

    d_nk = []
    d_ok1 = []
    d_ko1 = []

    for (q1,a1),(q2,a2,m) in d1:
        if not eq_atom(q2,q1_ok) and not eq_atom(q2,q1_ko):
            d_nk = ajout(eq_assoc,(((1,q1),a1),((1,q2),a2,m)),d_nk)
        elif eq_atom(q2,q1_ok):
            d_ok1 = ajout(eq_assoc,(((1,q1),a1),((2,q2_0),a2,m)),d_ok1)
        elif eq_atom(q2,q1_ko):
            d_ko1 = ajout(eq_assoc,(((1,q1),a1),((2,q2_ko),a2,m)),d_ko1)

    d = union(eq_assoc,union(eq_assoc,union(eq_assoc,d_2,d_nk),d_ok1),d_ko1)

    return (d,(1,q1_0),(2,q2_ok),(2,q2_ko))

M_opp_int_bin = ([(((1, 1), 'Z'), ((2, 0), 'Z', 'R')), (((2, 0), '0'), ((2, 1), '1', 'L')), (((2, 0), '1'), ((2, 0), '0', 'R')), (((2, 0), 'Z'), ((2, 2), '1', 'R')), (((2, 1), '0'), ((2, 1), '0', 'L')), (((2, 1), '1'), ((2, 1), '1', 'L')), (((2, 1), 'Z'), ((2, 3), 'Z', 'R')), (((2, 2), 'Z'), ((2, 1), 'Z', 'L')), (((1, 1), '1'), ((1, 1), '1', 'L')), (((1, 1), '0'), ((1, 1), '0', 'L')), (((1, 0), 'Z'), ((1, 1), 'Z', 'L')), (((1, 0), '1'), ((1, 0), '0', 'R')), (((1, 0), '0'), ((1, 0), '1', 'R'))],(1, 0),(2, 3),(2, 4))

# Composition de machines de Turing : conditionnelle
#---------------------------------------------------

def exec_cond_MT_1(MC,M1,M2,L,i0):
    (bc,ic,Lc)=exec_MT_1(MC,L,i0)
    if bc:
        return exec_MT_1(M1,Lc,ic)
    else:
        return exec_MT_1(M2,Lc,ic)


def make_cond_MT(MC,M1,M2):
     # M1,M2 : machines de Turing deterministes a 1 bande
    dc,qc_0,qc_ok,qc_ko = MC
    d1,q1_0,q1_ok,q1_ko = M1
    d2,q2_0,q2_ok,q2_ko = M2

    if dc == []:
        return M1

    eq_assoc = make_eq_set(make_eq_set(eq_atom))

    d_2 = []

    for (q1,a1),(q2,a2,m) in d2:
        d_2 = ajout(eq_assoc,(((2,q1),a1),((2,q2),a2,m)),d_2)

    d_nkC = []
    d_nk = []
    d_okC = []
    d_ok1 = []
    d_koC = []
    d_ko1 = []

    for (q1,a1),(q2,a2,m) in d1:
        if not eq_atom(q2,q1_ok) and not eq_atom(q2,q1_ko):
            d_nk = ajout(eq_assoc,(((1,q1),a1),((1,q2),a2,m)),d_nk)
        elif eq_atom(q2,q1_ok):
            d_ok1 = ajout(eq_assoc,(((1,q1),a1),((2,q2_ok),a2,m)),d_ok1)
        elif eq_atom(q2,q1_ko):
            d_ko1 = ajout(eq_assoc,(((1,q1),a1),((2,q2_ko),a2,m)),d_ko1)
    for (q1,a1),(q2,a2,m) in dc:
        if not eq_atom(q2,qc_ok) and not eq_atom(q2,qc_ko):
            d_nkC = ajout(eq_assoc,(((0,q1),a1),((0,q2),a2,m)),d_nkC)
        elif eq_atom(q2,qc_ok):
            if d1 != []:
                d_okC = ajout(eq_assoc,(((0,q1),a1),((1,q1_0),a2,m)),d_okC)
            else:
                d_okC = ajout(eq_assoc,(((0,q1),a1),((2,q2_ok),a2,m)),d_okC)
        elif eq_atom(q2,qc_ko):
            d_koC = ajout(eq_assoc,(((0,q1),a1),((2,q2_0),a2,m)),d_koC)       



    d = union(eq_assoc,union(eq_assoc,union(eq_assoc,union(eq_assoc,union(eq_assoc,union(eq_assoc,d_2,d_nk),d_ok1),d_ko1),d_nkC),d_okC),d_koC)

    return (d,(0,qc_0),(2,q2_ok),(2,q2_ko))

M_abs = ([(((0, 4), 'Z'), ((1, (1, 0)), 'Z', 'R')), (((1, (1, 1)), 'Z'), ((1, (2, 0)), 'Z', 'R')), (((1, (2, 0)), '0'), ((1, (2, 1)), '1', 'L')), (((1, (2, 0)), '1'), ((1, (2, 0)), '0', 'R')), (((1, (2, 0)), 'Z'), ((1, (2, 2)), '1', 'R')), (((1, (2, 1)), '0'), ((1, (2, 1)), '0', 'L')), (((1, (2, 1)), '1'), ((1, (2, 1)), '1', 'L')), (((1, (2, 2)), 'Z'), ((1, (2, 1)), 'Z', 'L')), (((1, (1, 1)), '1'), ((1, (1, 1)), '1', 'L')), (((1, (1, 1)), '0'), ((1, (1, 1)), '0', 'L')), (((1, (1, 0)), 'Z'), ((1, (1, 1)), 'Z', 'L')), (((1, (1, 0)), '1'), ((1, (1, 0)), '0', 'R')), (((1, (1, 0)), '0'), ((1, (1, 0)), '1', 'R')), (((1, (2, 1)), 'Z'), ((2, 0), 'Z', 'R')), (((0, 4), '1'), ((0, 4), '1', 'L')), (((0, 4), '0'), ((0, 4), '0', 'L')), (((0, 3), '1'), ((0, 3), '1', 'L')), (((0, 3), '0'), ((0, 3), '0', 'L')), (((0, 2), 'Z'), ((0, 4), 'Z', 'L')), (((0, 2), '1'), ((0, 2), '1', 'R')), (((0, 2), '0'), ((0, 1), '0', 'R')), (((0, 1), 'Z'), ((0, 3), 'Z', 'L')), (((0, 1), '1'), ((0, 2), '1', 'R')), (((0, 1), '0'), ((0, 1), '0', 'R')), (((0, 0), '1'), ((0, 2), '1', 'R')), (((0, 0), '0'), ((0, 1), '0', 'R')), (((0, 3), 'Z'), ((2, 0), 'Z', 'R'))], (0, 0), (2, 0), (2, 1))

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
    dc,qc_0,qc_ok,qc_ko = MC
    dp,qp_0,qp_ok,qp_ko = M

    eq_assoc = make_eq_set(make_eq_set(eq_atom))

    d_nokC = []
    d_nokP = []
    d_okC = []
    d_okP = []

    for (q1,a1),(q2,a2,m) in dc:
        if not eq_atom(q2,qc_ok):
            d_nokC = ajout(eq_assoc,(((0,q1),a1),((0,q2),a2,m)),d_nokC)
        else:
            d_okC = ajout(eq_assoc,(((0,q1),a1),((1,qp_0),a2,m)),d_okC)
    for (q1,a1),(q2,a2,m) in dp:
        if not eq_atom(q2,qp_ok):
            d_nokP = ajout(eq_assoc,(((1,q1),a1),((1,q2),a2,m)),d_nokP)
        else:
            d_okP = ajout(eq_assoc,(((1,q1),a1),((0,qc_0),a2,m)),d_okP)      

    d = union(eq_assoc,union(eq_assoc,union(eq_assoc,d_okC,d_nokC,),d_nokP),d_okP)

    return (d,(0,qc_0),(0,qc_ko),(1,qp_ko))

M_foo1 = make_loop_MT(M_eq_0,M_Right_bin)

M_foo0 = make_cond_MT(M_isneg,M_prop1,M_id)

M_foo2 = make_seq_MT(M_foo0,M_foo1)

M_foo3 = make_seq_MT(M_Right_bin,M_compl_bin)

M_eq_Z = make_test_eq("Z",["0","1","Z"])

M_foo4 = make_cond_MT(M_eq_Z,M_id,M_foo3)

M_foo = make_seq_MT(M_foo2,M_foo4)