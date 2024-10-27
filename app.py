import streamlit as st
import tempfile
import cv2
from services import video_loader, audio_transcription, face_detection, mood_analysis
from collections import Counter

# Основное приложение
st.title("Анализ видео: транскрибация и распознавание настроений")

# Загрузка видео
uploaded_file = st.file_uploader("Загрузите видеофайл", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_video:
        temp_video.write(uploaded_file.read())
        temp_video_path = temp_video.name

    # Извлечение и транскрибация аудио
    transcription = audio_transcription.transcribe_audio(temp_video_path)
    if transcription:
        st.subheader("Транскрибация аудио")
        st.write(transcription)

    # Инициализация счетчика настроений
    mood_counts = Counter()

    # Обработка видео
    video_capture = cv2.VideoCapture(temp_video_path)
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))

    # Обработка кадров видео
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        # Обнаружение лиц и анализ настроений
        faces = face_detection.detect_faces(frame)
        if faces:
            mood = mood_analysis.analyze_mood(frame)
            if mood:
                mood_counts[mood] += 1
                face_detection.draw_faces_with_mood(frame, faces, mood)

        # Показ текущего кадра
        st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), caption="Анализ настроений на видео", use_column_width=True)

    video_capture.release()

    # Вывод статистики настроений
    total_frames = sum(mood_counts.values())
    mood_percentages = {mood: count / total_frames * 100 for mood, count in mood_counts.items()}

    st.sidebar.subheader("Статистика настроений")
    for mood, percentage in mood_percentages.items():
        st.sidebar.write(f"{mood}: {percentage:.2f}%")
