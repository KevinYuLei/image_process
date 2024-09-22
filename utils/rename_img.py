import os

img_ext = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.jfif', '.webp')

def rename_img(img_dir):
    # 获取该文件夹下的所有文件，并按照文件名排序
    files = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(img_ext)])

    # 初始化计数器
    counter = 1

    # 遍历所有图片文件
    for file in files:
        # 获取文件的完整路径
        old_file_path = os.path.join(img_dir, file)
        
        # 新的文件名格式 (image_00001.jpg)
        new_file_name = f'image_{counter:05d}{os.path.splitext(file)[1]}'
        
        # 新文件路径
        new_file_path = os.path.join(img_dir, new_file_name)
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        
        # 递增计数器
        counter += 1

    print(f"所有图片已重新命名，总共处理了 {counter-1} 张图片。")
    

if __name__ == '__main__':
    img_dir = r"D:\DesktopShortcut\Project\MyUtils\image_process\to_rename\exp3"
    
    rename_img(img_dir)