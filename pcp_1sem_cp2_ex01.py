#Entrada de dados
estado_origem = int(input("Digite o código do estado (1 a 5): "))
peso_toneladas = float(input("Digite o peso da carga em toneladas: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

#Calcular o peso em quilos
peso_quilos = peso_toneladas * 1000

#Calcular o preço da carga com base no código
if 10 <= codigo_carga <= 20:
    preco_por_kg = 100.00
elif 21 <= codigo_carga <= 30:
    preco_por_kg = 250.00
elif 31 <= codigo_carga <= 40:
    preco_por_kg = 340.00
else:
    preco_por_kg = 0.00 #se o código for invalido ou inexistente

preco_carga = peso_quilos * preco_por_kg

#Calculo de imposto com base do estado de origem
if estado_origem == 1:
    porcentagem_imposto = 0.35
elif estado_origem == 2:
    porcentagem_imposto = 0.25
elif estado_origem == 3:
    porcentagem_imposto = 0.15
elif estado_origem == 4
    porcentagem_imposto = 0.05
elif estado_origem == 5
    porcentagem_imposto = 0.00 #isento de imposto
else:
    porcentagem_imposto = 0.00

valor_imposto = preco_carga * porcentagem_imposto

#Calcular o valor total
