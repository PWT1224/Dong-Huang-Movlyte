import cv2  # 导入OpenCV库（图像处理/视频捕捉核心）
cap = cv2.VideoCapture(0)  # 创建视频捕捉对象cap，调用摄像头,0表示设备
# 循环：持续读取摄像头画面（只要摄像头正常打开）
while(cap.isOpened()):
    retval, frame = cap.read()  # 读取一帧画面
    cv2.imshow('测试点one', frame)  # 显示实时画面到窗口
    # 等待5毫秒，若按下任意键（返回值≥0）则退出循环
    if cv2.waitKey(5) >= 0:
        break

