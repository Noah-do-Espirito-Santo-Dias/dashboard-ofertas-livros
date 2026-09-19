"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
from dados import ler_livros


def calcular_preco_medio(livros):
    """
    Calcula o preço médio dos livros na lista.
    return: Valor do preço médio.
    """
    if len(livros) == 0:
        return 0.0

    soma = 0.0
    for livro in livros:
        preco_texto = livro["preco"].replace("£", "")
        soma += float(preco_texto)

    return soma / len(livros)


def contar_cinco_estrelas(livros):
    """
    Conta quantos livros possuem avaliação de 5 estrelas.
    return: Quantidade de livros com 5 estrelas.
    """
    contador = 0
    for livro in livros:
        nota = str(livro["nota"]).strip()
        if nota == "Five" or nota == "5":
            contador += 1
    return contador


def encontrar_livro_mais_caro(livros):
    """
    Encontra o livro com o maior preço.
    return: Dicionário do livro mais caro ou None se a lista estiver vazia.
    """
    if len(livros) == 0:
        return None

    mais_caro = livros[0]
    maior_preco = float(mais_caro["preco"].replace("£", ""))

    for livro in livros:
        preco_atual = float(livro["preco"].replace("£", ""))
        if preco_atual > maior_preco:
            maior_preco = preco_atual
            mais_caro = livro

    return mais_caro


st.title("📚 Dashboard de Livros")

livros = ler_livros()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Livros", len(livros))

with col2:
    preco_medio = calcular_preco_medio(livros)
    st.metric("Preço Médio", f"£{preco_medio:.2f}")

with col3:
    qtd_cinco_estrelas = contar_cinco_estrelas(livros)
    st.metric("Livros (5 Estrelas)", qtd_cinco_estrelas)

with col4:
    livro_mais_caro = encontrar_livro_mais_caro(livros)
    if livro_mais_caro != None:
        preco = float(livro_mais_caro["preco"].replace("£", ""))
        st.metric("Mais Caro", f"£{preco:.2f}")
        st.caption(livro_mais_caro["titulo"])

st.dataframe(livros)