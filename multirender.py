import os
import sys
import moviepy.editor as mpy
import numba
import threading

@numba.jit
def converte(rede_social=None,qt=2):
    if rede_social is None:
        return False

    if rede_social:
        path_ = os.path.dirname(os.path.abspath(__file__))
        arquivos = os.listdir(os.path.join(path_, 'videos'))
        arquivos_video = [arquivo for arquivo in arquivos if arquivo.lower().endswith('.mp4')]

        pasta_saida = os.path.join(path_, "imagens_convertida")
        os.makedirs(pasta_saida, exist_ok=True)

        with threading.ThreadPool(2) as pool:
            for arquivo in arquivos_video:
                caminho_entrada = os.path.join(path_, 'videos', arquivo)
                video = mpy.VideoFileClip(caminho_entrada).resize((791, 1420)).set_pos(('center', 273))
                tempo = video.duration

                _arquivos_ = os.path.join(path_, 'templetes')
                image = ImageClip(os.path.join(_arquivos_, f"{rede_social}.png"), duration=tempo).resize((1080, 1920)).set_pos('center')

                audio = AudioFileClip(caminho_entrada)

                compose = mpy.CompositeVideoClip([image, video])
                compose.audio = audio

                os.chdir(pasta_saida)

                pool.submit(compose.write_videofile, f'video_{arquivos_video.index(arquivo) + 1}.mp4', codec="libx264", preset="fast", bitrate="1M", threads=32, fps=24)

                os.chdir(path_)  # Voltar para o diretório original após a conclusão do loop


name_arg = sys.argv[1]

if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        th = sys.argv[2]
        converte(rede_social=name_arg,qt=th)
    
    else:
        
        converte(rede_social=nome_arg)
else:
    print('DIGITE UM NOME')
    print('Exemplo: python moldura.py story 2')
    print('ou python moldura.py story ')
