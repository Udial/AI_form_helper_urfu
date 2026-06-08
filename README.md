AI Form Helper URFU

Веб-приложение для интеллектуального заполнения проектных заявок с использованием GigaChat.

Проект состоит из:

* Frontend — HTML/CSS/JavaScript интерфейс для заполнения формы проекта.
* Backend — FastAPI-сервис, отвечающий за авторизацию пользователей и взаимодействие с GigaChat.
* AI Assistant — помощник для генерации целей проекта, результатов, критериев приемки и описания проекта.

⸻

Возможности

* Автоматическая генерация текста с помощью GigaChat.
* JWT-авторизация пользователей.
* Автосохранение черновиков в браузере.
* Голосовой ввод текста.
* Вставка сгенерированного текста непосредственно в поля формы.
* Улучшение и перегенерация текста.
* Поддержка нескольких типов проектных полей:
    * Цель проекта
    * Результат проекта
    * Критерии приемки
    * Описание проекта

⸻

Стек технологий

Backend

* Python 3.11+
* FastAPI
* Uvicorn
* Pydantic
* Python-JOSE
* GigaChat SDK

Frontend

* HTML5
* CSS3
* Vanilla JavaScript

⸻

Структура проекта

.
├── main.py
├── config.py
├── requirements.txt
├── .env
├── routers/
├── services/
│   ├── auth.py
│   └── ai/
│       └── gigachat.py
├── schemas.py
└── website.html

⸻

Настройка окружения

Создайте файл .env в корне проекта.

Пример:

GIGACHAT_CREDENTIALS=YOUR_GIGACHAT_AUTHORIZATION_DATA
GIGACHAT_SCOPE=GIGACHAT_API_PERS
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

Получение GigaChat Credentials

Необходимо использовать параметр Authorization data из кабинета GigaChat API.

⚠️ Не используйте:

* Client Secret
* Client ID
* client_id:client_secret

SDK ожидает уже готовую Base64-строку Authorization data.

⸻

Локальный запуск

1. Клонировать репозиторий

git clone <repository_url>
cd <repository_name>

2. Создать виртуальное окружение

Windows:

python -m venv .venv
.venv\Scripts\activate

Linux/macOS:

python -m venv .venv
source .venv/bin/activate

⸻

3. Установить зависимости

pip install -r requirements.txt

Если требуется:

pip install "python-jose[cryptography]"

⸻

4. Запустить Backend

uvicorn main:app --reload

После запуска API будет доступно по адресу:

http://127.0.0.1:8000

⸻

5. Запустить Frontend

В отдельном терминале:

python -m http.server 5500

Открыть в браузере:

http://127.0.0.1:5500/website.html

⸻

Проверка работоспособности

После запуска:

1. Откройте сайт.
2. Нажмите кнопку ✦ AI возле любого поля.
3. Отправьте запрос.
4. Получите ответ от GigaChat.
5. Нажмите Вставить в форму для заполнения поля.

⸻

API

Авторизация

Получение JWT токена

POST /api/v1/auth/login

Пример:

curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
     -F "username=test"

⸻

Генерация текста

POST /api/v1/ai/assist

Требуется JWT-токен.

Пример запроса:

{
  "idea": "Разработка системы мониторинга склада",
  "field": "description"
}

Допустимые значения поля:

goal
result
criteria
description

⸻

Разработка

Для проверки изменений:

git add .
git commit -m "Description of changes"

⸻

Лицензия

Проект создан в рамках учебной деятельности УрФУ.

Использование и модификация разрешены в образовательных целях.
