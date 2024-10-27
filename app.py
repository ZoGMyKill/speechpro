import streamlit as st
import tempfile
from services import video_loader, audio_transcription, face_detection, mood_analysis
from collections import Counter

st.title("Анализ видео: транскрибация и распознавание настроений")

# Загрузка видео
uploaded_file = st.file_uploader("Загрузите видеофайл", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(uploaded_file.read())
        temp_video_path = temp_video.name

    # Отображение загруженного видео
    st.video(temp_video_path)

    # Добавление индикатора загрузки на время транскрибации и анализа
    with st.spinner("Обрабатываем аудио и анализируем настроения. Пожалуйста, подождите..."):
        # Извлечение и транскрибация аудио
        transcription = audio_transcription.transcribe_audio(temp_video_path)
        if transcription:
            st.subheader("Транскрибация аудио")
            st.write(transcription)

        # Анализ видео и настроений
        mood_counts = Counter()
        for frame in video_loader.load_video_frames(temp_video_path):
            faces = face_detection.detect_faces(frame)
            if len(faces) > 0:
                mood = mood_analysis.analyze_mood(frame)
                if mood:
                    mood_counts[mood] += 1

    # Индикатор исчезнет, как только процесс завершится
    st.success("Обработка завершена!")

    # Вывод статистики настроений
    st.sidebar.subheader("Статистика настроений")
    total_frames = sum(mood_counts.values())
    if total_frames > 0:
        mood_percentages = {mood: count / total_frames * 100 for mood, count in mood_counts.items()}
        for mood, percentage in mood_percentages.items():
            st.sidebar.write(f"{mood}: {percentage:.2f}%")
    else:
        st.sidebar.write("Данные о настроении недоступны.")
