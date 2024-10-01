import cv2

# 视频文件路径
video_path = 'frame.mp4'
# 输出帧数据文件
output_data_file = 'frames.data'

# 定义目标控制台的宽度和高度（需要根据实际情况调整）
console_width = 150
console_height = 38

# 打开 MP4 文件
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("无法打开视频文件")
    exit()

# 获取视频的总帧数
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"视频帧数: {frame_count}, 帧率: {fps}")

# 打开输出文件，准备写入所有帧数据
with open(output_data_file, 'wb') as f:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 缩放帧到控制台的尺寸
        resized_frame = cv2.resize(frame, (console_width, console_height))

        # 将 BGR 图像转换为 RGB
        frame_rgb = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

        # 将帧数据转换为字节流并写入文件
        frame_data = frame_rgb.tobytes()
        f.write(frame_data)

        # print("写入一帧数据")

cap.release()
print(f"帧数据已保存到 '{output_data_file}' 文件中")
