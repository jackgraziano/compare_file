from hashlib import md5
import requests
import time
import os

url = 'http://agentes.ons.org.br/download/pmo_decks_decomp/pmo_decks_decomp_preliminar/pmo_deck_preliminar.zip'
response = requests.get(url)
hash_inicial = md5()
hash_secundario = md5()




#Criação diretorio para download#

cdw = os.getcwd()
print('Este é local onde o arquivo .zip será baixado...', cdw)

dir = os.path.join(os.getcwd(),"download")
if not os.path.exists(dir):
    os.mkdir(dir)

#Download arquivo inicial#

with open('download/arquivo_inicial.zip', 'wb') as f:
    f.write(response.content)

with open('download/arquivo_inicial.zip', 'rb') as f:
    data = f.read()
    hash_inicial.update(data)

    print('Este é o hash do arquivo .zip', hash_inicial.hexdigest())

#Download novamente para comparação do hash#

with open('download/arquivo_inicial.zip', 'wb') as f:
    f.write(response.content)

with open('download/arquivo_inicial.zip', 'rb') as f:
    data=f.read()
    hash_secundario.update(data)


while hash_inicial.update(data) == hash_secundario.update(data):
    with open('download/arquivo_inicial.zip', 'wb') as f:
        f.write(response.content)

    with open('download/arquivo_inicial.zip', 'rb') as f:
        data = f.read()
        hash_secundario.update(data)

    print('Hash secundario igual ao inicial, arquivo não foi atualizado, nova tentativa de download em 10s...')
    time.sleep(10)


else:

    print('Hash_secundario diferente do inicial, arquivo teve atualização, fim do processo...')






