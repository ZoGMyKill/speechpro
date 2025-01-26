FROM python:3.11-slim

# Устанавливаем зависимости системы и ffmpeg
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python зависимости
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Копируем скрипт и аудиофайлы в контейнер
COPY . /app
WORKDIR /app

# Запуск Python скрипта
CMD ["python3", "transcribe_script.py"]

#docker build -t transcribe_script .
#docker run