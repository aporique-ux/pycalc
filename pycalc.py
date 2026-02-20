import sys
resultat = 0
if len(sys.argv) == 4 : 
    n1 = float(sys.argv[1])
    n2 = int(sys.argv[3])
    
    if sys.argv[2] == '*' :
        for _ in range(n2):
            resultat = resultat + n1

    elif sys.argv[2] == '/' :
        resultat = n1/n2

    elif sys.argv[2] == '+' :
        resultat = n1+n2
    
    elif sys.argv[2] == '-' :
        resultat = n1-n2
    
print(resultat)
