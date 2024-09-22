import os
import re

def get_max_exp_dir(base_dir):
    max_index = -1
    max_dir = None
    
    # 遍历指定目录下的所有文件夹
    for folder in os.listdir(base_dir):
        match = re.match(r'exp(\d+)', folder)
        if match:
            index = int(match.group(1))
            if index > max_index:
                max_index = index
                max_dir = folder
    return os.path.join(base_dir, max_dir)


if __name__ == '__main__':
    base_dir = r'D:\DesktopShortcut\Project\MyUtils\image_process\to_convert_jpg'  # 替换为你的文件夹路径
    max_exp_dir = get_max_exp_dir(base_dir)
    if max_exp_dir is not None:
        print(f"序号最大的文件夹是: {max_exp_dir}")
    else:
        print("未找到任何 exp{i} 文件夹。")
