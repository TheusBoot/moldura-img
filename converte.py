
from moviepy.editor import AudioFileClip, VideoFileClip, ImageClip, CompositeVideoClip
import os

def converte(rede_social=None):
    if rede_social is None:
        return False

    if rede_social in ['instagram', 'insta','pinterest','tiktok','whatssap','youtube']:
        path_ = os.path.dirname(os.path.abspath(__file__))
        arquivos = os.listdir(os.path.join(path_, 'videos'))
        arquivos_video = [arquivo for arquivo in arquivos if arquivo.lower().endswith('.mp4')]

        pasta_saida = os.path.join(path_, "imagens_convertida")
        os.makedirs(pasta_saida, exist_ok=True)

        for arquivo in arquivos_video:
            caminho_entrada = os.path.join(path_, 'videos', arquivo)
            video = VideoFileClip(caminho_entrada).resize((791, 1420)).set_pos(('center', 273))
            tempo = video.duration

            _arquivos_ = os.path.join(path_, 'templetes')
            image = ImageClip(os.path.join(_arquivos_, f"{rede_social}.png"), duration=tempo).resize((1080, 1920)).set_pos('center')

            audio = AudioFileClip(caminho_entrada)

            compose = CompositeVideoClip([image, video])
            compose.audio = audio

            os.chdir(pasta_saida)

            #compose.write_videofile(f'video_{arquivos_video.index(arquivo) + 1}.mp4')
            #compose.write_videofile(f'video_{arquivos_video.index(arquivo) + 1}.mp4', codec='libx264', audio_codec='aac')
            compose.write_videofile(f'video_{arquivos_video.index(arquivo) + 1}.mp4')

            #audio.write_audiofile(f'audio_{arquivos_video.index(arquivo) + 1}.mp3')

            os.chdir(path_)  # Voltar para o diretório original após a conclusão do loop


converte(rede_social="instagram")
