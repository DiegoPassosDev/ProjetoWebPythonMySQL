import streamlit as st
import FuncoesDatabase as fdb
import pandas as pd


def EditarCliente():
    st.subheader('Editar Cliente')

    listaCliente = [i[0] for i in fdb.NomeClientes()]
    seletorCliente = st.selectbox('Escolha o Cliente', listaCliente)
    resultado = fdb.getCliente(seletorCliente)


    if resultado:
        clienteCont = resultado[0][1]
        numCont = resultado[0][2]
        tipoCont = resultado[0][3]
        statusCont = resultado[0][4]
        categoriaCont = resultado[0][5]

        col1, col2 = st.columns([2, 1])

        with col1:
            alterarClienteCont = st.text_input('Cliente', clienteCont).upper()
            alterarNumCont = st.text_input('Número do Contêiner', numCont, max_chars=11, help='4 - Letras e 7 - Números').upper()
            alterarTipoCont = st.selectbox('Tipo', [20, 40])
            alterarStatusCont = st.selectbox('Status', ['CHEIO', 'VAZIO'])
            alterarCategoriaCont = st.selectbox('Categoria', ['IMPORTAÇÃO', 'EXPORTAÇÃO'])

            if st.button('Alterar Dados'):
                fdb.EditarCliente(alterarClienteCont, alterarNumCont, alterarTipoCont, alterarStatusCont, alterarCategoriaCont, clienteCont, numCont, tipoCont, statusCont, categoriaCont)
                st.success('Dados editados com sucesso!')


def EditarMovimentacao():
    hora = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23']
    minutos = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
               '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
               '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
               '51', '52', '53', '54', '55', '56', '57', '58', '59']
    hora2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
             '19', '20', '21', '22', '23', '00']
    minutos2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
                '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51',
                '52', '53', '54', '55', '56', '57', '58', '59', '00']

    st.subheader('Editar Movimentação')
    with st.expander('Listagem de Movimentações'):
        resultado = fdb.DadosMovi()
        df_movi = pd.DataFrame(resultado, columns=['ID', 'Cliente', 'Tipo Movimentação', 'Início', 'Hora Início', 'Término', 'Hora Fim'])
        st.dataframe(df_movi)

        listaMovimentacao = [i[0] for i in fdb.idMovimentacao()]
        selecionarIdMovi = st.selectbox('Escolha a Movimentação', listaMovimentacao)
        resuldadoIdMovi = fdb.GetIdMovimentacao(selecionarIdMovi)

    if resuldadoIdMovi:
        clienteMovi = resuldadoIdMovi[0][1]
        tipoMovi = resuldadoIdMovi[0][2]
        inicioDataMovi = resuldadoIdMovi[0][3]
        horaInicioMovi = resuldadoIdMovi[0][4]
        fimDataMovi = resuldadoIdMovi[0][5]
        horaFimMovi = resuldadoIdMovi[0][6]

        colA, colB = st.columns([1, 1])
        colC, colD, colE = st.columns([1, 1, 6])

        with colA:
            listaCliente = [i[0] for i in fdb.NomeClientes()]
            seletorCliente = st.selectbox('Escolha o Cliente', listaCliente)
            resultado = fdb.getCliente(seletorCliente)

            if resultado:
                alterarClienteMovi = resultado[0][1]
            alterarTipoMovi = st.selectbox('Tipo Movimentação', ['EMBARQUE', 'DESCARGA', 'GATE IN', 'GATE OUT', 'REPOSICIONAMENT0', 'PESAGEM', 'SCANNER'])
            alterarDataInicioMovi = st.date_input('Data do início da Movimentação')
            with colC:
                alterarHoraI_Mov = st.selectbox('Hora', hora)

            with colD:
                alterarMinutosI_Mov = st.selectbox('Minutos', minutos)

        alterarDataFimMovi = st.date_input('Data do Fim da Movimentação')
        colF, colG, colH = st.columns([1, 1, 6])
        with colF:
            alterarHoraF_Mov = st.selectbox('Hora', hora2)
        with colG:
            alterarMinutosF_Mov = st.selectbox('Minutos', minutos2)

        if st.button('Alterar Movimentação'):
            alterarTotalHoraInicialMovi = alterarHoraI_Mov + ':' + alterarMinutosI_Mov
            alterarTotalHoraFimMovi = alterarHoraF_Mov + ':' + alterarMinutosF_Mov
            fdb.UpdateMovimentacao(alterarClienteMovi, alterarTipoMovi, alterarDataInicioMovi, alterarTotalHoraInicialMovi, alterarDataFimMovi, alterarTotalHoraFimMovi, clienteMovi, tipoMovi, inicioDataMovi, horaInicioMovi, fimDataMovi, horaFimMovi)
            st.success('Movimentação alterada com sucesso!')