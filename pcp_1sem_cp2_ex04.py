nome = input("Digite o nome do funcionário: ")
print("Cargos: 1Gerente, 2-Analista, 3-Assistente, 4-Estagiário")
cargo_cod = int(input("Digite o código do cargo: "))
salario_base = float(input("Digite o salário base (float): "))
horas_extras = int(input("Total de horas extras trabalhadas: "))
faltas = int(input("Total de faltas no mês: "))
recebeu_bonus = input("Recebeu bônus por desempenho? (s/n): ").lower()



# Valor da hora extra: 1SEM-CP2---Esturutra-Condicional-e-Fun-es.5% do salário base por hora
valor_total_extra = horas_extras * (salario_base * 0.015)

# Desconto por falta: 2% do salário base por falta
desconto_faltas = faltas * (salario_base * 0.02)

bonus_valor = 0
if recebeu_bonus == 's':
    if cargo_cod == 1:
        bonus_valor = 1000
    elif cargo_cod == 2:
        bonus_valor = 500
    elif cargo_cod == 3:
        bonus_valor = 300
    elif cargo_cod == 4:
        bonus_valor = 100

# Cálculo do Salário Líquido Final
salario_liquido = salario_base + valor_total_extra + bonus_valor - desconto_faltas

# 3. O sistema deve calcular e mostrar:
print("\n" + "="*30)
print(f"RESUMO DO PAGAMENTO: {nome}")
print(f"Salário Base: R$ {salario_base:.2f}")
print(f"Adicional Horas Extras: R$ {valor_total_extra:.2f}")
print(f"Bônus Desempenho: R$ {bonus_valor:.2f}")
print(f"Desconto por Faltas: R$ {desconto_faltas:.2f}")
print("-" * 30)
print(f"SALÁRIO LÍQUIDO: R$ {salario_liquido:.2f}")
print("="*30)