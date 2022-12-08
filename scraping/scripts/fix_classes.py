from dotenv import load_dotenv
import glob
import os
import csv


def make_dir(import_path, fixed_text_path):
    """
    envに指定したフォルダを作成

    Parameters
    ----------
    import_path : str
        importするファイルのパス
    fixed_text_path : str
        修正したtxtファイルを出力するパス
    """
    os.makedirs(f'{import_path}/{fixed_text_path}', exist_ok=True)


def import_config():
    """
    クラスを書き換えるときのtxtファイルをimportする

    Parameters
    ----------
    import_path : str
        importするファイルのパス
    """
    with open('config.csv') as f:
        csv_config = csv.DictReader(f)
        config = [row for row in csv_config]
        return config


def import_class_files(import_path, fixed_text_path, config):
    """
    アノテーション情報が記載されたtxtファイルをimportする

    Parameters
    ----------
    import_path : str
        importするファイルのパス
    fixed_text_path : str
        importするファイルのパス
    config : str
        config
    """

    class_textes = glob.glob(f'{import_path}/labels/*[.txt]')

    for text in class_textes:
        file_name = text.split('/')[-1]
        fixed_labels = [] # 修正したラベルを格納
        with open(text) as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            split_line = line.split(' ')
            class_id = int(split_line[0])
            bbox = ' '.join(split_line[1:])
            before_class = int(config[0]['before'])
            after_class = int(config[0]['after'])
            # csvに記載されたclassを探して修正・それをfixed_labelsに格納する
            if class_id == before_class:
                fixed_labels.append(f'{after_class} {bbox}')
            else:
                fixed_labels.append(line)

        # fixed_text_path内にtextファイルを書き込み
        fixed_labels_joined = "\n".join(fixed_labels)
        output_text_path = f'{import_path}/{fixed_text_path}/{file_name}'
        with open(output_text_path, 'w') as f:
            f.write(fixed_labels_joined)
    print(f'{len(class_textes)}件書き込みが完了しました.')
                

    

def main():
    load_dotenv()
    import_path = os.environ['SHAPE_INPUT_TEXT_DIR']
    fixed_text_path = os.environ['FIX_OUTPUT_DIR']
    make_dir(import_path, fixed_text_path)
    config = import_config()
    import_class_files(import_path, fixed_text_path, config)


if __name__ == "__main__":
    main()