import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

picturelist = []
videolist = []
documentslist = []
musiclist = []
other_elements_list = []


document_ext = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls']
music_ext = ['mp3', 'ogg', 'wav', 'amr']
picture_ext = ['jpeg', 'png', 'jpg', 'psd']
video_ext = ['avi', 'mp4', 'mov']

all_list_ext = []

for element in files:
    new_element = element.split(".")

    if len(new_element) >= 2:
        all_list_ext.append(new_element[-1].lower())

        if new_element[1].lower() in picture_ext:
            picturelist.append(".".join(new_element))

        elif new_element[1].lower() in document_ext:
            documentslist.append(".".join(new_element))

        elif new_element[1].lower() in music_ext:
            musiclist.append(".".join(new_element))

        elif new_element[1].lower() in video_ext:
            videolist.append(".".join(new_element))

        else:
            other_elements_list.append(".".join(new_element))

    else:
        other_elements_list.append(".".join(new_element))


print("Picture list\n", picturelist)
print("Documents list\n", documentslist)
print("Video list\n", videolist)
print("Music list\n", musiclist)
print("Other elements list\n", other_elements_list)
print("All extensions\n", set(all_list_ext))