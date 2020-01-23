
import zipfile
import os
from os import listdir


# [ Limpa a pasta Removendo os Arquivos antigos ]
pasta = './_BASES/'
for arquivo in listdir(pasta):
    if '.txt'.lower() in arquivo.lower() or '.csv'.lower() in arquivo.lower() or '.zip'.lower() in arquivo.lower():

        print(arquivo)

        # [ Se necessario, Descompacta o Arquivo ]
        try:
            if '.zip'.lower() in str(arquivo).lower():
                with zipfile.ZipFile('./_BASES/'+str(arquivo), 'r') as zip_ref:
                    zip_ref.extractall('./_BASES')  # Extrai o Arquivo Descompactado para a Pasta Definida
                os.remove('./_BASES/'+str(arquivo))  # Exclui o Arquivo Compactado
                nomeNovoArquivo = str(arquivo).replace('.zip', '').replace('.Zip', '').replace('.ZIP', '')

        except Exception as E:
            print('Erro ao Descompactar o Arquivo.')
            print(str(E))
            continue

        print(nomeNovoArquivo)
