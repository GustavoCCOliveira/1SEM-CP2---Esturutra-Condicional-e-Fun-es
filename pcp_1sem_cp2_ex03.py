#notas
cp1 = float(input("Digite a nota da CP1: "))
cp2 = float(input("Digite a nota da CP2: "))
cp3 = float(input("Digite a nota da CP3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global solution: "))

#descobre qual é a menor
menor = cp1
if cp2 < menor:
    menor = cp2
if cp3 < menor:
    menor = cp3

soma_cp = cp1 + cp2 + cp3 - menor

#média
media = (soma_cp + sp1 + sp2) / 4
media_final = media * 0.4 + gs * 0.6

#resultado
print(f"media: {media:.1f}")
print(f"media final: {media_final:.1f}")