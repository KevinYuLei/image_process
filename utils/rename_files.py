import os

def rename_files(folder_path):
    # 获取文件夹内所有jpg和json文件
    jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    
    # 先给所有文件添加_tmp后缀
    for jpg_file in jpg_files:
        tmp_jpg_name = jpg_file.replace('.jpg', '_tmp.jpg')
        os.rename(os.path.join(folder_path, jpg_file), os.path.join(folder_path, tmp_jpg_name))
    
    for json_file in json_files:
        tmp_json_name = json_file.replace('.json', '_tmp.json')
        os.rename(os.path.join(folder_path, json_file), os.path.join(folder_path, tmp_json_name))
    
    # 从0开始命名
    next_index = 0

    # 处理所有_tmp文件
    for jpg_file in sorted(os.listdir(folder_path)):
        if jpg_file.endswith('_tmp.jpg'):
            new_jpg_name = f'image_{next_index:05d}.jpg'
            os.rename(os.path.join(folder_path, jpg_file), os.path.join(folder_path, new_jpg_name))
            
            # 对应的JSON文件也重命名
            json_file = jpg_file.replace('_tmp.jpg', '_tmp.json')
            if json_file in os.listdir(folder_path):
                new_json_name = f'image_{next_index:05d}.json'
                os.rename(os.path.join(folder_path, json_file), os.path.join(folder_path, new_json_name))
            
            next_index += 1  # 增加计数器

    print(f"重命名完成，总计重命名文件: {next_index}个。")

if __name__ == '__main__':
    folder_path = r'D:\DesktopShortcut\Project\Datasets\leg_on_desk'  # 替换为要重命名的文件夹路径
    rename_files(folder_path)
