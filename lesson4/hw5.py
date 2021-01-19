import os
import sys
from pathlib import Path


images_list = ('.jpeg', '.png', '.jpg' ,'.svg')
video_list = ('.avi', '.mp4', '.mov', '.mkv')
documents_list = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
music_list = ('.mp3', '.ogg', '.wav', '.amr')
archive_list = ('.zip', '.gz', '.tar')


a = Path()

images = []
video = []
documents = []
music = []
archive = []
unknown = []
unique = set()

unique_list = list(unique)


def check_file(path):

    for file in path.iterdir():
        if file.suffix in images_list:
            images.append(file.name)

        elif file.suffix in video_list:
            video.append(file.name)

        elif file.suffix in documents_list:
            documents.append(file.name)

        elif file.suffix in music_list:
            music.append(file.name)

        elif file.suffix in archive_list:
            archive.append(file.name)

        elif file.is_dir():
           check_file(file)

        else:
            unknown.append(file.name)

        if file.suffix:
            unique.add(file.suffix)

check_file(a)





print(f'''images: {images} ; videos: {video} ;
documents: {documents} ; music: {music} ;
archive: {archive} ; unknown: {unknown} ;''')
print(f'''unique files: {unique_list}''') 