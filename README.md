# Nailong Detector (基于 YOLOv8 的奶龙检测)

![YOLOv8](https://img.shields.io/badge/YOLOv8-SOTA-blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

一个基于 **YOLOv8** 训练的目标检测项目，专门用于识别和检测视频或图片中的 **“奶龙” (Nailong)** 形象。本项目包含了完整的数据处理、帧提取、训练脚本以及推理演示。

## 📂 项目结构

```text
Nailong-YOLO-Project/
├── weights/
│   └── best.pt          # 训练好的最佳模型权重
├── assets/
│   └── demo.jpg         # 演示图片
├── data.yaml            # 数据集配置文件
├── classes.txt          # 类别名称说明
├── train.py             # 模型训练脚本
├── clean_data.py        # 数据清洗脚本
├── extract_frames.py    # 视频抽帧脚本
├── requirements.txt     # 项目依赖环境
└── README.md            # 项目说明文档
🛠️ 环境安装 (Installation)
本项目建议使用 Python 3.8+ 环境。

克隆仓库

Bash

git clone [https://github.com/](https://github.com/)[你的用户名]/Nailong-YOLO-Project.git
cd Nailong-YOLO-Project
安装依赖

Bash

pip install -r requirements.txt
核心依赖包括：Ultralytics YOLOv8, OpenCV, MoviePy 等。

🚀 快速开始 (Quick Start)
1. 模型推理 (Inference)
使用我们提供的预训练权重 weights/best.pt 进行检测。

命令行方式 (CLI):

Bash

# 检测图片
yolo detect predict model=weights/best.pt source='path/to/your/image.jpg' show=True

# 检测视频
yolo detect predict model=weights/best.pt source='path/to/your/video.mp4' show=True
Python 脚本方式: 你也可以编写简单的 Python 脚本来调用：

Python

from ultralytics import YOLO

# 加载模型
model = YOLO('weights/best.pt')

# 进行预测
results = model('test.jpg', show=True, save=True)
2. 模型训练 (Training)
如果你想自己重新训练模型，请确保数据集路径在 data.yaml 中配置正确，然后运行：

Bash

python train.py
🔧 工具脚本说明 (Utils)
本项目包含了一些用于处理数据集的实用脚本：

extract_frames.py: 用于将视频文件按间隔抽取为图片帧，便于制作数据集。

clean_data.py: 用于清洗数据集（例如删除损坏的图片或没有对应标签的文件）。

📊 模型信息 (Model Info)
架构: YOLOv8 (Ultralytics)

类别: nailong (详见 classes.txt)

训练框架: PyTorch

🤝 贡献 (Contributing)
欢迎提交 Issue 或 Pull Request 来改进这个项目！
