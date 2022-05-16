import streamlit as st
import Create as ct
import Read as rd
import Update as up

st.sidebar.title('Menu')
opc = st.sidebar.selectbox('Controle', ['Cliente - Adicionar', 'Cliente - Consultar/Excluir', 'Cliente - Editar',
                                        'Movimentação - Adicionar', 'Movimentação - Consultar/Excluir',
                                        'Movimentação - Editar', 'Relatórios'])

if opc == 'Cliente - Adicionar':
    ct.AdicionarCliente()

elif opc == 'Cliente - Consultar/Excluir':
    rd.ConsultarCliente()

elif opc == 'Cliente - Editar':
    up.EditarCliente()

elif opc == 'Movimentação - Adicionar':
    ct.AdicionarMovimentacao()

elif opc == 'Movimentação - Consultar/Excluir':
    rd.ConsultarMovimentacao()

elif opc == 'Movimentação - Editar':
    up.EditarMovimentacao()

elif opc == 'Relatórios':
    rd.Relatorios()