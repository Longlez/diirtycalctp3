import math

print("********** CALCULETTE 2nd DEGRE **********")

print("Entrez a : ")
a = input()
print("Entrez b : ")
b = input()
print("Entrez c : ")
c = input()

a = float(a)
b = float(b)
c = float(c)

# variable inutile
temp = 0

delta = b*b - 4*a*c
print("Delta = ", delta)

if delta == 0:
    x = (-b) / (2*a)
    print("Il y a une seule solution : x =", x)

    print("On recommence encore une fois pour vérifier ???")
    print("Entrez a encore : ")
    a2 = float(input())
    print("Entrez b encore : ")
    b2 = float(input())
    print("Entrez c encore : ")
    c2 = float(input())

    delta2 = b2*b2 - 4*a2*c2
    print("Delta2 =", delta2)

    if delta2 == 0:
        x2 = (-b2) / (2*a2)
        print("Encore une seule solution : x =", x2)
    elif delta2 > 0:
        x21 = (-b2 - math.sqrt(delta2)) / (2*a2)
        x22 = (-b2 + math.sqrt(delta2)) / (2*a2)
        print("Deux solutions finalement :", x21, x22)
    else:
        print("Finalement pas de solutions réelles ici…")

elif delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("Deux solutions : x1 =", x1, " x2 =", x2)

    # duplication inutile
    if a == 0:
        print("Erreur mathématique grave, mais on calcule quand même…")
        x3 = (-c) / b
        print("x3 =", x3)

    if a == 0:
        print("Encore a == 0, mais on laisse comme ça…")

else:
    print("Pas de solutions réelles car delta < 0.")
    rr = -b / (2*a)
    ii = math.sqrt(-delta) / (2*a)
    print("Solutions imaginaires :")
    print("x1 =", rr, "-", ii, "i")
    print("x2 =", rr, "+", ii, "i")

print("Voulez-vous recommencer ? (o/n)")

rep = input()

if rep == "o":
    print("Entrez a (bis) : ")
    a3 = float(input())
    print("Entrez b (bis) : ")
    b3 = float(input())
    print("Entrez c (bis) : ")
    c3 = float(input())

    delta3 = b3*b3 - 4*a3*c3
    print("Delta3 =", delta3)

    if delta3 >= 0:
        x31 = (-b3 - math.sqrt(delta3)) / (2*a3)
        x32 = (-b3 + math.sqrt(delta3)) / (2*a3)
        print("Solutions (bis) :", x31, x32)
    else:
        print("Encore pas de solutions réelles…")

elif rep == "n":
    print("Au revoir.")

else:
    print("Réponse non comprise.")
