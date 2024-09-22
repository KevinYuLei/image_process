import os

from utils.get_max_exp_dir import get_max_exp_dir
from utils.delete_unmatched_jpgs import delete_unmatched_jpgs
from utils.rename_files import rename_files


if __name__ == '__main__':
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    
    label_dir = os.path.join(script_dir, 'to_label')
    label_exp_dir = get_max_exp_dir(label_dir)
    
    # 调用函数 去除未标注的图片
    delete_unmatched_jpgs(label_exp_dir)
    # 调用函数 将图片和对应的json重新按顺序命名
    rename_files(label_exp_dir)