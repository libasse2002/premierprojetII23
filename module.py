def premier(m):
    cpt=0
    for i in range (1,m+1):
        if m%i==0:
            cpt+=1
    if cpt==2:
        return True
    else:
        return False
n = int(input("Entrez un nombre positif : "))
while n<=0:
    n = int(input("Entrez un nombre positif : "))
if premier(n):
    print("Le nombre",n,"est bien premier.")
else:
    print("Le nombre",n,"n'est pas premier.")
def nombres_premiers(k):
    for j in range(1,k+1):
        if premier(k):
            print (k,end=" ")
b=int(input("veuillez saisir un entier positif: "))
while b<=0 :
    b=int(input("Veuillez saisir un nombre positif: "))
print("Les nombres premiers compris entre 1 et" ,b,"sont:",end=" ")
nombres_premiers(b)
