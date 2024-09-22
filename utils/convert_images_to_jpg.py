import os
from PIL import Image

def convert_images_to_jpg(folder_path: str):
    """
    将指定文件夹下的所有非.jpg图片文件（包括.webp）转换为.jpg格式，并保存到同一文件夹。

    Args:
        folder_path (str): 要处理的文件夹路径。
    """
    # 支持的图片格式，添加 .webp 支持
    supported_formats = ('.png', '.bmp', '.gif', '.tiff', '.jpeg', '.webp', '.jfif')

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 获取文件的完整路径
        file_path = os.path.join(folder_path, filename)
        
        # 检查文件是否为支持的图片格式，并且不是已经是 .jpg 的文件
        if filename.lower().endswith(supported_formats) and not filename.lower().endswith('.jpg'):
            try:
                # 打开图片
                with Image.open(file_path) as img:
                    # 构造新的文件名，替换扩展名为 .jpg
                    new_filename = os.path.splitext(filename)[0] + ".jpg"
                    new_file_path = os.path.join(folder_path, new_filename)

                    # 将图片转换为 RGB 模式并保存为 .jpg 格式
                    img.convert('RGB').save(new_file_path, "JPEG")

                    print(f"Converted {filename} to {new_filename}")
                # 删除原文件
                os.remove(file_path)
                print(f"Deleted original file: {filename}")
                
            except Exception as e:
                print(f"Failed to convert {filename}. Error: {e}")

if __name__ == "__main__":
    folder_path = r"D:\DesktopShortcut\Project\Datasets\leg_on_desk"  # 替换为你要处理的文件夹路径
    convert_images_to_jpg(folder_path)
