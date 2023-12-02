import os

path_ = os.path.dirname(os.path.abspath(__file__))

pasta = 'videos'  # Substitua pelo caminho da sua pasta

# Lista todos os arquivos na pasta
arquivos = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]

# Filtra os arquivos .mp4
arquivos_mp4 = [f for f in arquivos if f.endswith('.mp4')]

# Ordena os arquivos em ordem crescente
arquivos_mp4.sort()

# Renomeia os arquivos em ordem crescente
for i, arquivo in enumerate(arquivos_mp4, start=1):
    novo_nome = f'video_{i:03d}.mp4'  # Formata o nome do arquivo com três dígitos e extensão .mp4
    caminho_antigo = os.path.join(pasta, arquivo)
    caminho_novo = os.path.join(pasta, novo_nome)

    # Renomeia o arquivo
    os.rename(caminho_antigo, caminho_novo)

print('Renomeação concluída.')
