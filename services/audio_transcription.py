from moviepy.editor import VideoFileClip
import speech_recognition as sr


def transcribe_audio(video_path):
    recognizer = sr.Recognizer()
    temp_audio_path = video_path + ".wav"

    # Извлечение аудио из видео
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(temp_audio_path)

    # Транскрибация
    with sr.AudioFile(temp_audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            transcription = recognizer.recognize_google(audio_data, language="ru-RU")
            return transcription
        except sr.UnknownValueError:
            return "Не удалось распознать аудио"
        except sr.RequestError:
            return "Ошибка при запросе к сервису транскрибации"
