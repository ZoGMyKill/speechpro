import os
import requests

# Настройки для API ChatGPT
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = os.getenv("OPENAI_API_KEY")


# Функция для получения рекомендаций
def get_speech_recommendations(speed, mood):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    # Формируем запрос к ChatGPT
    prompt = f"""
    {speech_speed} {speaker_mood} {speaker_pose}
    """

    data = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": """
        Без формальностей, только суть. Данные поступают как последовательность чисел: (1) скорость речи (слов/мин),
        (2-7) % времени в настроении (злой, счастливый, в энтузиазме, в отвращении, нейтральный, страх, грусть), (8-9) % времени в позе (открытая, закрытая).
        Дай рекомендации, как улучшить спич. Группируй комментарии. Числа не повторяй. Если предлагаешь улучшить параметр, добавь конкретные техники и практики.
        """,
            },
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 900,
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        recommendations = response.json()["choices"][0]["message"]["content"]
        return recommendations
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
        return None


# Пример использования
if __name__ == "__main__":
    # Пример входных данных
    speech_speed = 200  # слов в минуту
    speaker_mood = "80.3 4.7 5 5 5 0 0"  # ЭМОЦИЯ ЗЛОЙ, СЧАТЛИВЫЙ, В ЭТУЗИАЗМЕ, В ОТВРАЩЕНИИ, НЕЙТРАЛЬНЫЙ, СТРАХ, ГРУСТЬ
    speaker_pose = "60 40"  # ПОЗА ОТКРЫТАЯ, ЗАКРЫТАЯ

    # Получаем рекомендации
    recommendations = get_speech_recommendations(speech_speed, speaker_mood)

    if recommendations:
        print("Рекомендации по улучшению выступления:")
        print(recommendations)
