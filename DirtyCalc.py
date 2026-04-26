import math


def calculate_delta(a, b, c):
    """Calcule le discriminant (delta) d'une équation du 2nd degré."""
    return b * b - 4 * a * c


def solve_quadratic(a, b, c):
    """
    Résout une équation du 2nd degré ax² + bx + c = 0.
    Retourne un dictionnaire avec les solutions.
    """
    delta = calculate_delta(a, b, c)
    
    if delta == 0:
        x = (-b) / (2 * a)
        return {
            "type": "unique",
            "delta": delta,
            "solution": x
        }
    elif delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return {
            "type": "deux_solutions",
            "delta": delta,
            "x1": x1,
            "x2": x2
        }
    else:
        rr = -b / (2 * a)
        ii = math.sqrt(-delta) / (2 * a)
        return {
            "type": "imaginaire",
            "delta": delta,
            "real_part": rr,
            "imaginary_part": ii
        }


def format_result(result):
    """Formate le résultat pour l'affichage."""
    delta = result["delta"]
    print("Delta = ", delta)
    
    if result["type"] == "unique":
        print("Il y a une seule solution : x =", result["solution"])
    elif result["type"] == "deux_solutions":
        print("Deux solutions : x1 =", result["x1"], " x2 =", result["x2"])
    elif result["type"] == "imaginaire":
        print("Pas de solutions réelles car delta < 0.")
        print("Solutions imaginaires :")
        print("x1 =", result["real_part"], "-", result["imaginary_part"], "i")
        print("x2 =", result["real_part"], "+", result["imaginary_part"], "i")


def get_coefficients(prefix=""):
    """Demande à l'utilisateur d'entrer les coefficients a, b, c."""
    if prefix:
        print(f"On recommence {prefix} pour vérifier ???")
    print(f"Entrez a {prefix}: ")
    a = float(input())
    print(f"Entrez b {prefix}: ")
    b = float(input())
    print(f"Entrez c {prefix}: ")
    c = float(input())
    return a, b, c


def main():
    """Programme principal interactif."""
    print("********** CALCULETTE 2nd DEGRE **********")
    
    while True:
        a, b, c = get_coefficients()
        result = solve_quadratic(a, b, c)
        format_result(result)
        
        print("Voulez-vous recommencer ? (o/n)")
        rep = input()
        
        if rep == "n":
            print("Au revoir.")
            break
        elif rep != "o":
            print("Réponse non comprise.")


if __name__ == "__main__":
    main()
