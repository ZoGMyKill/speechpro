import cv2

def load_video_frames(video_path):

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Не удалось открыть видеофайл")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame

    cap.release()
