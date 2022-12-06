from dotenv import load_dotenv
import glob
import os


def import_class_files(import_path):
    """
    アノテーション情報が記載されたtxtファイルをimportする

    Parameters
    ----------
    import_path : str
        importするファイルのパス
    """
    class_txtes = glob.glob(f'{import_path}/labels/*[.txt]')
    for text in class_txtes:
        print(f'file: {text}')
        with open(text) as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            split_line = line.split(' ')
            class_id = split_line[0]
            bbox = split_line[1:]
            print(f'class: {class_id}, bbox: {bbox}')
    

def main():
    load_dotenv()
    import_path = os.environ['SHAPE_INPUT_DIR']
    import_class_files(import_path)


if __name__ == "__main__":
    main()