import pandas as pd

dados = {
    "Nome": ["Ana, Maria", "João", "Pedro", "Lucas", None],
    "Cidade": ["Londrina", "Maringá", "Londrina", None, "Cascavel"],
    "Idade": [18, 19, 18, 20, 19],
    "Nota": [8.5, 7.0, 9.0, 6.5, 8.0]
}

mauricio = {
    "nome": "Mauricio",
    "cabelo": "cacheado",
    "cor_do_cabelo": "castanho médio",
    "altura": "1.10m",
    "aura": 10000000,
    "idade": 17,
    "capital": "R$ 0,00"
}

df = pd.DataFrame(dados)
print(df)

#nomes das pessoas
pessoas = df['Nome']
print(f"\n {pessoas}")

#idades
idades = df['Idade']
print(f"\n{idades}")
