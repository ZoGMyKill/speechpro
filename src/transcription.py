import whisperx
import torch
import csv
import gc

# Устройство выполнения (GPU или CPU)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Входной аудиофайл
audio_file = "./temp/audio.wav"
batch_size = 16
compute_type = "int8" if device == "cuda" else "float32"

model = whisperx.load_model("small", device, compute_type=compute_type)
audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)

# Очистка памяти GPU
gc.collect()
if device == "cuda":
    torch.cuda.empty_cache()
del model

model_a, metadata = whisperx.load_align_model(
    language_code=result["language"], device=device
)
result = whisperx.align(
    result["segments"], model_a, metadata, audio, device, return_char_alignments=False
)

# Сохранение результата в CSV
output_csv = "output.csv"

with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Start Time", "End Time", "Word"])  # Заголовки

    for segment in result["segments"]:
        for word_info in segment["words"]:
            start_time = word_info["start"]
            end_time = word_info["end"]
            word = word_info["word"]
            writer.writerow([start_time, end_time, word])

# Вычисление скорости речи
total_words = sum(len(segment["words"]) for segment in result["segments"])
first_word_start_time = result["segments"][0]["words"][0]["start"]
last_word_end_time = result["segments"][-1]["words"][-1]["end"]
duration_minutes = (last_word_end_time - first_word_start_time) / 60
words_per_minute = total_words / duration_minutes

print(f"Средняя скорость речи: {words_per_minute:.2f} слов в минуту")
