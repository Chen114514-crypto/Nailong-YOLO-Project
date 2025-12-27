import os
import glob

# 设置你的路径 (根据你的实际情况修改)
# 注意：你需要分别对 'train' 和 'val' 运行一次，或者手动改一下这里的路径
IMG_DIR = r'D:\PythonProject\Nylon.data\my_nailong_project\datasets\images\val'
LABEL_DIR = r'D:\PythonProject\Nylon.data\my_nailong_project\datasets\labels\val'


def clean_data():
    # 获取所有图片和标签文件
    # 假设你的图片是 .jpg，如果是 .png 请改成 *.png
    images = glob.glob(os.path.join(IMG_DIR, '*.jpg'))

    deleted_count = 0

    print(f"正在检查 {IMG_DIR} ...")

    for img_path in images:
        # 获取文件名 (不带后缀)，例如 '001'
        basename = os.path.splitext(os.path.basename(img_path))[0]

        # 构造对应的标签文件路径
        label_path = os.path.join(LABEL_DIR, basename + '.txt')

        # 如果标签文件不存在，说明这张图没标过
        if not os.path.exists(label_path):
            print(f"删除未标注图片: {img_path}")
            os.remove(img_path)  # 删除图片
            deleted_count += 1

    print(f"清理完成！共删除了 {deleted_count} 张未标注的图片。")


if __name__ == '__main__':
    clean_data()