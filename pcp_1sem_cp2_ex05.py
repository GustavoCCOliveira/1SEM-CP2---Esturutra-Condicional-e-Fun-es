#Criar um programa aonde ele consiga analizar Nome, idade, valor de renda mensal, valor desejado do emprestimo, numero de parcelas (3 ate 24 )
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda = int(input("Digite sua renda mensal: "))
emprestimo = float(input("Valor do empréstimo: "))
parcelas = int(input("Número de parcelas (3 a 24): "))
#Agora o maximo de emprestimo e a renda x 20
maximo = renda * 20
if parcelas <= 6:
    print("Seu valor e de 5% de parcelas por mes")
#tenho que resolver a formula das parcelas e a resolucao pra a quantidade de parcelas extras
#agora adicionar o valor do financiamento
if idade < 18:
     print("Idade invalida!")
else:
    if idade >= 18:
     print("Seu emprestimo gera um valor de ")
