import os
import imagehash
from PIL import Image
import shutil

img_ext = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.jfif', '.webp')

def remove_duplicate_img(src_dir, dest_dir):
    # 创建目标目录（如果不存在）
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 存储图片的哈希值和文件路径
    hashes = {}

    # 设置哈希值差异的阈值，0 表示完全相同，阈值越高表示可以接受的差异度越大
    hash_diff_threshold = 5

    # 遍历源目录下的所有图片
    for idx, filename in enumerate(os.listdir(src_dir)):
        # 检查文件是否为图片（根据文件扩展名过滤）
        if filename.lower().endswith(img_ext):
            # 构造图片的完整路径
            img_path = os.path.join(src_dir, filename)
            
            # 打开图片并计算其感知哈希值
            try:
                with Image.open(img_path) as img:
                    img_hash = imagehash.phash(img)  # 使用感知哈希算法
            except Exception as e:
                print(f"无法处理第{idx}张图片 {filename}: {e}")
                continue

            # 查找是否有相似的图片
            is_duplicate = False
            for existing_hash, existing_file in hashes.items():
                # 计算两张图片哈希值的差异
                if img_hash - existing_hash <= hash_diff_threshold:
                    print(f"第{idx}张图片: {filename} 找到其相似图片: {existing_file}")
                    is_duplicate = True
                    break
            
            # 如果图片不是重复的，则保存它
            if not is_duplicate:
                # 将图片复制到目标目录，并将文件名保持不变
                shutil.copy(img_path, os.path.join(dest_dir, filename))
                print(f"第{idx}张图片: {filename} 未重复，成功保存至: {os.path.join(dest_dir, filename)} !")
                # 记录这张图片的哈希值
                hashes[img_hash] = filename

    orgin_count = len(os.listdir(src_dir))
    current_count = len(os.listdir(dest_dir))
    print(f"图片去重完成。原先图片总数: {orgin_count}, 去重后图片总数: {current_count}, 去除重复图像数量: {orgin_count-current_count}")

if __name__ == '__main__':
    src_dir = r"D:\DesktopShortcut\Project\MyUtils\image_process\to_remove_duplication"
    dest_dir = r"D:\DesktopShortcut\Project\MyUtils\image_process\to_convert_jpg"
    
    remove_duplicate_img(src_dir, dest_dir)