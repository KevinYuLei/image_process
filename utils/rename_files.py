import os

def rename_files(folder_path):
    # 获取文件夹内所有jpg和json文件
    jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    
    # 创建一个集合用于存储已存在的文件名
    existing_names = set(os.listdir(folder_path))
    
    # 从0开始命名
    next_index = 0

    for jpg_file in jpg_files:
        new_jpg_name = f'image_{next_index:05d}.jpg'
        while new_jpg_name in existing_names:  # 检查重名
            next_index += 1
            new_jpg_name = f'image_{next_index:05d}.jpg'
        
        os.rename(os.path.join(folder_path, jpg_file), os.path.join(folder_path, new_jpg_name))
        existing_names.add(new_jpg_name)  # 更新已存在的文件名集合
        
        # 重命名对应的json文件
        json_file = jpg_file.replace('.jpg', '.json')
        if json_file in json_files:
            new_json_name = f'image_{next_index:05d}.json'
            while new_json_name in existing_names:  # 检查重名
                next_index += 1
                new_json_name = f'image_{next_index:05d}.json'
            
            os.rename(os.path.join(folder_path, json_file), os.path.join(folder_path, new_json_name))
            existing_names.add(new_json_name)  # 更新已存在的文件名集合
        
        next_index += 1  # 增加计数器

    print(f"重命名完成，总计重命名文件: {next_index}个。")



if __name__ == '__main__':
    folder_path = r'D:\DesktopShortcut\Project\Datasets\leg_on_desk'  # 替换为要重命名s的文件夹路径
    rename_files(folder_path)
