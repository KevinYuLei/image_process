import os
import shutil

img_ext = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.jfif', '.webp')

def copy_to_dir(src_dir, dest_dir):
    # 创建目标目录（如果不存在）
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 初始化计数器
    counter = 1

    # 遍历源目录下的所有子目录
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # 检查文件是否为图片（根据文件扩展名过滤）
            if file.lower().endswith(img_ext):
                # 构造源文件的完整路径
                src_file_path = os.path.join(root, file)
                
                # 生成新的文件名（image_00001.jpg 这种格式）
                new_file_name = f'image_{counter:05d}{os.path.splitext(file)[1]}'
                
                # 构造目标文件的完整路径
                dest_file_path = os.path.join(dest_dir, new_file_name)
                
                # 移动文件并重命名
                shutil.copy(src_file_path, dest_file_path)
                
                # 递增计数器
                counter += 1

    print(f"已成功将图片转移并重命名，总计 {counter-1} 张图片。")

if __name__ == "__main__":
    # 源路径（包含若干子目录的主目录）
    src_dir = r'D:\DesktopShortcut\Project\MyUtils\image_process\to_process'
    # 目标路径
    dest_dir = r'D:\DesktopShortcut\Project\MyUtils\image_process\to_remove_duplication'
    
    copy_to_dir(src_dir, dest_dir)