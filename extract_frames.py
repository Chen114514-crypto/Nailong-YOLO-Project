import cv2
import os

# ================= 配置区域 =================
# 1. 视频文件的路径 (请修改为你下载下来的视频文件名)
VIDEO_PATH = 'video.mp4'

# 2. 图片保存的目录 (直接保存到你的训练集文件夹里)
OUTPUT_DIR = r'D:\PythonProject\Nylon.data\my_nailong_project\datasets\images\train'

# 3. 截取间隔 (每隔多少帧截一张)
# 视频通常是30帧/秒。设置为30就是每秒截一张；设置为15就是每0.5秒截一张。
# 建议设置大一点，防止图片太相似，造成数据冗余。
FRAME_INTERVAL = 30


# ===========================================

def extract_frames():
    # 检查输出目录是否存在，不存在则创建
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"文件夹不存在，已创建: {OUTPUT_DIR}")

    # 读取视频
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print(f"错误: 无法打开视频文件 {VIDEO_PATH}，请检查路径是否正确。")
        return

    count = 0  # 视频总帧数计数器
    save_count = 0  # 保存图片计数器

    print("开始截取...按 Ctrl+C 可以强制停止")

    while True:
        ret, frame = cap.read()

        # 如果读不到帧了（视频结束），就退出循环
        if not ret:
            break

        # 每隔 FRAME_INTERVAL 帧保存一次
        if count % FRAME_INTERVAL == 0:
            # 生成文件名，例如: 00001.jpg
            filename = os.path.join(OUTPUT_DIR, f"{save_count:05d}.jpg")

            # 保存图片
            cv2.imwrite(filename, frame)
            print(f"已保存: {filename}")
            save_count += 1

        count += 1

    cap.release()
    print(f"\n处理完成！共保存了 {save_count} 张图片到 {OUTPUT_DIR}")


if __name__ == '__main__':
    extract_frames()