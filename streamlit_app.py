import json
import os
import wave

import streamlit as st
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from vosk import KaldiRecognizer, Model


# Функция для извлечения аудио из видео с логированием
def extract_audio_from_video_with_pydub(video_filepath, output_audio_filepath):
    video_clip = VideoFileClip(video_filepath)
    temp_audio_filepath = "temp_audio.mp3"
    video_clip.audio.write_audiofile(temp_audio_filepath)

    audio = AudioSegment.from_file(temp_audio_filepath)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)

    audio.export(
        output_audio_filepath, format="wav", parameters=["-acodec", "pcm_s16le"]
    )
    os.remove(temp_audio_filepath)


# Функция для преобразования аудио в текст с логированием
def transcribe_audio(file_path, model_path, log_text):

    model = Model(model_path)
    wf = wave.open(file_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print("Процесс распознавания...")

    result = rec.FinalResult()
    return json.loads(result)


# Streamlit приложение
st.image("logo_speechpro.png", use_column_width=True)
st.title("SPEECHPRO - это ваш друг в подготовке выступления")

uploaded_video = st.file_uploader("Загрузите видеофайл", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    video_filepath = f"temp_video.{uploaded_video.type.split('/')[1]}"
    with open(video_filepath, "wb") as f:
        f.write(uploaded_video.getbuffer())

    st.video(video_filepath)

    # Извлечение аудио из видео
    output_audio_filepath = "output_audio.wav"

    with st.spinner("Извлечение аудио из видео..."):
        extract_audio_from_video_with_pydub(video_filepath, output_audio_filepath)
        st.success("Аудио извлечено из видео!")

    # Преобразование аудио в текст
    model_path = "model/vosk-model-ru-0.42"

    with st.spinner("Транскрибация аудио..."):
        transcription_result = transcribe_audio(
            output_audio_filepath, model_path, st.empty()
        )
        st.success("Транскрибация завершена!")

    if "text" in transcription_result:
        st.text_area("Распознанный текст", transcription_result["text"], height=300)
    else:
        st.error("Не удалось распознать текст.")

    # Удаление временных файлов
    os.remove(video_filepath)
    os.remove(output_audio_filepath)
