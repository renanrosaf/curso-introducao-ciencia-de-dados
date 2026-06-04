#Lista: Coleção ordenada de objetos mutaveis

#1:CRIANDO UMA LISTA : Utlizo de []
telefones =['1234-5678','9999-9999','8765-4321','8877-7768']
print(telefones)    #imprimindo a lista criada

#Lista é uma sequência de valores, espécie de container de valores do mesmo tipo ou diferentes tipos

#2:ACESSANDO ELEMENTOS DE UMA LISTA
#indico indice no colchetes
#1°Elemento de uma lista: indice 0
print(telefones[0])

#3: ADICIONANDO ELEMENTOS EM UMA LISTA
#1° Forma: Método Append,nesse método o elemento adicionado irá para a ultima poisção da lista
#posição da lista criada e só utilizo o parametro do elemento a ser adicionado
telefones.append('555-5555')
print(telefones)

#2° Forma: Método Insert
#Nesse método eu preciso indicar a posição da lista de onde eu quero 
#inserir o objeto a ser adcionado, além do elemento 
#indiquei a posição 0, ou seja sera na primeira posição da lista
telefones.insert(0,"444-44444")
print(telefones)

#4 REMOVENDO ELEMENTOS DE UMA LISTA:
#1: Forma: Usar o método remove
#Nesse método, parametros é apenas o elemento que quero remover
telefones.remove("444-44444")
print(telefones)

#2°Método é o POP
#Nesse método o parametro é apenas a posição(indice) do elemento a ser removido
#Lembrando que 0 é sempre a posição inicial
telefones.pop(1)
print(telefones)

