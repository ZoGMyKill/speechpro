import whisperx

# Устройство выполнения (GPU или CPU)
device = "cpu"

# Входной аудиофайл
audio_file = "./temp/audio.wav"
batch_size = 16
compute_type = "int8"

# Загрузка модели WhisperX и обработка транскрипции
model = whisperx.load_model("small", device, compute_type=compute_type)
audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
result_full = result

# Выравнивание текста с аудио
model_a, metadata = whisperx.load_align_model(
    language_code=result["language"], device=device
)
result = whisperx.align(
    result["segments"], model_a, metadata, audio, device, return_char_alignments=False
)

# Вычисление скорости речи
total_words = sum(len(segment["words"]) for segment in result["segments"])
first_word_start_time = result["segments"][0]["start"]
last_word_end_time = result["segments"][-1]["end"]
duration_minutes = (last_word_end_time - first_word_start_time) / 60
words_per_minute = total_words / duration_minutes

print(f"Средняя скорость речи: {words_per_minute:.2f} слов в минуту")
print("Текст:")
print(result_full["segments"][0]["text"])
