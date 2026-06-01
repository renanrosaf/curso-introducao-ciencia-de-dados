def pure_increments(elements, index):
    #elementos: elemento da lista
    #index: indice
    new_elements=elements.copy() #garanto que a lista original não foi alterada
    #Passando a lista como cópia para new_elements
    new_elements[index]+=1
    return new_elements

#variavel lisa
#Estou criando uma lista de 1 até 9
lista=[1,2,3,4,5,6,7,8,9]

#pure_elements
#chamo a função  e faço print
print(pure_increments(lista,0))

#Efeito Colateral foi provocado
print(lista)
