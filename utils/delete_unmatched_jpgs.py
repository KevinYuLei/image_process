import os

def delete_unmatched_jpgs(folder_path):
    # 获取文件夹内所有文件
    files = os.listdir(folder_path)

    # 创建一个集合存储所有的 JSON 文件名（不带扩展名）
    json_files = {os.path.splitext(file)[0] for file in files if file.endswith('.json')}

    # 遍历所有 JPG 文件
    for file in files:
        if file.endswith('.jpg'):
            # 检查 JPG 文件是否有对应的 JSON 文件
            if os.path.splitext(file)[0] not in json_files:
                jpg_path = os.path.join(folder_path, file)
                os.remove(jpg_path)  # 删除 JPG 文件
                print(f"Deleted non-labeled jpg: {jpg_path}")
                
                
if __name__ == '__main__':
    folder_path = r'D:\DesktopShortcut\Project\MyUtils\image_process\to_label\exp3'
    delete_unmatched_jpgs(folder_path)
