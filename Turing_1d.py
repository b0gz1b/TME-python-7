#=====================================================================#
# UE Calculabilite L3                                                 #
# TME Machines de Turing : Machines de Turing deterministes a 1 bande #
# Mathieu.Jaume@lip6.fr                                               #
#=====================================================================#

# Fonction associee a une liste representant une fonction sur un domaine fini
#----------------------------------------------------------------------------

def assoc_f(lf,x):
    """ list[alpha*beta] * alpha -> beta """
    for (xf,yf) in lf:
        if xf == x:
            return yf
    return None

# Machine de Turing deterministe a 1 bande
#-----------------------------------------
#
# M = (d,q0,qok,qko)
# d = ((q,a),(q',a',m))
#

# exemple

l_M_ex1 = [((0,"A"),(1,"A","R")), ((0,"a"),(3,"a","R")), ((0,"b"),(3,"b","R")),
           ((0,"B"),(3,"B","R")), ((1,"A"),(3,"A","R")), ((1,"B"),(2,"B","R")),
           ((1,"a"),(1,"b","R")), ((1,"b"),(1,"a","R"))]

M_ex1 =(l_M_ex1,0,2,3)


# Affichage d'une configuration pour une machine de Turing a 1 bande
#-------------------------------------------------------------------

def print_config_1(L,t,q,qok,qko):
    for s in L[:t]:
        print(s,end='')
    print("|",end='')
    if q == qok:
        print("ok",end='')
    elif q == qko:
        print("ko",end='')
    else:
        print(q,end='')
    print("|",end='')
    for s in L[t:]:
        print(s,end='')
    print(" ")

# print_config_1([1,2,3,4,5,6,7,8,9],9,"q","q2","q3")



# Execution d'une machine de Turing deterministe a 1 bande
#---------------------------------------------------------

def exec_MT_1(M,L,i0):
    # M : machine de Turing deterministe a 1 bande
    # L : liste representant la bande initiale
    # i0 : position initiale de la tete de lecture
    return

# exemples

# exec_MT_1(M_ex1,["A","a","b","a","a","B"],0)
# exec_MT_1(M_ex1,["B","a","b","a","a","B"],0)
