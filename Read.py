import pandas as pd
import streamlit as st
import FuncoesDatabase as fdb
import Delete as dt
import plotly.express as px


def ConsultarCliente():
    st.title('Dados dos Clientes')
    colunas = st.columns((1, 1, 1, 1, 1, 1, 1))
    campos = ['ID', 'Nome', 'Nº Contêiner', 'Tipo', 'Status', 'Categoria', 'Excluir']
    for col, campoNome in zip(colunas, campos):
        col.write(campoNome)
    for item in fdb.SelecionarClientes():
        col1, col2, col3, col4, col5, col6, col7= st.columns((1, 1, 1, 1, 1, 1, 1))
        col1.write(item.id)
        col2.write(item.clienteCont)
        col3.write(item.numCont)
        col4.write(item.tipoCont)
        col5.write(item.statusCont)
        col6.write(item.categoriaCont)
        botaoExcluir = col7.empty()
        clicarExcluir = botaoExcluir.button('Excluir', 'btnExcluir' + str(item.id))

        if clicarExcluir:
            dt.ExcluirCliente(item.id)
            botaoExcluir.button('Excluído', 'btnExcluir' + str(item.id))


def ConsultarMovimentacao():
    st.title('Dados das Movimentações')
    colunas = st.columns((0.5, 3, 3.5, 2, 2, 2, 2, 1))
    campos = ['ID', 'Cliente', 'Tipo Movimentação', 'Data Início', 'Hora Início', 'Data Fim', 'Hora Fim', 'Excluir']
    for col, campoNome in zip(colunas, campos):
        col.write(campoNome)
    for item in fdb.SelecionarMovimentacao():
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((0.5, 3, 3.5, 2.5, 2, 2.5, 2, 1))
        col1.write(item.idMovi)
        col2.write(item.clienteMovi)
        col3.write(item.tipoMovi)
        col4.write(item.inicioDataMovi)
        col5.write(item.horaInicioMovi)
        col6.write(item.fimDataMovi)
        col7.write(item.horaFimMovi)
        botaoExcluir = col8.empty()
        clicarExcluir = botaoExcluir.button('Excluir', 'btnExcluir' + str(item.idMovi))

        if clicarExcluir:
            dt.ExcluirMovimentacao(item.idMovi)
            botaoExcluir.button('Excluído', 'btnExcluir' + str(item.idMovi))



def Relatorios():
    resultado = fdb.VisualizarClientes()
    df_cliente = pd.DataFrame(resultado, columns=['Id', 'Nome', 'Número', 'Tipo', 'Status', 'Categoria'])

    with st.expander('Relatório de Movimentação'):
        listaMovimentacao = [i[0] for i in fdb.NomeMovimentacao()]
        selecionaCliente = st.selectbox('Escolha o Cliente', listaMovimentacao)
        resCliente = fdb.GetClienteMovimentacao(selecionaCliente)
        unicoCliente = resCliente[0][1]

        resC = fdb.DadosMoviCliente(unicoCliente)
        df_movimentacao = pd.DataFrame(resC, columns=['Id', 'Cliente', 'Tipo de Movimentação', 'Data Início', 'Hora Início', 'Data Fim', 'Hora Fim'])

        df_cli = df_movimentacao['Tipo de Movimentação'].value_counts().to_frame()
        df_cli = df_cli.reset_index()
        st.dataframe(df_cli)

        p1 = px.pie(df_cli, names='index', values='Tipo de Movimentação')
        st.plotly_chart(p1, use_container_width=True)


    with st.expander('Total de Importações/Exportações'):
        df_info = df_cliente['Categoria'].value_counts().to_frame()
        df_info = df_info.reset_index()
        st.dataframe(df_info)

        p2 = px.pie(df_info, names='index', values='Categoria')
        st.plotly_chart(p2, use_container_width=True)