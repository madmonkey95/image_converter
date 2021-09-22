from PIL import Image # image library for Python

import glob # for path standardization

import time, sys

def loading():
    loadingText = 'Converting...'
    print(loadingText[:-3], end='', flush=True)
    for i in loadingText[-3:]:
        time.sleep(.5)
        print(i, end='', flush=True)
    print()

def program():
    print('~~~ RUN THIS SCRIPT FROM THE DIRECTORY CONTAINING IMAGES YOU WANT TO CONVERT ~~~' + '\n'*10)
    ext = input('File extension to search for - do not include the dot (ex. "png"): ').lower()
    newExt = input('File extension to convert to - do not include the dot (ex. "png"):  ').lower()
    type = ext
    newType = newExt

    while True:
        try:
            qlty = int(input('Specify conversion quality, recommended 80+, enter integer: '))
            break
        except ValueError:
            print('Must be an integer.')
            continue

    matches = glob.glob(f'*.{type}')

    print('Found the following matches for ' + type + ' in current directory...')
    print(' '.join(matches))

    while True:
        print('Continue conversion to ' + newType + '?')
        confirm = input('Y/N: ').lower()

        if confirm == 'y' or confirm == 'yes': break
        else: sys.exit()


    for file in matches:
        img = Image.open(file)
        imgRgb = img.convert('RGB')
        imgRgb.save(file.replace(type, newType), quality=qlty)

    loading()

    print('Converted files succesfully...')
    matches = glob.glob(f'*.{newType}')
    print(' '.join(matches))


if __name__ == '__main__':
    program()


    