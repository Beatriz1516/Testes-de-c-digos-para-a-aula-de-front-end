import pandas as pd

dados = {
    "Nome": ["Ana", "Maria", "João", "Pedro", "Lucas"],
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
print("======= DATAFRAME =======")
print(df)

#estatísticas
print("\n=== ESTATÍSTICAS ===")
print("Média de notas: ", df['Nota'].mean())
print("Maior nota: ", df['Nota'].max())
print("Menor nota: ", df['Nota'].min())
print("Soma das notas: ", df['Nota'].sum())

#todos os cálculos base
print("\n=== DESCRIBE ===")
print(df.describe())

#nomes das pessoas
pessoas = df['Nome']
print(f"\n {pessoas}")

#idades
idades = df['Idade']
print(f"\n{idades}")
