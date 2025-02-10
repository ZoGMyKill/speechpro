
FROM python:3.11-slim

# Устанавливаем базовые зависимости
RUN apt-get update && apt-get install -y \
    python3-pip \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python зависимости
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Копируем скрипт и аудиофайлы в контейнер
COPY . /app
WORKDIR /app

# Запуск Python скрипта
CMD ["python3", "emotion_analysis.py"]
