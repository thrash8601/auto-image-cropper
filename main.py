import os
from PIL import Image


def is_img_file(file_dir):
    return file_dir.endswith('png') or file_dir.endswith('jpg') or file_dir.endswith('jpeg')


def get_img_files():
    files = os.listdir('in')
    ret = []
    for file in files:
        if is_img_file(os.path.join('in', file)):
            ret.append(os.path.join('in', file))
    return ret


def get_file_name(file_path):
    return file_path.split(os.sep)[-1]


def crop_image(img_path):
    img = Image.open(img_path)
    img2 = img.crop((0, 0, img.width, img.height - 125))
    img2.save(os.path.join('out', get_file_name(img_path)))


def run():
    img_files = get_img_files()
    print(img_files)

    for img in img_files:
        filename = img.split('/')[-1]
        print('Processing ' + filename + '...')
        crop_image(img)


run()
