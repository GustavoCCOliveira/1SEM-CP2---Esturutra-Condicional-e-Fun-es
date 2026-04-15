A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# A ≥ B ≥ C
if B > A:
    A, B = B, A
if C > A:
    C, A = A, C
if B > C:
    B, C = C, B

#verifica se forma ou n um triang.
if A >= B + C:
    A, B = B, A
    print("NAO FORMA TRIANGULO")
else:
    if A ** 2 == B ** 2 + C ** 2:
        print("TRIANGULO RETANGULO")
    elif A ** 2 > B ** 2 + C ** 2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

#tipo pelos lados do triang.
if A == B and B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or B == C or A == C:
    print("TRIANGULO ISOSCELES")
