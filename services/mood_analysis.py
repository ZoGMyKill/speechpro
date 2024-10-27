from fer import FER

# Инициализация модели анализа настроений
emotion_detector = FER(mtcnn=False)

def analyze_mood(frame):
    result = emotion_detector.top_emotion(frame)
    if result:
        mood, _ = result
        return mood
    return None
