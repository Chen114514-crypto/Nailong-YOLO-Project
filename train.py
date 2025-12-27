import os
from ultralytics import YOLO


def main():
    # ================= 配置区域 =================
    # 项目配置文件路径
    YAML_PATH = 'data.yaml'

    # 训练参数设置
    EPOCHS = 50  # 训练轮数 (50-100轮通常足够)
    BATCH_SIZE = 8  # 批次大小 (显存够大可改 16，显存小改 4)
    IMG_SIZE = 640  # 图片尺寸
    WORKERS = 0  # Windows下必须设为0，否则多线程会报错
    MODEL_NAME = 'yolov8n.pt'  # 使用 Nano 模型 (最小最快)
    PROJECT_NAME = 'nailong_detector'  # 项目名称 (结果保存在 runs/detect/nailong_detector)
    # ===========================================

    # 1. 检查配置文件是否存在
    if not os.path.exists(YAML_PATH):
        print(f"❌ 错误: 找不到配置文件 {YAML_PATH}")
        print("请确保 data.yaml 在当前目录下，且内容正确。")
        return

    print(f"🚀 正在加载模型 {MODEL_NAME}...")
    try:
        # 加载预训练模型 (会自动下载)
        model = YOLO(MODEL_NAME)

        print("🔥 开始训练... (这可能需要一段时间，请耐心等待)")
        print("💡 提示: 初次运行会下载模型权重，请保持网络连接")

        # 2. 开始训练
        model.train(
            data=YAML_PATH,
            epochs=EPOCHS,
            imgsz=IMG_SIZE,
            batch=BATCH_SIZE,
            workers=WORKERS,
            project='runs/detect',  # 结果保存的根目录
            name=PROJECT_NAME,  # 具体的项目文件夹名
            device='',  # 留空自动选择 (优先使用 GPU)
            exist_ok=True,  # 如果文件夹已存在，允许覆盖(或继续)
            amp=False  # 如果遇到显卡报错，可以尝试改为 False
        )

        print(f"\n✅ 训练完成！")
        print(f"👉 最佳模型权重保存在: runs/detect/{PROJECT_NAME}/weights/best.pt")
        print(f"👉 训练结果图表保存在: runs/detect/{PROJECT_NAME}/results.png")

    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        print("建议检查: 1. data.yaml路径是否正确  2. 图片和标签是否一一对应")


if __name__ == '__main__':
    # 必须放在 if __name__ == '__main__': 下运行，否则 Windows 会报错
    main()