import os
import shutil

GENERAL = ''

all_types = ['images', 'documents', 'videos', 'audios', 'archives']
image_type = ['.jpg', '.png', '.jpeg']
video_type = ['.avi', '.mp4', '.mov']
doc_type = ['.pdf', '.docx', '.txt', '.xlsx']
music_type = ['.mp3', '.ogg', '.wav', '.amr']
archives = ['.zip', '.7zip', '.gz', '.tar']


def normalize(string):


    alphabet = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('є'): 'ye', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y',
                  ord('і'): 'i', ord('ї'): 'yi', ord('й'): 'y', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r',
                  ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh', ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ю'): 'yu',
                  ord('я'): 'ya', ord('ы'): 'y', ord('э'): 'e', ord('ё'): 'yo', ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E',
                  ord('Є'): 'Ye', ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y', ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y', ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M',
                  ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'Kh', ord('Ц'): 'Ts',
                  ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch', ord('Ю'): 'Yu', ord('Я'): 'Ya', ord('Ы'): 'Y', ord('Э'): 'E', ord('Ё'): 'Yo'}

    list_N = []

    normalized = ''

    for c in string:
        if not c.isalpha() and not c.isdigit():
            c = '_'
            list_N.append(c)
        else:
            c = c.translate(alphabet)
            list_N.append(c)
    return normalized.join(list_N)


def create_folders():
    for name in all_types:
        directory = os.path.join(GENERAL, name)
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)


def relocateFile(filesInfo):

    create_folders()

    info = filesInfo.split(";")

    src = os.path.join(info[1], info[2]+info[3])

    dest = os.path.join(GENERAL, info[0], normalize(info[2])+info[3])

    if info[0] == 'archives':
        shutil.unpack_archive(shutil.move(src, dest),
                              os.path.join(GENERAL, info[0]))
        os.remove(dest)

    else:
        shutil.move(src, dest)
    try:
        os.rmdir(info[1])
    except OSError:
        pass


def fileDistribute(fileCollections, path, nestingDeep):

    for file in fileCollections:
        fileName, fileExtension = os.path.splitext(file)
        if fileExtension in image_type:
            relocateFile(f'images;{path};{fileName};{fileExtension}')
        elif fileExtension in video_type:
            relocateFile(f'videos;{path};{fileName};{fileExtension}')
        elif fileExtension in doc_type:
            relocateFile(f'documents;{path};{fileName};{fileExtension}')
        elif fileExtension in music_type:
            relocateFile(f'audios;{path};{fileName};{fileExtension}')
        elif fileExtension in archives:
            relocateFile(f'archives;{path};{fileName};{fileExtension}')


def grabPath(path, nestingDeep=0):
    fileCollections = []
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            grabPath(os.path.join(path, file), nestingDeep + 1)
        else:
            fileCollections.append(file)
    fileDistribute(fileCollections, path, nestingDeep)


def main():

    global GENERAL
    GENERAL = r'D:/junk/'
    grabPath(r'D:/junk/')


if __name__ == '__main__':
    main()