from datetime import date

#Versão 1: Sem importação da data atuao
nome=input("Digite o seu nome: ")
idade_atual=int(input("Digite a sua idade: "))
ano_nascimento=int(input("Digte o ano que você nasceu: "))
idade_2030=2030-ano_nascimento

print(f"Olá, {nome} em 2030, você terá {idade_2030} anos de idade ")

#Versão 2:
#Aqui importei com módulo datetime e date importado

nome=input("Digite o seu nome: ")
idade_atual=int(input("Digite a sua idade: "))

idade_2030=idade_atual + (2030-date.today().year)
print(f"Olá, {nome} em 2030, você terá {idade_2030} anos de idade ")

#versão 3:SEM IMPORTAÇÃO DO MODULO
user=input("Digite o Seu Nome:") #Usuário entra com o nnome
age=int(input("Digite a Sua Idade:")) #Usuario entra com a idade

actual_year=2026
future_year=2030

age_2030 = age + (future_year-actual_year)

print(f" {user} em 2030 você terá: {age_2030}")
