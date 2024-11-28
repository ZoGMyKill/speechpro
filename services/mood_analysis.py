from fer import FER
import cv2


def analyze_mood(frame):

    detector = FER()
    result = detector.detect_emotions(frame)

    if result:
        # Извлекаем настроение с наивысшим баллом
        emotions = result[0]['emotions']
        mood = max(emotions, key=emotions.get)
        return mood
    return None
