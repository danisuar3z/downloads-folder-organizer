# -*- coding: utf-8 -*-

# downloads_folder.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Clean Downloads folder project

'''

'''

import os

from my_input import my_input

IMG_EXTENSIONS = ['png', 'jpg', 'peg', 'gif',]
DOC_EXTENSIONS = ['pdf', 'doc', 'ocx', 'ppt', 'ptx', 'des', 'eet',]
DAT_EXTENSIONS = ['txt', 'csv', 'lsx', 'xls',]
MED_EXTENSIONS = ['mp4', 'mp3', 'wma', 'wav', 'mkv',]
SCR_EXTENSIONS = ['.py', 'ynb', 'aml', 'js', 'son', 'bat', 'css',]
SET_EXTENSIONS = ['exe', 'msi']
ZIP_EXTENSIONS = ['zip', 'rar',]

_home  = os.path.expanduser('~')
_downloads = os.path.join(_home, 'downloads')


def make_dirs():
    os.mkdir('processed')
    os.mkdir(os.path.join('processed', 'imgs'))
    os.mkdir(os.path.join('processed', 'docs'))
    os.mkdir(os.path.join('processed', 'data'))
    os.mkdir(os.path.join('processed', 'media'))
    os.mkdir(os.path.join('processed', 'scripts'))
    os.mkdir(os.path.join('processed', 'setups'))
    os.mkdir(os.path.join('processed', 'zip-rars'))


def process_downloads_file(item, folder, subfolder=False, subf_name=None):
    if subfolder:
        os.rename(
            os.path.join(_downloads, subf_name, item),
            os.path.join(_downloads, 'processed', folder, item)
            )        
    else:
        os.rename(
            os.path.join(_downloads, item),
            os.path.join(_downloads, 'processed', folder, item)
            )


def process_downloads_folder():
    items_moved = 0
    for item in os.listdir(_downloads):
        if os.path.isdir(item):
            continue
        if item[-3:] in IMG_EXTENSIONS:
            process_downloads_file(item, 'imgs')
            items_moved += 1
        if item[-3:] in DOC_EXTENSIONS:
            process_downloads_file(item, 'docs')
            items_moved += 1
        if item[-3:] in DAT_EXTENSIONS:
            process_downloads_file(item, 'data')
            items_moved += 1
        if item[-3:] in MED_EXTENSIONS:
            process_downloads_file(item, 'media')
            items_moved += 1
        if item[-3:] in SCR_EXTENSIONS:
            process_downloads_file(item, 'scripts')
            items_moved += 1
        if item[-3:] in SET_EXTENSIONS:
            process_downloads_file(item, 'setups')
            items_moved += 1
        if item[-3:] in ZIP_EXTENSIONS:
            process_downloads_file(item, 'zip-rars')
            items_moved += 1
    print(f'{items_moved} items moved.')


def process_actual_folder():
    items_moved = 0
    for item in os.listdir('.'):
        if os.path.isdir(item):
            continue
        if item[-3:] in IMG_EXTENSIONS:
            os.rename(item, os.path.join('processed', 'imgs', item))
            items_moved += 1
        if item[-3:] in DOC_EXTENSIONS:
            os.rename(item, os.path.join('processed', 'docs', item))
            items_moved += 1
        if item[-3:] in DAT_EXTENSIONS:
            os.rename(item, os.path.join('processed', 'data', item))
            items_moved += 1
        if item[-3:] in MED_EXTENSIONS:
            os.rename(item, os.path.join('processed', 'media', item))
            items_moved += 1
        if item[-3:] in SCR_EXTENSIONS:
            os.rename(item, os.path.join('processed', 'scripts', item))
            items_moved += 1
        if item[-3:] in SET_EXTENSIONS:
            os.rename(item, os.path.join('processed', 'setups', item))
            items_moved += 1
        if item[-3:] in ZIP_EXTENSIONS:
            os.rename(item, os.path.join('processed', 'zip-rars', item))
            items_moved += 1
    print(f'{items_moved} items moved.')


def process_downloads_subfolder(subfolder):
    '''
    ONLY ONE LEVEL
    '''
    items_moved = 0
    for item in os.listdir(os.path.join(_downloads, subfolder)):
        if os.path.isdir(item):
            continue
        if item[-3:] in IMG_EXTENSIONS:
            process_downloads_file(item, 'imgs',
                                   subfolder=True, subf_name=subfolder)
            items_moved += 1
        if item[-3:] in DOC_EXTENSIONS:
            process_downloads_file(item, 'docs',
                                   subfolder=True, subf_name=subfolder)
            items_moved += 1
        if item[-3:] in DAT_EXTENSIONS:
            process_downloads_file(item, 'data',
                                   subfolder=True, subf_name=subfolder)
            items_moved += 1
        if item[-3:] in MED_EXTENSIONS:
            process_downloads_file(item, 'media',
                                   subfolder=True, subf_name=subfolder)
            items_moved += 1
        if item[-3:] in SCR_EXTENSIONS:
            process_downloads_file(item, 'scripts',
                                   subfolder=True, subf_name=subfolder)
            items_moved += 1
        if item[-3:] in SET_EXTENSIONS:
            process_downloads_file(item, 'setups',
                                   subfolder=True, subf_name=subfolder)
            items_moved += 1
        if item[-3:] in ZIP_EXTENSIONS:
            process_downloads_file(item, 'zip-rars',
                                   subfolder=True, subf_name=subfolder)
            items_moved += 1
    print(f'{items_moved} items moved.')


def main():
    print(
        f'\n{"*"*67}\n'
        f'{"| Welcome to the Downloads Folder organizer. To exit press ctrl+c.|":67}'
        f'\n{"| What do you want to do?":66}{"|":>}'
        f'\n{"| 1- Process Downloads folder":65}{" |":>}\n'
        f'{"| 2- Process a Downloads subfolder":65}{" |":>}\n'
        f'{"| 3- Process current folder: "}{os.getcwd():37}{"|":>}\n'
        f'{"*"*67}\n'
        f'{"by Dani Suarez":>67}')
    ans = my_input('Type an option: ', ['1', '2', '3'])
    
    if ans == '1':  # Process Downloads folder
        dirs = my_input('Do you already have the subfolders processed/ and'
                 ' imgs/docs/etc? [y/n]', ['y', 'n'])
        if dirs.lower() == 'n':
            os.chdir(_downloads)
            make_dirs()
        print('Processing...')
        process_downloads_folder()
   
    elif ans == '2':  # Process a Downloads subfolder
        dirs = my_input('Do you already have the subfolders processed/ and'
                 ' imgs/docs/etc? [y/n]', ['y', 'n'])
        if dirs.lower() == 'n':
            os.chdir(_downloads)
            make_dirs()
        subfolder = input('What\'s the exact name of the subfolder?')
        print('Processing...')
        process_downloads_subfolder(subfolder)

    elif ans == '3':  # Process current folder
        dirs = my_input('Do you already have the subfolders processed/ and'
                 ' imgs/docs/etc? [y/n]', ['y', 'n'])
        if dirs.lower() == 'n':
            make_dirs()        
        print('Processing...')
        process_actual_folder()


if __name__ == '__main__':
    main()


'''
Add zip/rar
Improve extension reading, maybe with split method.
Change multiple conditionals for dictionary.
'''
