#Fila: é do tipo FIFO (First In First Out)
#E nesse caso preciso importar um módulo especifico, pois a fila não é uma estrutura nativa do python


from collections import deque #Preciso importar esse módulo quando eu for trabalhar com Fila em Python
#FILA é do tipo First In First Out
#Atribuo a uma variável o módulo DEQUE

fila=deque() #Fila esta recebendo o comportamento do modulado instalado de fila

#Adicionando elementos na fila: Uso append
fila.append(1)
fila.append(2)
fila.append(3)
print(fila)

#Removendo elementos da fila: FIFO
#Aqui compartamentos é diferente do da lista padrão, uso aqui o Pop Left ao invés de Pop aplicado a lista padrão
fila.popleft()
print(fila) #Como Fila é FIFO, ela irá excluir o primeiro item da lista a ser removida, pois foi o primeiro elemento a entrar na lista, no caso é o 1
