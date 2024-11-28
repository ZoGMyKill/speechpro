import streamlit as st
from services.video_loader import load_video_frames
from services.audio_transcription import transcribe_video_audio
from services.mood_analysis import analyze_mood
import cv2
import os

# Настройка заголовка приложения
st.title("Анализ Видео: Транскрибация и Распознавание Настроений")

# Загрузка видео
uploaded_file = st.file_uploader("Выберите видео файл", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Сохранение загруженного файла
    temp_video_path = os.path.join("temp", uploaded_file.name)
    with open(temp_video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.video(temp_video_path)  # Отображаем видео в интерфейсе

    # Кнопка для запуска анализа
    if st.button("Начать анализ"):
        # Транскрибация аудио
        with st.spinner("Идет процесс транскрибации..."):
            transcription = transcribe_video_audio(temp_video_path)
            st.subheader("Транскрипция:")
            st.write(transcription)

        # Анализ настроений
        st.subheader("Анализ настроений:")
        mood_counts = {}

        # Обработка кадров видео для анализа настроений
        with st.spinner("Идет процесс анализа настроений..."):
            for frame in load_video_frames(temp_video_path):
                mood = analyze_mood(frame)
                if mood:
                    if mood in mood_counts:
                        mood_counts[mood] += 1
                    else:
                        mood_counts[mood] = 1

        # Отображение результатов анализа настроений
        if mood_counts:
            total_frames = sum(mood_counts.values())
            st.write("Процент времени в каждом настроении:")
            for mood, count in mood_counts.items():
                percentage = (count / total_frames) * 100
                st.write(f"{mood}: {percentage:.2f}%")
        else:
            st.write("Настроение не было обнаружено.")

    # Удаление временного видео после анализа
    if os.path.exists(temp_video_path):
        os.remove(temp_video_path)
