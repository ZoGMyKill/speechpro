# SpeechPro
# Цели и предпосылки

## 1.1. Зачем идем в разработку продукта?

### Бизнес-цель:
- Разработка ПО для помощи в тренировки выступлений с использованием технологии AI и CV.
- Предоставление рекомендаций пользователям по их выступлению с аргументацией на метрики, полученные посредством записи видео выступления.

### Чему помогаем:
- Облегчить тренировки публичных выступлений.
- Облегчить поиск метана в атмосфере Земли, вызванного природными или техногенными факторами, обеспечивая возможность быстро и точно выявлять источники выброса метана. Тем самым снижая потери для держателей газопроводов и снижая общее присутствие метана в атмосфере, оказывающего значительное влияние на парниковый эффект.

### Что считаем успехом:
- Решение доступно всем по API или через сайт.
- Решение отказоустойчиво и не падает при большой нагрузке.
- Решение имеет понятную документацию по внедрению.

### Расходы:
- **Работа дата-саентистов**: Включает в себя оплату труда и прочие издержки, связанные с формированием и поддержанием команды дата-саентистов, занимающихся созданием и поддержкой ML-моделей для системы распознования утечек метана.
- **Инфраструктурные затраты на ML-модели**: Включают расходы, связанные с необходимой инфраструктурой для развертывания и функционирования ML-моделей. Это может охватывать расходы на вычислительные ресурсы (например, серверы или облачные вычисления), хранение данных, сетевую инфраструктуру, обеспечение безопасности и т.д.

## 1.2. Бизнес-требования и ограничения

### Бизнес-требования:
- Код решения и данные используются только публично доступные или сгенерированные данные.

### Бизнес-ограничения:
- Система может принимать 1 документ за 1 запрос.
- Система имеет простой Web UI с возможностью вставить 1 документ и получить изображение.
- На выходе система отдает сегментированное изображение на каждое входное изображение.
- Время ответа не более 10 секунд.

### Возможные пути развития проекта:
- Дообучение существующих моделей и тюнинг гиперпараметров.
- Проверка новых моделей (CogVLM, SAM и другие).
- Расширение обучающего набора данных, обогащение более качественными примерами.
- В перспективе фундаментальная модель по спутниковым снимкам.

### Возможные применения проекта:
- Поиск утечек газа средне-крупных масштабов в трубопроводе.
- Исследования по вегетативному индексу различных культур.
- Поиск естественных выбросов метана.

## 1.3 Типичный сценарий использования

Компания Х, имеющая под своим управлением газопровод, использует наше решение. При выявлении факта утечек по спутникам легко будет определить координаты, где находится пробой.

# Цели и предпосылки

## 1.1. Зачем идем в разработку продукта?

### Бизнес-цель:
- Создание и запуск мобильного приложения, помогающего старшеклассникам и студентам (16-26 лет) улучшить навыки публичных выступлений с помощью ИИ.
- Разработка ПО для помощи в тренировки выступлений с использованием технологии AI и CV. Задача заключается в предоставлении рекомендаций пользователям по их выступлению с аргументацией на метрики, полученные посредством записи видео выступления.

### Чему помогаем:
- Повысить уверенность в себе при публичных выступлениях.
- Улучшить навыки невербальной коммуникации (мимика, жесты).
- Развить навыки структурирования речи и донесения информации.
- Устранить речевые ошибки и оговорки.

### Что считаем успехом:
- Достижение 10 000 активных пользователей в течение первого года.
- Получение положительных отзывов от 80% пользователей.
- Повышение уверенности в себе у пользователей на 20% после использования приложения.

### Расходы:
- **Разработка и запуск приложения**: 500 000 рублей.
- **Маркетинг и реклама**: 200 000 рублей в год.
- **Поддержка приложения**: 100 000 рублей в год.

## 1.2. Бизнес-требования и ограничения

### Бизнес-требования:
- Приложение должно быть простым в использовании и доступным для пользователей с разным уровнем технической подготовки.
- Анализ выступлений должен быть точным и содержать полезные рекомендации.
- Приложение должно мотивировать пользователей регулярно практиковаться.
- Стоимость разработки и поддержки приложения должна быть окупаемой.

### Бизнес-ограничения:
- Ограниченный бюджет на разработку и маркетинг.
- Конкуренция со стороны других приложений для обучения ораторскому искусству.
- Необходимость постоянного обновления контента и функций приложения.

### Возможные пути развития проекта:
- Расширение целевой аудитории за счет добавления функций для более взрослых пользователей.
- Разработка дополнительных обучающих материалов и курсов.
- Интеграция приложения с другими образовательными платформами.
- Создание платной версии приложения с расширенными функциями.

### Возможные применения проекта:
- Подготовка к экзаменам и презентациям.
- Развитие лидерских качеств.
- Повышение навыков коммуникации в рабочих коллективах.
- Тренировка навыков публичных выступлений для актеров и других представителей творческих профессий.

## 1.3 Типичный сценарий использования

1. Пользователь скачивает и устанавливает приложение на свой смартфон.
2. Он регистрируется в приложении, используя свой номер телефона или адрес электронной почты.
3. Пользователь подключает Telegram-бота приложения, нажав кнопку "Start".
4. Пользователь записывает видео своего выступления и отправляет его в Telegram-бот.
5. Пользователь кратко описывает цель своего выступления в текстовом сообщении.
6. Бот отправляет видео и текстовое описание на сервер приложения.
7. Сервер анализирует видео и аудиозапись выступления с помощью ИИ.
8. Сервер генерирует отчет, который включает в себя:
    - Оценку выступления.
    - Рекомендации по улучшению невербальной коммуникации (мимика, жесты).
    - Анализ структуры речи и советы по донесению информации.
    - Рекомендации по устранению речевых ошибок и оговорок.
9. Бот отправляет отчет пользователю в Telegram.
10. Пользователь может ознакомиться с отчетом и использовать его для улучшения своих навыков публичных выступлений.

# Методология

## 2.1. Постановка задачи

### Задача:
- Разработка мобильного приложения, помогающего старшеклассникам и студентам (16-26 лет) улучшить навыки публичных выступлений с помощью ИИ.

### Цель:
- Создать приложение, которое позволит пользователям:
    - Записывать и загружать видео своих выступлений.
    - Получать автоматизированный анализ своих выступлений с помощью ИИ.
    - Улучшать свои навыки невербальной коммуникации (мимика, жесты).
    - Развивать навыки структурирования речи и донесения информации.
    - Устранять речевые ошибки и оговорки.

### Описание задачи:
- **Входные данные**: Видеозаписи выступлений пользователей, текстовые описания целей выступлений.
- **Обработка**:
    - **Анализ видео**:
        - Определение метрик поведения тела и мимики.
        - Предоставление рекомендаций по улучшению невербальной коммуникации.
    - **Анализ речи**:
        - Транскрипция речи.
        - Анализ структуры речи и донесения информации.
        - Выявление речевых ошибок и оговорок.
        - Предоставление рекомендаций по улучшению вербальной коммуникации.
- **Выходные данные**: Отчет об анализе выступления, включающий в себя:
    - Оценку выступления.
    - Рекомендации по улучшению невербальной и вербальной коммуникации.
    - Конкретные примеры ошибок и способы их исправления.

## 2.2. Критерии успеха технического решения

### Основные критерии:
- **Точность анализа**: Анализ выступления должен быть точным и содержать полезные рекомендации.
- **Полезность рекомендаций**: Рекомендации должны быть actionable, то есть легко выполнимыми и понятными пользователю.
- **Мотивация пользователей**: Приложение должно мотивировать пользователей регулярно практиковаться и совершенствовать свои навыки.
- **Простота использования**: Приложение должно быть простым в использовании и доступным для пользователей с разным уровнем технической подготовки.

### Дополнительные критерии:
- **Конфиденциальность данных**: Приложение должно обеспечивать конфиденциальность данных пользователей.
- **Производительность**: Приложение должно работать быстро и без сбоев.
- **Масштабируемость**
