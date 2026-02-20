import sys
resultat = 0
if len(sys.argv) == 4 : 
    n1 = float(sys.argv[1])
    n2 = int(sys.argv[3])
    
    if sys.argv[2] == '*' :
        for _ in range(n2):
            resultat = resultat + n1

print(resultat)