import os
import subprocess


def compress_video(input_video_path, output_dir):
    """
    Сжимает видео и сохраняет в указанной папке.

    :param input_video_path: Путь к исходному видео.
    :param output_dir: Папка для сохранения сжатого видео.
    :return: Путь к сжатому видео.
    """
    os.makedirs(output_dir, exist_ok=True)
    compressed_video_path = os.path.join(output_dir, "compressed_video.mp4")

    # Команда для сжатия видео
    command = [
        "ffmpeg",
        "-i",
        input_video_path,
        "-vcodec",
        "libx264",
        "-crf",
        "28",
        compressed_video_path,
    ]

    subprocess.run(command, check=True)
    return compressed_video_path


def extract_audio(input_video_path, output_dir):
    """
    Извлекает аудио из видео и сохраняет его в формате .wav.

    :param input_video_path: Путь к исходному видео.
    :param output_dir: Папка для сохранения аудио.
    :return: Путь к аудиофайлу .wav.
    """
    os.makedirs(output_dir, exist_ok=True)
    audio_path = os.path.join(output_dir, "audio.wav")

    # Команда для извлечения аудио
    command = [
        "ffmpeg",
        "-i",
        input_video_path,
        "-ac",
        "1",
        "-ar",
        "16000",
        "-vn",
        audio_path,
    ]

    subprocess.run(command, check=True)
    return audio_path


if __name__ == "__main__":
    input_video = "./test_files/test.MOV"
    output_directory = "./temp"

    # Сжимаем видео
    compressed_video = compress_video(input_video, output_directory)
    print(f"Сжатое видео сохранено: {compressed_video}")

    # Извлекаем аудио
    audio_file = extract_audio(compressed_video, output_directory)
    print(f"Аудиофайл сохранен: {audio_file}")
