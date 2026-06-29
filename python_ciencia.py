# Realizar a aplicação no google colab ou no python fiddle

import pandas as pd

varejo = [['Abacate', 'Abacaxi', 'Açaí', 'Acerola', 'Ameixa', 'Amora', 'Ananás', 'Atemoia', 'Avelã', 'Babaco',
    'Bacuí', 'Bacuri', 'Banana', 'Baru', 'Bergamota', 'Beringela', 'Bilimbi', 'Biribá', 'Buriti', 'Cacau',
    'Cagaita', 'Caju', 'Calamansi', 'Cambucá', 'Cambuci', 'Camu-camu', 'Carambola', 'Cariota', 'Castanha', 'Caviar-cítrico',
    'Cereja', 'Cidra', 'Ciriguela', 'Coco', 'Cranberry', 'Cupuaçu', 'Damasco', 'Dendê', 'Durião', 'Embaúba',
    'Figo', 'Framboesa', 'Fruta-pão', 'Gabiroba', 'Glicosmis', 'Goiaba', 'Granadilla', 'Groselha', 'Grumixama', 'Guabiju',
    'Guaraná', 'Guariroba', 'Ilama', 'Inajá', 'Ingá', 'Jabuticaba', 'Jaca', 'Jambo', 'Jambolão', 'Jaracatiá',
    'Jatobá', 'Jenipapo', 'Jerivá', 'Juçara', 'Kiwano', 'Kiwi', 'Laranja', 'Laranja-kinkan', 'Lichia', 'Lima',
    'Limão', 'Longan', 'Lucuma', 'Macaúba', 'Maçã', 'Mamão', 'Manga', 'Mangaba', 'Maracujá', 'Marang',
    'Marmelo', 'Melancia', 'Melão', 'Mirtilo', 'Morango', 'Murici', 'Nectarina', 'Nêspera', 'Noz', 'Pequi',
    'Pêra', 'Pêssego', 'Physalis', 'Pitanga', 'Pitaya', 'Romã', 'Tamarindo', 'Tangerina', 'Uva', 'Uvaia'], [ 7.50, 8.00, 14.00, 12.50, 16.00, 45.00, 9.50, 18.00, 65.00, 35.00,
    25.00, 30.00, 6.50, 55.00, 5.50, 6.00, 15.00, 20.00, 12.00, 15.00,
    18.00, 12.00, 28.00, 40.00, 22.00, 35.00, 11.00, 30.00, 40.00, 180.00,
    60.00, 9.00, 14.00, 5.00, 75.00, 16.50, 50.00, 8.00, 90.00, 20.00,
    25.00, 80.00, 12.00, 22.00, 30.00, 7.00, 38.00, 55.00, 35.00, 28.00,
    25.00, 15.00, 45.00, 10.00, 12.00, 14.00, 25.00, 16.00, 15.00, 26.00,
    14.00, 11.00, 10.00, 16.00, 35.00, 19.50, 5.00, 28.00, 22.00, 9.00,
    6.00, 45.00, 50.00, 12.00, 10.00, 8.50, 7.50, 18.00, 10.50, 60.00,
    16.00, 3.50, 7.00, 90.00, 28.00, 16.00, 15.00, 19.00, 50.00, 15.00,
    12.00, 14.00, 65.00, 20.00, 22.00, 25.00, 12.00, 6.00, 13.00, 24.00], ["Sudeste", "Nordeste", "Norte", "Nordeste", "Sul", "Sul", "Nordeste", "Sudeste", "Sul", "Sul",
    "Norte", "Norte", "Nordeste", "Centro-Oeste", "Sul", "Sudeste", "Nordeste", "Norte", "Norte", "Nordeste",
    "Centro-Oeste", "Nordeste", "Sudeste", "Sudeste", "Sudeste", "Norte", "Sudeste", "Norte", "Norte", "Sudeste",
    "Sul", "Sudeste", "Nordeste", "Nordeste", "Sul", "Norte", "Sul", "Nordeste", "Sudeste", "Sudeste",
    "Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Sudeste", "Sudeste", "Sudeste", "Sul", "Sudeste", "Sul",
    "Norte", "Centro-Oeste", "Sudeste", "Norte", "Norte", "Sudeste", "Nordeste", "Sudeste", "Sudeste", "Sudeste",
    "Centro-Oeste", "Nordeste", "Sul", "Sudeste", "Sudeste", "Sul", "Sudeste", "Sudeste", "Sudeste", "Sudeste",
    "Sudeste", "Sudeste", "Sul", "Cerrado", "Sul", "Nordeste", "Sudeste", "Nordeste", "Sudeste", "Sudeste",
    "Sudeste", "Nordeste", "Nordeste", "Sul", "Sul", "Norte", "Sul", "Sudeste", "Sul", "Centro-Oeste",
    "Sul", "Sul", "Sudeste", "Sudeste", "Centro-Oeste", "Sudeste", "Nordeste", "Sul", "Sul", "Sudeste"] ]


# Transformação da lista de varejo em um Data Frame
df_varejo = pd.DataFrame({
    "Frutas": varejo[0],
    "Preço_kilo": varejo[1],
    "Regiao": varejo[2]
})
print(df_varejo)

# visualizar por coluna
df_varejo ['Regiao']

# visualizar os cinco primeiros
df_varejo.head()