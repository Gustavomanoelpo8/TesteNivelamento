import tabula
import pandas as pd
import csv
import zipfile
import os

pdfPath=r'C:\Users\Jason\Desktop\programas\TesteveNivelamento\extract\\pdf_1.pdf'
zipName = 'Teste_Gustavo'

table = tabula.read_pdf(pdfPath, pages= '3-181', encoding='utf-8', pandas_options={'header':None})
df = pd.concat(table)

df.rename(columns={
    0: 'Seg. Odontológica',
    1: 'Seg. Ambulatorial',
    2: 'Seg. Hospitalar Com Obstetrícia',
    3: 'Seg. Hospitalar Sem Obstetrícia',
    4: 'Plano Referência',
    5: 'Procedimento de Alta Complexidade',
    6: 'Diretriz de Utilização'
}, inplace=True)

csvName = 'dados.csv'
df.to_csv(csvName, index=False, encoding='utf-8-sig')


with zipfile.ZipFile(f'{zipName}.zip', 'w') as zipf:
    zipf.write(csvName)

os.remove(csvName)
