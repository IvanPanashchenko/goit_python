import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

pictures = []
video = []
documents = []
music = []
other_elements_list = []


documents = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls']
music = ['mp3', 'ogg', 'wav', 'amr']
picture = ['jpeg', 'png', 'jpg', 'psd']
video = ['avi', 'mp4', 'mov']

all_list = []

for element in files:
    new_element = element.split(".")

    if len(new_element) >= 2:
        all_list.append(new_element[-1].lower())

        if new_element[1].lower() in picture:
            pictures.append(".".join(new_element))

        elif new_element[1].lower() in documents:
            documents.append(".".join(new_element))

        elif new_element[1].lower() in music:
            music.append(".".join(new_element))

        elif new_element[1].lower() in video:
            video.append(".".join(new_element))

        else:
            other_elements_list.append(".".join(new_element))

    else:
        other_elements_list.append(".".join(new_element))


print("Picture list\n", pictures)
print("Documents list\n", documents)
print("Video list\n", video)
print("Music list\n")
print("Other elements list\n", other_elements_list)
print("All extensions\n", set(all_list))