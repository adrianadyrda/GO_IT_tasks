import sys
import os
import glob
import shutil





format_dict = {
    'JPEG': 'images',
    'PNG': 'images',
    'JPG': 'images',
    'SVG': 'images',
    'DOC': 'documents',
    'DOCX': 'documents',
    'TXT': 'documents',
    'PDF': 'documents',
    'XLSX': 'documents',
    'PPTX': 'documents',
    'MP3': 'audio',
    'OGG': 'audio',
    'WAV': 'audio',
    'AMR': 'audio',
    'AVI': 'video',
    'MP4': 'video',
    'MOV': 'video',
    'MKV': 'video',
    'ZIP': 'archives',
    'RAR': 'archives',
    'GZ': 'archives',
    'TAR': 'archives'
}








def normalize(file_name):
    legend = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'h',
        'д': 'd',
        'е': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'y',
        'і': 'i',
        'ї': 'ji',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'kh',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ь': "'",
        'є': 'je',
        'ю': 'yu',
        'я': 'ya',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'Y',
        'I': 'I',
        'Ї': 'Yi',
        'Й': 'J',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'Kh',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ь': "'",
        'Є': 'Ye',
        'Ю': 'Yu',
        'Я': 'Ya',
    }
    for letter in file_name:
        if letter in legend:
            file_name = file_name.replace(letter, legend[letter])
        if not letter.isdigit() and not letter.isalpha():
            file_name = file_name.replace(letter, '_')
    return file_name


def innit_folders(path, folders):
    for folder in folders:
        dir = os.path.join(path, folder)
        if not os.path.exists(dir):
            os.mkdir(dir)


def collect_all_files(path):
    files = glob.glob(os.path.join(path, '**', '*'), recursive=True)
    return files


# def copy_files(files):
#     for file in files:
#         if os.path.isfile
#         format = file

def rename_file(file):
    file_name = file.split('\\')[-1]
    name,format = file_name.split('.')
    name = normalize(name)
    dir = file.split('\\')[:-1]
    dir = "\\".join(dir)
    new_file = os.path.join(dir, f'{name}.{format}')
    os.rename(file, new_file)
    return new_file


def unpack_archive(file, target_path):
    archive_name = file.split('\\')[-1]
    archive_name = archive_name.split('.')[0]
    target_path = os.path.join(target_path, archive_name)
    shutil.unpack_archive(file, target_path)
    os.remove(file)


def move_file(file, target_path):
    shutil.move(file, target_path)


def handle_file(file, path_to_trash):
    format = file.split('.')[-1]
    target = format_dict.get(format.upper())
    if target is not None:
        target_path = os.path.join(path_to_trash, target)
        if target == 'archives':
            unpack_archive(file, target_path)
        else:
            move_file(file, target_path)


def handle_dir(path_to_dir):
    files = collect_all_files(path_to_dir)
    if len(files) == 0:
        os.rmdir(path_to_dir)


def should_skip(file, target_folders):
    for folder in target_folders:
        if f'\\{folder}' in file:
            return True

def main(path):
    target_folders = ['images', 'documents', 'audio', 'video', 'archives']
    innit_folders(path, target_folders)
    files = collect_all_files(path)
    for file in files:
        if should_skip(file, target_folders):
            continue
        if os.path.isfile(file):
            file = rename_file(file)
            handle_file(file, path)
        else:
            handle_dir(file)


if __name__ == '__main__':
    main(sys.argv[1])