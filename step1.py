import os
from utils.create_next_exp_folder import create_next_exp_folder
from utils.copy_to_dir import copy_to_dir
from utils.remove_duplicate_img import remove_duplicate_img
from utils.rename_img import rename_img
from utils.convert_images_to_jpg import convert_images_to_jpg


if __name__ == '__main__':
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    
    process_dir = os.path.join(script_dir, 'to_process')
    remove_dir = os.path.join(script_dir, 'to_remove_duplication')
    convert_dir = os.path.join(script_dir, 'to_convert_jpg')
    label_dir = os.path.join(script_dir, 'to_label')
    
    i, remove_exp_dir = create_next_exp_folder(remove_dir)
    _, convert_exp_dir = create_next_exp_folder(convert_dir)
    _, label_exp_dir = create_next_exp_folder(label_dir)
    process_exp_dir = os.path.join(process_dir, 'exp'+str(i))
    
    copy_to_dir(process_exp_dir, remove_exp_dir)
    
    remove_duplicate_img(remove_exp_dir, convert_exp_dir)
    
    rename_img(convert_exp_dir)
    
    convert_images_to_jpg(convert_exp_dir)
    
    copy_to_dir(convert_exp_dir, label_exp_dir)
    # 之后再label_exp_dir内进行labelme标注，全部标注完成后运行step2.py
    