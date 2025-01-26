import streamlit as st
import requests

st.set_page_config(layout="wide")


def main():
    st.title("Видео анализ")

    uploaded_file = st.file_uploader("Загрузите видео", type=["mp4", "avi", "mov"])

    if uploaded_file:
        # Сохраняем видео временно
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("Видео успешно загружено!")

        # Отправляем видео в backend для обработки
        with st.spinner("Обработка видео..."):
            response = requests.post(
                "http://backend:8000/process_video/", files={"file": uploaded_file}
            )

        if response.status_code == 200:
            data = response.json()

            # Транскрипция
            st.header("Транскрипция")
            st.text_area(
                "Текст транскрипции", data["transcription"].get("text", ""), height=200
            )

            # Эмоциональный анализ и скорость речи
            with st.sidebar:
                st.header("Эмоциональный анализ")
                emotions = data.get("emotions", {})

                for emotion, score in emotions.items():
                    st.write(f"{emotion.capitalize()}: {score:.2f}")

                st.header("Скорость речи")
                speech_rate = data["transcription"].get("speech_rate", "Неизвестно")
                st.write(f"Скорость речи: {speech_rate} слов/мин")
        else:
            st.error("Ошибка обработки видео. Попробуйте снова.")

        # Отчет
        st.header("Отчет")
        st.write(
            "Вы молодец, хорошо поработали. Для подробного ответа введите ниже ваш OpenAI API Key."
        )

        api_key = st.text_input("OpenAI API Key", type="password")

        if st.button("Получить подробный отчет"):
            if api_key:
                report_response = requests.post(
                    "http://backend:8000/generate_report/",
                    json={
                        "api_key": api_key,
                        "transcription": data["transcription"].get("text", ""),
                    },
                )

                if report_response.status_code == 200:
                    report = report_response.json()
                    st.write(report.get("detailed_report", "Ошибка генерации отчета."))
                else:
                    st.error("Ошибка генерации отчета. Попробуйте снова.")
            else:
                st.error("Пожалуйста, введите ваш OpenAI API Key.")


if __name__ == "__main__":
    main()
