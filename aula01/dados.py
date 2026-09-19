"""Leitura dos arquivos CSV do projeto.
"""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"


def ler_livros() -> list[dict]:
    """
    Lê o arquivo CSV de livros e retorna uma lista de dicionários.
    return: Lista contendo os dicionários com as informações de cada livro.
    """
    with open(CAMINHO_LIVROS, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


if __name__ == "__main__":
    livros = ler_livros()
    print(f"Total de livros lidos: {len(livros)}")
    if len(livros) > 0:
        print("Exemplo do primeiro livro:", livros[0])