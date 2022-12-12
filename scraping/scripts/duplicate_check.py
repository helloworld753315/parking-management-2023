import os
import shutil
from PIL import Image
import imagehash
import numpy as np
from dotenv import load_dotenv


def check_size(image_path, width, height):
    im = Image.open(image_path)
    w, h = im.size
    if w < width and h < height:
        return True
    else:
        return False


def duplicate_check(import_images_path, export_image_path):
    image_files = []
    duplicate_image_combinations = []
    f = [os.path.join(import_images_path, path) for path in os.listdir(import_images_path)]
    for i in f:
        if i.endswith('.jpg') or i.endswith('.png'):
            image_files.append(i)

    duplicated_count = 0
    imgs = {}
    for img in sorted(image_files):
        hash = imagehash.average_hash(Image.open(img))
        if hash in imgs:
            # print('Similar image :', img, imgs[hash])
            duplicate_image_combinations.append([img, imgs[hash]])
            shutil.move(img, export_image_path)
            duplicated_count += 1
        else:
            imgs[hash] = img
    
    print(f'重複数: {duplicated_count}件')


def make_dir(path):
    """
    envに指定したフォルダを作成

    Parameters
    ----------
    import_path : str
        importするファイルのパス
    fixed_text_path : str
        修正したtxtファイルを出力するパス
    """
    os.makedirs(path, exist_ok=True)
        


def main():
    load_dotenv()
    import_images_path = os.environ['SAVE_DIR']
    moving_target_path = f'data/images/google/tmp'
    make_dir(moving_target_path)
    duplicate_check(import_images_path, moving_target_path)

if __name__ == "__main__":
    main()


