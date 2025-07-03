#Revisão de listas
contato = [] #criando lista

contato = ["Rafael", 1992, True, 20.23] #atribuindo valores para a lista
contato2 = ["João Dev", 1998, True, 21.23] #criando outra lista
listaLista = [contato, contato2] #criando lista de lista

#Revisão dicionário
dictContato = { #composto por chave e valor
    "Nome": "Rafael",
    "Nascimento": 1992,
    "Telefone": 6799999999
    }

dictContato2 = { #criando outro dicionário
    "Nome": "João Dev",
    "Nascimento": 1998,
    "Telefone": 67999999999
    }

listaContato = [dictContato, dictContato2] #cria uma lista de dicionário
print(listaContato[1]["Nome"],"\n")

for contato in listaContato: #iterar a lista, que tenha em cada iteração
                             #temos um dicionário na variável contato
    print(contato["Nome"])