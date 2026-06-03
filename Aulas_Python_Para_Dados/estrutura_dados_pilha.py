pilha=[] #Crio uma lista vazia

#Uma lista nativa em Python ela possui o conceito de Pilha
#Adicionando valores a pilha via método append
pilha.append(1)
pilha.append(2)
pilha.append(3)
print(pilha)


#Pilha=Last In First Out (LIFO)
#Ultima entrar  é o primeiro a sair da lista
#comando pop remove elemento da pilha, nesse caso elimna o ultimo elemento a entrar na lista 
#POP é first out
pilha.pop()
print(pilha)

#Fila: é do tipo FIFO (First In First Out)
#E nesse caso preciso importar um módulo especifico, pois a fila não é uma estrutura nativa do site
