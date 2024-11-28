import whisper
from moviepy.editor import VideoFileClip
import os


def extract_audio_from_video(video_path):

    video = VideoFileClip(video_path)
    audio_path = video_path.replace(".mp4", ".wav")
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')  # Кодек для сохранения в формате wav
    return audio_path


def transcribe_audio(audio_path):

    model = whisper.load_model("base")  # Можно выбрать "tiny", "small", "medium", "large" для других размеров модели
    result = model.transcribe(audio_path)
    return result["text"]


def transcribe_video_audio(video_path):

    # Извлечение аудио из видео
    audio_path = extract_audio_from_video(video_path)

    # Транскрибация извлеченного аудио
    transcription = transcribe_audio(audio_path)

    # Удаляем временный аудиофайл
    os.remove(audio_path)

    return transcription
