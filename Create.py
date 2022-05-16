import streamlit as st
import FuncoesDatabase as fdb
import Cliente as Cliente
import Movimentacao as Movimentacao


def AdicionarCliente():
    st.title('Adicionar Cliente')
    with st.form(key='adicionarCliente'):
        nomeCliente = st.text_input(label='Cliente').upper()
        numCont = st.text_input(label='Número do Contêiner', max_chars=11, help='4 - Letras e 7 - Números').upper()
        tipoCont = st.selectbox('Tipo', [20, 40])
        statusCont = st.selectbox('Status', ['CHEIO', 'VAZIO'])
        categoriaCont = st.selectbox('Categoria', ['IMPORTAÇÃO', 'EXPORTAÇÃO'])
        botaoEnviarCliente = st.form_submit_button('Adicionar Cliente')

        if botaoEnviarCliente:
            fdb.AdicionarCliente(Cliente.Cliente(0, nomeCliente, numCont, tipoCont, statusCont, categoriaCont))
            st.success('Cliente adicionado com sucesso!')


def AdicionarMovimentacao():
    hora = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    minutos = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16','17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
    hora2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '00']
    minutos2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16','17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '00']

    st.title('Adicionar Movimentação')
    with st.form(key='adicionarMovi'):
        listaCliente = [i[0] for i in fdb.NomeClientes()]
        seletorCliente = st.selectbox('Escolha o Cliente', listaCliente)
        nomeClienteMovi = fdb.getCliente(seletorCliente)
        if nomeClienteMovi:
            clienteMovi = nomeClienteMovi[0][1]

        tipoMovi = st.selectbox('Tipo Movimentação', ['EMBARQUE', 'DESCARGA', 'GATE IN', 'GATE OUT', 'REPOSICIONAMENT0', 'PESAGEM', 'SCANNER'])
        inicioDataMovi = st.date_input('Data do início da Movimentação')
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            inicioHora = st.selectbox('Hora', hora)
        with col2:
            inicioMinutos = st.selectbox('Minutos', minutos)

        fimDataMovi = st.date_input('Data do Fim da Movimentação')
        col4, col5, col6 = st.columns([1, 1, 3])
        with col4:
            fimHora = st.selectbox('Hora', hora2)
        with col5:
            fimMinutos = st.selectbox('Minutos', minutos2)

        okBotaoMovi = st.form_submit_button('Adicionar Movimentação')

        if okBotaoMovi:
            inicioTHora = inicioHora + ':' + inicioMinutos
            fimTHora = fimHora + ':' + fimMinutos
            fdb.AdicionarMovi(Movimentacao.Movimentacao(0, clienteMovi, tipoMovi, inicioDataMovi, inicioTHora, fimDataMovi, fimTHora))
            st.success('Movimentação adicionada com sucesso!')