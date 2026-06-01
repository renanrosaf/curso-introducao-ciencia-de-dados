#Lista: Coleção ordenada de objetos mutaveis

#1:Criando uma lista: Utlizo de []
telefones =['1234-5678','9999-9999','8765-4321','8877-7768']
print(telefones)    #imprimindo a lista criada

#Adicionando elementos em uma lista
#1° Forma: Método Append,nesse método o elemento adicionado irá para a ultima
#posição da lista criada e só utilizo o parametro do elemento a ser adicionado
telefones.append('555-5555')
print(telefones)

#2° Forma: Método Insert
#Nesse método eu preciso indicar a posição da lista de onde eu quero 
#inserir o objeto a ser adcionado, além do elemento 
#indiquei a posição 0
telefones.insert(0,"444-44444")
print(telefones)

#2:Removendo elementos de uma lista
#1: Forma: Usar o método remove
#Nesse método, parametros é apenas o elemento que quero remover
telefones.remove("444-44444")
print(telefones)

#2°Método é o POP
#Nesse método o parametro é apenas a posição(indice) do elemento a ser removido
#Lembrando que 0 é sempre a posição inicial
telefones.pop(1)
print(telefones)

#3° Tupla({});  Crio usando {}
contato=("Yan","324-5678") #contato não esta dentro uma lista

#adicionando uma tupla em uma lista
telefones2=[] #lista vazia de elementos, primeiro crio lista vazia
telefones2.append(contato) #depois uso append.(nomedatupla)
print (telefones2)

#outra forma: Crio uma lista de tuplas, items com mais de um valor 
#Lista com tres tuplas
telefones3=[("Yan","2343-6678"),("Ana","3345-6678"),("Carlos","3345-6679")]
print(telefones3)

#Acessando elemento de uma lista de tuplas: Aqui não posso acessar com o indice
#pois cada item tem 2 posições
print(telefones3[0])

#imprimindo apenas o numero do Yan'
print(telefones3[0][1])

#imprimindo apenas o numero da ana
print(telefones3[1][1])