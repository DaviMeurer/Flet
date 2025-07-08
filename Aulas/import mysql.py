import mysql.connector
user="root"
senha=""
host="localhost"
database="lanchonete"

#tentara puxar a conexão com o DB
try:
    conexao = mysql.connector.connect( #comando de puxar a conexão
        host=host,#igualando os parâmetros com as variáveis acima
        password=senha,
        user=user,
        database=database
    )
    if conexao.is_connected(): #testa se tem conexão
        print("Conexão estabelecida!")

        cursor = conexao.cursor()

        cursor.execute("SHOW TABLES") #chama um comando de BD
        retorno = cursor.fetchall() #segue junto acima

        print("Banco de dados:",retorno)

except mysql.connector.Error as e:
    print(f"Erro ao conectar com o BD: {e}")

finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada!")