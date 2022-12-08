import glob
from dotenv import load_dotenv
import os
import shutil

# データセットの配分を計算 : 0.6, 0.2, 0.2のように全体が1になるよう指定
def calc_rate(images, train, test, val):
    images_len = len(images)
    train_lens = int(images_len * train) # trainの画像枚数
    test_lens = int(images_len * test) # testの画像枚数
    val_lens = int(images_len * val) # valの画像枚数
    print(f'画像ファイル数: {images_len}\n配分: {train_lens} {test_lens} {val_lens}')
    train_lens += (images_len - train_lens - test_lens - val_lens)

    return {"train_lens": train_lens, "test_lens": test_lens, "val_lens": val_lens}

# envに指定したフォルダを作成
def make_dir(dataset_path):
    os.makedirs(f'./datasets', exist_ok=True)
    os.makedirs(f'./tmp/{dataset_path}/train', exist_ok=True)
    os.makedirs(f'./tmp/{dataset_path}/test', exist_ok=True)
    os.makedirs(f'./tmp/{dataset_path}/val', exist_ok=True)


# リストを結合して文字列に文字列に変換
def list_to_string(li):
    return "/".join(li)


# 必要なファイルをコピーする
def remove(import_text_path, import_image_path, export_path):
    # 画像ファイル
    images = glob.glob(f'{import_image_path}/*.*')
    '''
    # txtファイル
    txtes = glob.glob(f'{import_text_path}/fixed_labels/**/*[.txt]')
    '''

    # データセットの配分
    datasets_rate = calc_rate(images, 0.8, 0, 0.2)

    # train/test/val
    train = []
    test = []
    val = []

    
    for count in range(len(images)):
        # name = image.split("/")[-1].split(".")[0]
        if count < datasets_rate["train_lens"]:
            train.append(images[count])
        elif count < datasets_rate["train_lens"] + datasets_rate["test_lens"]:
            test.append(images[count])
        else:
            val.append(images[count])

    # train/test/valにコピー
    print("train作成...")
    for image in train:
        input_text_path = f'{import_text_path}/fixed_labels/{image.split("/")[-1].split(".")[0]}.txt'
        output_image_path = f'./tmp/{export_path}/train'
        output_text_path = f'./tmp/{export_path}/train'
        shutil.copy(image, output_image_path)
        try:
            shutil.copy(input_text_path, output_text_path)
        except FileNotFoundError:
            print(f'{image.split("/")[-1].split(".")[0]}.txt が見つからないため、スキップします.')
    
    print("test作成...")
    for image in test:
        input_text_path = f'{import_text_path}/fixed_labels/{image.split("/")[-1].split(".")[0]}.txt'
        output_image_path = f'./tmp/{export_path}/test'
        output_text_path = f'./tmp/{export_path}/test'
        shutil.copy(image, output_image_path)
        try:
            shutil.copy(input_text_path, output_text_path)
        except FileNotFoundError:
            print(f'{image.split("/")[-1].split(".")[0]}.txt が見つからないため、スキップします.')


    print("val作成...")
    for image in val:
        input_text_path = f'{import_text_path}/fixed_labels/{image.split("/")[-1].split(".")[0]}.txt'
        output_image_path = f'./tmp/{export_path}/val'
        output_text_path = f'./tmp/{export_path}/val'
        shutil.copy(image, output_image_path)
        try:
            shutil.copy(input_text_path, output_text_path)
        except FileNotFoundError:
            print(f'{image.split("/")[-1].split(".")[0]}.txt が見つからないため、スキップします.')

def main():
    load_dotenv()
    import_text_path = os.environ['SHAPE_INPUT_TEXT_DIR']
    import_image_path = os.environ['SHAPE_INPUT_IMAGE_DIR']
    export_path = os.environ['SHAPE_OUTPUT_DIR']
    make_dir(export_path)

    remove(import_text_path, import_image_path, export_path)

if __name__ == "__main__":
    main()