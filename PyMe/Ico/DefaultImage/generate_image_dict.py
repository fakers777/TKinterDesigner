import os
from PIL import Image

# 获取当前目录
current_dir = os.getcwd()

# 初始化图片分类字典
image_dict = {}

# 遍历所有子文件夹
for folder_name in os.listdir(current_dir):
    folder_path = os.path.join(current_dir, folder_name)
    
    # 确保是目录
    if os.path.isdir(folder_path):
        # 初始化该分类的字典
        image_dict[folder_name] = {}
        
        # 遍历文件夹中的所有文件
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # 确保是文件且是图片格式
            if os.path.isfile(file_path):
                # 检查文件扩展名是否为图片格式
                ext = os.path.splitext(file_name)[1].lower()
                if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                    try:
                        # 打开图片获取尺寸
                        with Image.open(file_path) as img:
                            width, height = img.size
                        
                        # 将图片信息添加到分类字典中
                        image_dict[folder_name][file_name] = f'{width}x{height}'
                    except Exception as e:
                        print(f"处理文件 {file_path} 时出错: {e}")

# 打印结果
print("图片分类字典:")
for category, images in image_dict.items():
    print(f"\n{category}:")
    for img_file, img_size in images.items():
        print(f"  - {img_file}: {img_size}")

# 可选：将结果保存到JSON文件
import json
with open('image_dict.json', 'w', encoding='utf-8') as f:
    json.dump(image_dict, f, ensure_ascii=False, indent=2)

print("\n结果已保存到 image_dict.json 文件")
