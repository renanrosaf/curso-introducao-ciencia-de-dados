
#TUPLA: ESTRUTURA QUE APRESENTA 2 VALORES (POSIÇÕES)
#CRIANDO UMA TUPLA: CRIO USANDO ()
contato=("Yan","324-5678") #contato não esta dentro uma lista ainda  e sim uma tupla

#ADICIONANDO  UMA TUPLA EM UMA LISTA

#Forma1:Crio uma tupla e adficiono em uma lista
telefones2=[] #lista vazia de elementos, primeiro crio lista vazia
telefones2.append(contato) #depois uso append.(nomedatupla)
print (telefones2)

#Forma 2:
#outra forma: Crio uma lista de tuplas, items com mais de um valor 

#Lista com tres tuplas: Items com mais de uma valor 
telefones3=[("Yan","2343-6678"),("Ana","3345-6678"),("Carlos","3345-6679")]
print(telefones3)

#ACESSAR ELEMENTO DE UMA LISTA:

#Acessando elemento de uma lista de tuplas: Aqui não posso acessar com o indice
#pois cada item tem 2 posições
print(telefones3[0])

#imprimindo apenas o numero do Yan' #POSIÇÃO O DA LISTA (DADOS YAN), POSIÇÃO 1: YAN
print(telefones3[0][1])

#imprimindo apenas o numero da ana
print(telefones3[1][1])