#from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
#from moviepy.editor import AudioFileClip,VideoFileClip,ImageClip,CompositeVideoClip,ImageClip
#import os
#resize(0.2)
#resize(0.30)

        #video = VideoFileClip('C:\\Users\\Lenovo\\Desktop\\video\\criativo.mp4').subclip(0,5).resize((791,1420)).set_pos(('center',273))
        #image = ImageClip("C:\\Users\\Lenovo\\Desktop\\video\\mold.png", duration=5).resize((1080,1920)).set_pos('center')
        #audio= AudioFileClip('C:\\Users\\Lenovo\\Desktop\\video\\criativo2.mp4').subclip(0,5)
        #compose = CompositeVideoClip([image,video])
        #compose.audio = audio



    #compose.write_videofile('teste.mp4')  #arquivo de saida <3 


from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from moviepy.editor import AudioFileClip,VideoFileClip,ImageClip,CompositeVideoClip,ImageClip

import os
import sys
import moviepy.editor as mpy

def converte(rede_social=None):
    if rede_social is None:
        return False

    if rede_social:
        path_ = os.path.dirname(os.path.abspath(__file__))
        arquivos = os.listdir(os.path.join(path_, 'videos'))
        arquivos_video = [arquivo for arquivo in arquivos if arquivo.lower().endswith('.mp4')]

        pasta_saida = os.path.join(path_, "imagens_convertida")
        os.makedirs(pasta_saida, exist_ok=True)

        for arquivo in arquivos_video:
            caminho_entrada = os.path.join(path_, 'videos', arquivo)
            video = mpy.VideoFileClip(caminho_entrada).resize((360, 640)).set_pos(('center', 273))
            tempo = video.duration

            _arquivos_ = os.path.join(path_, 'templetes')
            image = ImageClip(os.path.join(_arquivos_, f"{rede_social}.png"), duration=tempo).resize((640, 1280)).set_pos('center')

            audio = AudioFileClip(caminho_entrada)

            compose = mpy.CompositeVideoClip([image, video])
            compose.audio = audio

            os.chdir(pasta_saida)

            compose.write_videofile(f'video_{arquivos_video.index(arquivo) + 1}.mp4', codec="libx264", preset="fast", bitrate="1M", threads=32, fps=24)

            # audio.write_audiofile(f'audio_{arquivos_video.index(arquivo) + 1}.mp3')

            os.chdir(path_)  # Voltar para o diretório original após a conclusão do loop


name_arg = sys.argv[1]

if len(sys.argv) > 1:
    converte(rede_social=name_arg)
else:
    print('DIGITE UM NOME')