import mysql.connector
user="root"
senha=""
host="localhost"
database="lanchonete"

#retorna a conexão estabelecida ou None caso dê errado
def conectar():
    conexao=None
    try:
        conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=senha,
            database=database
        )
    except mysql.connector.Error as e:
        print(f"Erro ao conectar com BD:{e}")

    return conexao

#finalizar a conexão o fim das operações
def fechar_conexao(conexao):
    if conexao.is_connected():
        conexao.close()
        print("Conexão terminada!")

#CREATE

def read(conexao): #READ
    try:
        cursor = conexao.cursor()
        query = "Select * from produtos"
        cursor.execute(query)
        registros = cursor.fetchall()

        for produto in registros:
            print(produto)

    except mysql.connector.Error as e:
        print(f"Erro ao listar produtos: {e}")
    finally:
        cursor.close()

#UPDATE

#DELETE

#MAIN
conexao = conectar()
if conexao:
    print("Conectado com o banco de dados!")

    read(conexao)

    fechar_conexao(conexao)