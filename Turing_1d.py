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
    d,q0,qok,qko = M
    q = q0
    t = i0
    while True:
        # print_config_1(L,t,q,qok,qko)
        T = assoc_f(d,(q,L[t]))
        if T != None:
            q, ns, m = T
            L[t] = ns
            if m == "R":
                t += 1
                if t >= len(L):
                    L.append("Z")
            else:
                t -= 1
                if t < 0:
                    t = 0
                    L.insert(0,"Z")
        else:
            break
    return (q == qok,t,L)

# exemples

# exec_MT_1(M_ex1,["A","a","b","a","a","B"],0)
# exec_MT_1(M_ex1,["B","a","b","a","a","B"],0)

l_ex2 = [((0,"a"),(1,"X","R")), ((0,"b"),(2,"X","R")), \
         ((0,"Z"),(4,"Z","R")), ((1,"a"),(1,"a","R")), \
         ((1,"Y"),(1,"Y","R")), ((1,"b"),(3,"Y","L")), \
         ((2,"b"),(2,"b","R")), ((2,"Y"),(2,"Y","R")), \
         ((2,"a"),(3,"Y","L")), ((3,"a"),(3,"a","L")), \
         ((3,"b"),(3,"b","L")), ((3,"Y"),(3,"Y","L")), \
         ((3,"X"),(0,"X","R")), ((0,"Y"),(0,"Y","R"))]

M_ex2 =(l_ex2,0,4,5)


d_isneg = [((0,"0"),(1,"0","R")), ((0,"1"),(2,"1","R")), \
           ((1,"0"),(1,"0","R")), ((1,"1"),(2,"1","R")), ((1,"Z"),(3,"Z","L")),\
           ((2,"0"),(1,"0","R")), ((2,"1"),(2,"1","R")), ((2,"Z"),(4,"Z","L")),\
           ((3,"0"),(3,"0","L")), ((3,"1"),(3,"1","L")), ((3,"Z"),(5,"Z","R")),\
           ((4,"0"),(4,"0","L")), ((4,"1"),(4,"1","L")), ((4,"Z"),(6,"Z","R"))]

M_isneg =(d_isneg,0,6,5)
