import torch
from aniemore.recognizers.voice import VoiceRecognizer
from aniemore.models import HuggingFaceModel
import numpy as np
import librosa
import soundfile as sf

model = HuggingFaceModel.Voice.WavLM
device = "cuda" if torch.cuda.is_available() else "cpu"
vr = VoiceRecognizer(model=model, device=device)


# Функция для распознавания эмоций по сегментам
def analyze_emotions_percentage(audio_file, segment_duration=1.5):

    audio, sr = librosa.load(audio_file, sr=None)
    duration = librosa.get_duration(y=audio, sr=sr)  # длительность файла в секундах

    # Инициализация для подсчета эмоций
    emotions_count = {}
    total_segments = int(np.ceil(duration / segment_duration))

    # Разделение на сегменты
    for segment in range(total_segments):
        start_time = segment * segment_duration
        end_time = min((segment + 1) * segment_duration, duration)
        segment_audio = audio[int(start_time * sr) : int(end_time * sr)]

        # Сохранение сегмента во временный файл
        segment_file = "temp_segment.wav"
        sf.write(segment_file, segment_audio, sr)

        # Распознавание эмоции для сегмента
        emotion = vr.recognize(segment_file, return_single_label=True)

        # Подсчет эмоций
        if emotion not in emotions_count:
            emotions_count[emotion] = 0
        emotions_count[emotion] += 1

    # Подсчет процентов
    total_segments = sum(emotions_count.values())
    emotion_percentages = {
        emotion: (count / total_segments) * 100
        for emotion, count in emotions_count.items()
    }

    return emotion_percentages


audio_file = "./temp/audio.wav"
emotion_percentages = analyze_emotions_percentage(audio_file)

emotion_order = [
    "anger",
    "happiness",
    "enthusiasm",
    "disgust",
    "neutral",
    "fear",
    "sadness",
]

# Вывод эмоций в указанном порядке
print("Эмоции на протяжении всего файла:")
for emotion in emotion_order:
    if emotion in emotion_percentages:
        print(f"{emotion}: {emotion_percentages[emotion]:.2f}")
    else:
        print(f"{emotion}: 0.00")  # Если эмоция отсутствует в словаре, выводим 0
