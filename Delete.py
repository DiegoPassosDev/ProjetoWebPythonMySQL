import database as db


def ExcluirCliente(id):
    db.cursor.execute(f'DELETE FROM cliente WHERE idCont = {id}')
    db.conexao.commit()


def ExcluirMovimentacao(idMovi):
    db.cursor.execute(f'DELETE FROM movimentacao WHERE idMovi = {idMovi}')
    db.conexao.commit()