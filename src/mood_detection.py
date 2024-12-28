import tempfile

import cv2
import streamlit as st
from fer import FER

# Загрузка модели для детектирования лиц
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Создаем объект детектора эмоций
emotion_detector = FER(mtcnn=True)


# Функция для детектирования лиц и распознавания эмоций
def detect_faces_and_emotions(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for x, y, w, h in faces:
        face = image[y : y + h, x : x + w]
        emotion, score = emotion_detector.top_emotion(face)
        if emotion:
            text = f"{emotion} ({int(score * 100)}%)"
        else:
            text = "No emotion detected"

        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(
            image, text, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2
        )

    return image


# Основная часть Streamlit приложения
def main():
    st.title("Face Tracking with Emotion Labeling")
    st.write("Upload a video file to track faces and detect emotions.")

    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi"])

    if uploaded_file is not None:
        # Создаем временный файл для сохранения видео
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            video_path = temp_file.name

        # Используем cv2.VideoCapture() для открытия видеофайла
        video = cv2.VideoCapture(video_path)

        # Проверка успешного открытия видеофайла
        if not video.isOpened():
            st.error("Error: Could not open video file.")
            return

        # Пустой контейнер для отображения обработанного видео
        processed_video_container = st.empty()

        while True:
            ret, frame = video.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Детектирование лиц и распознавание эмоций
            processed_frame = detect_faces_and_emotions(frame_rgb)

            # Обновление контейнера с обработанным видео
            processed_video_container.image(
                processed_frame, channels="RGB", use_column_width=True
            )

        video.release()

        st.success("Video processing completed!")


if __name__ == "__main__":
    main()
