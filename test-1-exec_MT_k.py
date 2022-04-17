from Turing_kd import *
from ensembles import * 
from machines3b import *


print("\n\n----------------------------------------------\n\n")
print("Test 1 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M2_ex1,2,[["Z"],["Z"]],[0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [0,0], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["Z"],["Z"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 2 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M2_ex1,2,[["a","b","b","a","a","a","b","b","Z"],["Z"]],[0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [8,0], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["a","b","b","a","a","a","b","b","Z"],["X","Z","Z"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 3 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M2_ex1,2,[["a","b","b","a","a","a","b","a","Z"],["Z"]],[0,0])
assert b == False, "Erreur dans le langage accepte"
assert T == [8,2], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["a","b","b","a","a","a","b","a","Z"],["X","Z","Z"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 4 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M2_palin_bin,2,[["Z"],["Z"]],[0,0])
assert b== True, "Erreur dans le langage accepte"
assert T == [0,0], "Erreur dans les positions des testes de lectures sur les bandes"
assert L == [["Z","Z"],["Z","Z"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 5 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M2_palin_bin,2,[["0","Z"],["Z"]],[0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [2,0], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["Z","X","Z"], ["Z","X","Z"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 6 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M2_palin_bin,2,[["1","1","1","0","1","Z"],["Z"]],[0,0])
assert b == False, "Erreur dans le langage accepte"
assert T == [2,3], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["Z","X","1","1","0","1","Z"],["1","1","1","0","X","Z"]], "Erreur dans le contenu des bandes"


print("\n\n----------------------------------------------\n\n")
print("Test 7 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M2_palin_bin,2,[["1","0","1","0","1","Z"],["Z"]],[0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [6,0], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["Z","X","X","X","X","X","Z"],["Z","X","X","X","X","X","Z"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 8 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M2_un_to_bin,2,[["$"],["Z"]],[0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [1,1], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["$", "Z"],["$","0"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 8 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L)= exec_MT_k(M2_un_to_bin,2,[["$","I","I","I","I","I","I"],["Z"]],[0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [7,1], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["$","I","I","I","I","I","I","Z"],["$","1","1","0","Z"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 9 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M2_anbncn,2,[["a","b","c","c"],["Z"]],[0,0])
assert b == False, "Erreur dans le langage accepte"
assert T == [3,2], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["a","b","c","c"],["Z","C","Z"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 10 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L)=exec_MT_k(M2_anbncn,2,[["a","a","b","b","c","c"],["Z"]],[0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [7,4], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["a","a","b","b","c","c","Z","Z"],["Z","C","C","Z","Z"]], "Erreur dans le contenu des bandes"


print("\n\n----------------------------------------------\n\n")
print("Test 11 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L)= exec_MT_k(M2_anbncn,2,[["a","a","a","b","b","c","c"],["Z"]],[0,0])
assert b == False, "Erreur dans le langage accepte"
assert T == [5,0], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [["a","a","a","b","b","c","c"],["A","B","B","Z"]], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 12 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L)= exec_MT_k(M3_add_bin_3,3,[[1,0,1,1],[1,0,0,1],["Z"]],[0,0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [4, 4, 5], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [[1, 0, 1, 1, 'Z'], [1, 0, 0, 1, 'Z'], [0, 1, 1, 0, 1, 'Z']], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 13 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M3_add_bin_3,3,[[1,0,1,1,0,0,0,1],[1,0,0,1],["Z"]],[0,0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [8, 4, 8], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [[1, 0, 1, 1, 0, 0, 0, 1, 'Z'], [1, 0, 0, 1, 'Z'], [0, 1, 1, 0, 1, 0, 0, 1, 'Z']], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 14 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M3_add_bin_3,3,[[0,1,1],[1,1],["Z"]],[0,0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [3,2,4], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [[0, 1, 1, 'Z'], [1, 1, 'Z'], [1, 0, 0, 1, 'Z']], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 15 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M3_mult_un_3,3,[["$","I","I"],["$"],["Z"]],[0,0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [2,0,1], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [['$', 'X', 'I'], ['$', 'Z'], ['$', 'Z']], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 16 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L) = exec_MT_k(M3_mult_un_3,3,[["$"],["$"],["Z"]],[0,0,0])

assert b == True, "Erreur dans le langage accepte"
assert T == [1,1,1], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [['$', 'Z'], ['$', 'Z'], ['$', 'Z']], "Erreur dans le contenu des bandes"

print("\n\n----------------------------------------------\n\n")
print("Test 17 : exec_MT_k")
print("--------------------------------------------------")
(b,T,L)= exec_MT_k(M3_mult_un_3,3,[["$","I","I","I"],["$","I","I"],["Z"]],[0,0,0])
assert b == True, "Erreur dans le langage accepte"
assert T == [4, 2, 7], "Erreur dans les positions des tetes de lecture sur les bandes"
assert L == [['$', 'X', 'X', 'X', 'Z'], ['$', 'I', 'I', 'Z'], ['$', 'I', 'I', 'I', 'I', 'I', 'I', 'Z']], "Erreur dans le contenu des bandes"
