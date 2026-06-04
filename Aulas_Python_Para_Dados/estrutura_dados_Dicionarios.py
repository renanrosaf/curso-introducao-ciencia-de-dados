#Lista de tuplas
telefones3=[("Yan","2345-6678"),("Ana","3345-66778"),("Carlos","3345-6679")]
print(telefones3)

#1: TRANSFORMANDO LISTAS DE TUPLICAS EM DICIONÁRIOS:
#Uso função DICT do python
#Tupla em elementos com chave e valor
telefones3_dict =dict(telefones3)
print(telefones3_dict)

#No dicionário é realizado por chaves
#dicionario tem item em formato: chave: acesso o item e o segundo o valor: valor que 
#atribui a chave

#2: ACESSANDO ELEMENTOS EM DICIONÁRIO
#Acesso via CHAVES
#buscando o telefone atribuido a Yan:Acesso pela chave
#variavel[chave do dicionário]
print (telefones3_dict["Yan"]) #Imprimo valor atribuido ao YAN

#3: ADICIONANDO ELEMENTO AO DICIONÁRIO
#Para Adicionar elemento ao dicionário
#variavel[chave]=valor
telefones3_dict["Paulo"]="3345-9969"
print(telefones3_dict)

#4: REMOVENDO ELEMENTO DE UM DICIONÁRIO
#Para remover um elemento de um dicionário, aplico o  Método Pop e passo a chave como argumento da função POP
telefones3_dict.pop("Paulo")
print(telefones3_dict)