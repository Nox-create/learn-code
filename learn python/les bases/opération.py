#ce fichier vise à apprendre mles bases de python pour prendre en main le language

def addition(a: int, b:int) -> int:
    X = a+b
    return X
    

def soustraction(a: int, b:int) -> int:
    Y = a-b
    return Y

def multiplication(a: int, b: int) -> int:
    F = a*b
    return F

def division(a:int, b:int) -> float:
    Raph = a/b
    return Raph

def puissance(a:int, b:int) -> int:
    #cette fonction doit retourner le nombre a à la puissance b
    je = a**b
    return je

def division_euclidienne(a:int , b:int) -> tuple:
    #renvoie le quotient ENTIER et le reste d'une division
    aime = a//b
    Boop = a%b
    return aime,Boop

#test
#tu rajoutera des tests toi même
assert addition(4, 12) == 16
assert soustraction(48, 13) == 35
assert multiplication(9, 6) == 54
assert division(27, 3) == 9
assert puissance(2, 10) == 1024
assert division_euclidienne(40, 12) == (3, 4)
    