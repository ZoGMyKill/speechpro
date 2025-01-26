# Базовый образ с Python
FROM python:3.11-slim

# Установка FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Копирование кода в контейнер
COPY . /app
WORKDIR /app

# Команда запуска скрипта
CMD ["python", "video_utils.py"]

#docker build -t video_utils .
#docker run --rm -v $(pwd)/temp:/app/temp video_utils
#sudo rm -rf temp
