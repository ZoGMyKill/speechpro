# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Создаем директорию для приложения
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt /app/requirements.txt

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем весь код приложения в контейнер
COPY . /app

# Устанавливаем переменную окружения для API ключа (вообще надо спрятать как-то потом)
ENV OPENAI_API_KEY="secret"

# Указываем команду запуска
CMD ["python", "report.py"]
