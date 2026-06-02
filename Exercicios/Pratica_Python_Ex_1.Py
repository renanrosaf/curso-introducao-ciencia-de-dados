#Versão 1:
# nome=input("Digite o seu nome: ")
# idade_atual=int(input("Digite a sua idade: "))
# ano_nascimento=int(input("Digte o ano que você nasceu: "))
# idade_2030=2030-ano_nascimento

# print(f"Olá, {nome} em 2030, você terá {idade_2030} anos de idade ")

#Versão 2:
from datetime import date
nome=input("Digite o seu nome: ")
idade_atual=int(input("Digite a sua idade: "))

idade_2030=idade_atual + (2030-date.today().year)
print(f"Olá, {nome} em 2030, você terá {idade_2030} anos de idade ")