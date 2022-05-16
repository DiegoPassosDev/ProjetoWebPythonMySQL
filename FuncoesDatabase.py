import database as db
import Cliente as Cliente
import Movimentacao as Movimentacao

#FUNÇÕES DOS CLIENTES
def AdicionarCliente(cliente):
    db.cursor.execute(f'INSERT INTO cliente(clienteCont, numCont, tipoCont, statusCont, categoriaCont) VALUES '
                      f'("{cliente.clienteCont}", "{cliente.numCont}", {cliente.tipoCont}, "{cliente.statusCont}", '
                      f'"{cliente.categoriaCont}")')
    db.conexao.commit()


def SelecionarClientes():
    db.cursor.execute('SELECT * FROM cliente')
    listaCliente = []

    for r in db.cursor.fetchall():
        listaCliente.append(Cliente.Cliente(r[0], r[1], r[2], r[3], r[4], r[5]))

    return listaCliente


def NomeClientes():
    db.cursor.execute('SELECT DISTINCT clienteCont FROM cliente')
    data = db.cursor.fetchall()
    return data


def getCliente(nome):
    db.cursor.execute(f'SELECT * FROM cliente WHERE clienteCont = "{nome}"')
    data = db.cursor.fetchall()
    return data


def EditarCliente(nClienteCont, nNumCont, nTipoCont, nStatusCont, nCategoriaCont, clienteCont, numCont, tipoCont,
                  statusCont, categoriaCont):
    db.cursor.execute(f'UPDATE cliente SET clienteCont = "{nClienteCont}", numCont = "{nNumCont}", '
                      f'tipoCont = {nTipoCont}, statusCont = "{nStatusCont}", categoriaCont = "{nCategoriaCont}" '
                      f'WHERE  clienteCont = "{clienteCont}" AND numCont = "{numCont}" AND '
                      f'tipoCont = {tipoCont} AND statusCont = "{statusCont}" AND categoriaCont = "{categoriaCont}"')
    db.conexao.commit()
    data = db.cursor.fetchall()
    return data


def VisualizarClientes():
    db.cursor.execute('SELECT * FROM cliente')
    data = db.cursor.fetchall()
    return data

#FUNÇÕES DAS MOVIMENTAÇÕES


def AdicionarMovi(movimentacao):
    db.cursor.execute(f'INSERT INTO movimentacao(clienteMovi, tipoMovi, inicioDataMovi, horaInicioMovi, fimDataMovi, '
                      f'horaFimMovi) VALUES ("{movimentacao.clienteMovi}", "{movimentacao.tipoMovi}", '
                      f'"{movimentacao.inicioDataMovi}", "{movimentacao.horaInicioMovi}", "{movimentacao.fimDataMovi}",'
                      f' "{movimentacao.horaFimMovi}")')
    db.conexao.commit()


def SelecionarMovimentacao():
    db.cursor.execute('SELECT * FROM movimentacao')
    listaMovi = []

    for r in db.cursor.fetchall():
        listaMovi.append(Movimentacao.Movimentacao(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

    return listaMovi


def DadosMovi():
    db.cursor.execute(f'SELECT * FROM movimentacao')
    data = db.cursor.fetchall()
    return data


def idMovimentacao():
    db.cursor.execute('SELECT DISTINCT idMovi FROM movimentacao')
    data = db.cursor.fetchall()
    return data


def NomeMovimentacao():
    db.cursor.execute('SELECT DISTINCT clienteMovi FROM movimentacao')
    data = db.cursor.fetchall()
    return data


def GetIdMovimentacao(idMovi):
    db.cursor.execute(f'SELECT * FROM movimentacao WHERE idMovi = {idMovi}')
    data = db.cursor.fetchall()
    return data


def GetClienteMovimentacao(cliente):
    db.cursor.execute(f'SELECT * FROM movimentacao WHERE clienteMovi = "{cliente}"')
    data = db.cursor.fetchall()
    return data


def DadosMoviCliente(cliente):
    db.cursor.execute(f'SELECT * FROM movimentacao WHERE clienteMovi LIKE "{cliente}"')
    data = db.cursor.fetchall()
    return data


def UpdateMovimentacao(novoCliente, novoTipo, novaDataInicial, novaHoraInicial, novaDataFinal, novaHoraFinal, cliente, tipo, dataInicial, horaInicial, dataFinal, horaFinal):
    db.cursor.execute(f'UPDATE movimentacao SET clienteMovi = "{novoCliente}", tipoMovi = "{novoTipo}", inicioDataMovi = "{novaDataInicial}", horaInicioMovi = "{novaHoraInicial}", fimDataMovi = "{novaDataFinal}", horaFimMovi = "{novaHoraFinal}" WHERE clienteMovi = "{cliente}" AND tipoMovi = "{tipo}" AND inicioDataMovi = "{dataInicial}" AND horaInicioMovi = "{horaInicial}" AND fimDataMovi = "{dataFinal}" AND horaFimMovi = "{horaFinal}"')
    db.conexao.commit()
    data = db.cursor.fetchall()
    return data
