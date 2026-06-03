def dividir(a,b):
    r=0
    try: 
        r=a/b
        return print (r)
    except ZeroDivisionError:
        print("Erro: Divisão Por Zero")
    except:
        print("Erro inesperado.Desculpe.")
    finally:
        print("Função Executada.")
#print(dividir(4,2))

#Erro de Excessão
#print(dividir(4,0))

#Lidando com Erros:
#Usando o Try, Except, Finally

#Passando Letra
print(4,'a')