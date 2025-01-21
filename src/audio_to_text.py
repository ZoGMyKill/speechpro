import wave

from vosk import KaldiRecognizer, Model

model_path = "model/vosk-model-ru-0.42"

model = Model(model_path)


def transcribe_audio(file_path):
    wf = wave.open(file_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # Чтение данных и распознавание
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print("Процесс распознавания...")

    # Получение итогового результата
    result = rec.FinalResult()
    return result


def main():
    audio_file_path = "files/output_audio.wav"
    text = transcribe_audio(audio_file_path)

    with open("files/transcribed_text.txt", "w") as text_file:
        text_file.write(text)
        print("Текст успешно сохранен в файл 'transcribed_text.txt'.")


if __name__ == "__main__":
    main()
