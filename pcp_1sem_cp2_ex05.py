#Criar um programa aonde ele consiga analizar Nome, idade, valor de renda mensal, valor desejado do emprestimo, numero de parcelas (3 ate 24 )
print("=== Cadastro para Empréstimo ===")
print("Preencha as informações abaixo:\n")

nome = input("Nome: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: "))
emprestimo = float(input("Valor do empréstimo: "))
parcelas = int(input("Parcelas (3 a 24): "))

#Agora o maximo de emprestimo e a renda x 20
maximo = renda * 20
if idade <= 18:
    print("Empréstimo negado: menor de idade")
    exit()

if emprestimo > maximo:
    print("Empréstimo negado: valor excede 20x sua renda")
    exit()

if parcelas <= 6:
    i = 0.05
elif parcelas <= 12:
    i = 0.08
elif parcelas <= 24:
    i = 0.10
else:
    print("Número de parcelas inválido")
    exit()

#PMT formula da renda = PV . i(1+i)n/ (1+i)n-1
n = parcelas
PV = emprestimo

PMT = PV * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
print("|============================|")
print(f" Cliente: {nome}")
print(f" Empréstimo aprovado!\n")
print(f" Valor da parcela: R$ {PMT:.2f}\n")
print(f" Total pago: R$ {PMT * n:.2f}\n")
print("|============================|")