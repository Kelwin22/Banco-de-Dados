import streamlit as st
from datetime import datetime, timedelta
import mysql.connector

st.set_page_config(
    page_title="Locadora Digital - CineMengo",
    page_icon="🎬",
    layout="wide"
)

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234567kk",
        database="CineMengo"
    )

with st.sidebar:
    st.title("CineMengo 🎥")
    menu = st.radio("Navegação", ["Clientes", "Catálogo", "Aluguéis", "Recomendações"])

st.markdown("""
    <style>
        .main-header {
            text-align: center;
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    <div class="main-header">
        <h1>📽️ Bem-vindo à Locadora Digital CineMengo</h1>
        <p>O seu hub para gerenciar clientes, filmes e aluguéis!</p>
    </div>
""", unsafe_allow_html=True)

if menu == "Clientes":
    st.header("👥 Gerenciamento de Clientes")
    sub_menu = st.radio("Escolha uma opção:", ["Cadastrar Cliente", "Listar Clientes"], horizontal=True)

    if sub_menu == "Cadastrar Cliente":
        with st.form("Cadastro de Cliente", clear_on_submit=True):
            st.subheader("📋 Cadastrar Novo Cliente")
            nome = st.text_input("Nome Completo")
            endereco = st.text_input("Endereço")
            email = st.text_input("E-mail")
            forma_pagamento = st.selectbox("Forma de Pagamento", ["Cartão", "Pix", "Boleto"])
            submit = st.form_submit_button("Salvar")

            if submit:
                try:
                    conexao = conectar_banco()
                    cursor = conexao.cursor()
                    query = "INSERT INTO Cliente (nome, endereco, email, forma_pagamento) VALUES (%s, %s, %s, %s)"
                    cursor.execute(query, (nome, endereco, email, forma_pagamento))
                    conexao.commit()
                    st.success("✅ Cliente cadastrado com sucesso!")
                except Exception as e:
                    st.error(f"❌ Erro ao cadastrar cliente: {e}")
                finally:
                    if conexao:
                        conexao.close()

    elif sub_menu == "Listar Clientes":
        st.subheader("📋 Lista de Clientes")
        try:
            conexao = conectar_banco()
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM Cliente")
            clientes = cursor.fetchall()
            if clientes:
                st.table(clientes)
            else:
                st.info("Nenhum cliente cadastrado ainda.")
        except Exception as e:
            st.error(f"❌ Erro ao listar clientes: {e}")
        finally:
            if conexao:
                conexao.close()

elif menu == "Catálogo":
    st.header("🎞️ Gerenciamento de Catálogo")
    sub_menu = st.radio("Escolha uma opção:", ["Adicionar Filme", "Listar Filmes"], horizontal=True)

    if sub_menu == "Adicionar Filme":
        with st.form("Adicionar Filme", clear_on_submit=True):
            st.subheader("🎬 Adicionar Novo Filme")
            titulo = st.text_input("Título")
            ano = st.number_input("Ano de Lançamento", min_value=1900, max_value=datetime.now().year)
            duracao = st.number_input("Duração (minutos)", min_value=1)
            preco = st.number_input("Preço do Aluguel", min_value=0.0, format="%.2f")
            genero_id = st.number_input("ID do Gênero", min_value=1, step=1)
            submit = st.form_submit_button("Salvar")

            if submit:
                try:
                    conexao = conectar_banco()
                    cursor = conexao.cursor()
                    query = "INSERT INTO Filme (titulo, ano_lancamento, duracao, preco_aluguel, genero_id) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(query, (titulo, ano, duracao, preco, genero_id))
                    conexao.commit()
                    st.success("✅ Filme adicionado com sucesso!")
                except Exception as e:
                    st.error(f"❌ Erro ao adicionar filme: {e}")
                finally:
                    if conexao:
                        conexao.close()

    elif sub_menu == "Listar Filmes":
        st.subheader("📜 Lista de Filmes")
        try:
            conexao = conectar_banco()
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM Filme")
            filmes = cursor.fetchall()
            if filmes:
                st.table(filmes)
            else:
                st.info("Nenhum filme cadastrado ainda.")
        except Exception as e:
            st.error(f"❌ Erro ao listar filmes: {e}")
        finally:
            if conexao:
                conexao.close()

elif menu == "Aluguéis":
    st.header("📅 Gerenciamento de Aluguéis")
    cliente_id = st.number_input("ID do Cliente", min_value=1, step=1)
    tipo_conteudo = st.radio("Tipo de Conteúdo", ["Filme", "Série"], horizontal=True)
    conteudo_id = st.number_input(f"ID do {tipo_conteudo}", min_value=1, step=1)
    if st.button("Realizar Aluguel"):
        try:
            conexao = conectar_banco()
            cursor = conexao.cursor()
            data_aluguel = datetime.now()
            data_devolucao = data_aluguel + timedelta(days=2)
            query = "INSERT INTO Aluguel (cliente_id, filme_id, serie_id, data_aluguel, data_devolucao) VALUES (%s, %s, %s, %s, %s)"
            if tipo_conteudo == "Filme":
                cursor.execute(query, (cliente_id, conteudo_id, None, data_aluguel, data_devolucao))
            else:
                cursor.execute(query, (cliente_id, None, conteudo_id, data_aluguel, data_devolucao))
            conexao.commit()
            st.success("✅ Aluguel realizado com sucesso!")
        except Exception as e:
            st.error(f"❌ Erro ao realizar aluguel: {e}")
        finally:
            if conexao:
                conexao.close()

elif menu == "Recomendações":
    st.header("🤖 Recomendações Personalizadas")
    st.info("Em breve: sugestões baseadas no histórico de aluguéis!")
