# image_process

每次使用时，将要处理的图片或者含图片的文件夹放置在/to_process/exp{i}目录下
i为最新一次的运行次数，/to_process/exp{i} 该目录需要自行创建，然后运行start.py即可

## step
/to_process/exp{i} -> /to_remove_duplication/exp{i} -> /to_convert_jpg/exp{i} -> /to_label//exp{i}