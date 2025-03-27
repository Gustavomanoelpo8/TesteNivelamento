import requests
import zipfile
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

extrair = requests.get(url)
extrair.raise_for_status()

soup = BeautifulSoup(extrair.text, 'html.parser')
pdfExtract = [a for a in soup.find_all('a', class_='internal-link', href=True) if a['href'].endswith('.pdf')]
pdfExtract = pdfExtract[:2]

with zipfile.ZipFile('teste.zip', 'w') as zipf:
    for i, link in enumerate(pdfExtract, start=1):
        pdfUrl = urljoin(url, link['href'])
        pdfResponse = requests.get(pdfUrl)
        pdfResponse.raise_for_status()
        
        
        filename = f'pdf_{i}.pdf'
        zipf.writestr(filename, pdfResponse.content)