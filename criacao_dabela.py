import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='db_filmes', user='user')

    criar_tabela_sql = """Create TABLE tb_produtos ( 
                          IdFilme int(1) NOT NULL,
                          NomeFilme VARCHAR (255) NOT NULL,
                          Diretor VARCHAR(100) NOT NULL,
                          PRIMARY KEY(idFilme))"""

    cursor = con.cursor()
    cursor.execute(criar_tabela_sql)
    print("Tabela criada com sucesso !!")
except mysql.connector.Error as erro:
    print("Falha em criar a tabela: {}", format(erro))
finally:
    if con.is_connected():
        cursor.close()
        print("Conexao finalizada com sucesso")
