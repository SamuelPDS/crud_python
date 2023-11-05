import mysql.connector
from Piloto import Piloto

con = mysql.connector.connect(host='localhost', database='oo_promove', user='root', password='')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()


def CreatePiloto(piloto):
    query = "INSERT INTO piloto (id, ano_campeonato, nacionalidade, nome_piloto, equipe) VALUES (%s, %s, %s, %s, %s )"
    values = (piloto.id, piloto.ano_campeonato, piloto.nacionalidade, piloto.nome_piloto, piloto.equipe)
    cursor.execute(query, values)
    print("Registro feito com sucesso!!!")
    con.commit()


def ReadPiloto():
    url = "select * from piloto"
    cursor.execute(url)
    dados_pilotos = cursor.fetchall()
    listapiloto = []

    for linha in dados_pilotos:
        piloto = Piloto()
        piloto.id = int(linha[0])
        piloto.ano_campeonato = linha[1]
        piloto.nacionalidade = linha[2]
        piloto.nome_piloto = linha[3]
        piloto.equipe = linha[4]

        listapiloto.append(piloto)

    for piloto_dados in listapiloto:
        print(
            f"ID: {piloto_dados.id}, Ano do campeonato: {piloto_dados.ano_campeonato}, Nacionalidade: {piloto_dados.nacionalidade}, Nome do Piloto: {piloto_dados.nome_piloto}, Equipe Ganhadora: {piloto.equipe}")
    print("\n Dados lidos com sucesso!!!")


def UpdatePiloto(piloto):
    url = "UPDATE piloto set ano_campeonato= %s, " \
          "nacionalidade= %s, nome_piloto= %s, equipe= %s" \
          "WHERE id= %s"
    values = (piloto.ano_campeonato, piloto.nacionalidade, piloto.nome_piloto, piloto.equipe, piloto.id)
    cursor.execute(url, values)
    con.commit()
    print("Registro alterado com sucesso!!!")


def DeletePiloto(piloto):
    url = f"DELETE from piloto " \
          f"WHERE id= {piloto.id}"
    cursor.execute(url)
    con.commit()
    print("Piloto excluído com sucesso!!")


def FechaConexao():
    if con.is_connected():
        cursor.close()
        con.close()
        print("conexão encerrada")


while True:
    inp = int(input("\nDigite um número, sendo: \n1 - Criar usuário \n"
                          "2 - Ler os usuarios dentro do bando de dados \n"
                          "3 - Alterar usuário \n"
                          "4 - Exluir Usuário \n"
                          "0 - Sair"))

    if inp == 1:
        piloto = Piloto()
        piloto.ano_campeonato = int(input("Digite o ano do campeonato:"))
        piloto.nacionalidade = input("Digite a Nacionalidade do piloto:")
        piloto.nome_piloto = input("Digite o nome do piloto:")
        piloto.equipe = input("Digite a equipe vencedora:")
        CreatePiloto(piloto)

    elif inp == 2:
        ReadPiloto()

    elif inp == 3:
        piloto = Piloto()
        piloto.ano_campeonato = int(input("Digite o ano do campeonato:"))
        piloto.nacionalidade = input("Digite a Nacionalidade do piloto:")
        piloto.nome_piloto = input("Digite o nome do pilto:")
        piloto.equipe = input("Digite a equipe vencedora:")
        piloto.id = int(input("Digite o Id do Piloto a ser alterado"))
        UpdatePiloto(piloto)

    elif inp == 4:
        delpilot = Piloto()
        delpilot.id = int(input("Digite o ID que você deseja excluir"))
        DeletePiloto(delpilot)

    elif inp == 0:
        print("Operação encerrado com sucesso!")
        break

    else:
        print("Digite um número válido")

