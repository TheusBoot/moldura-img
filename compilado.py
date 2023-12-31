import os
import sys
import moviepy.editor as mpy
import numba

from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


@numba.jit
def concatena_videos_na_pasta(pasta_entrada, video_saida):
    # Lista todos os arquivos na pasta de entrada
    arquivos = sorted(os.listdir(pasta_entrada))

    # Lista para armazenar objetos de vídeo
    clips = []

    # Loop através de cada arquivo na pasta
    for arquivo in arquivos:
        # Verifica se o arquivo é um vídeo
        if arquivo.endswith(('.mp4', '.avi', '.mov')):
            # Cria o caminho completo para o arquivo de vídeo
            caminho_video = os.path.join(pasta_entrada, arquivo)

            # Adiciona o vídeo à lista de clips
            clip = VideoFileClip(caminho_video)
            clips.append(clip)

    # Concatena todos os vídeos
    video_final = concatenate_videoclips(clips, method="compose")

    # Salva o vídeo final
    video_final.write_videofile(video_saida, codec="libx264", fps=24,preset="fast",threads=32, bitrate="1M")

if __name__ == "__main__":
    # Especifique a pasta de entrada e o nome do arquivo de saída
    pasta_entrada = r"videos"
    video_saida = r"imagens_convertida/video_final.mp4"

    # Chama a função para concatenar os vídeos
    concatena_videos_na_pasta(pasta_entrada, video_saida)





