nome = input("digite seu primeiro nome: ")

parte1nome = nome[0:20]

salario = input("digite seu salario: ")

parte3salario = salario[0:1]
parte4salario = salario[1:4]
parte5salario = salario[4:6]

salarioformatado = parte3salario + "." + parte4salario + "," + parte5salario

recebimento = parte1nome + " no mes de abril recebeu um salario de R$" + salarioformatado + " reais"

print(recebimento)