import os


class Config:
    # ════════════════════════════════════════════════════════════
    # БАЗОВЫЕ URL
    # ════════════════════════════════════════════════════════════

    BASE_URL = os.getenv("BASE_URL", "http://localhost:3000/email-templates")
    AUTH_URL = os.getenv("AUTH_URL", "http://localhost:3000")

    # ════════════════════════════════════════════════════════════
    # НАСТРОЙКИ НАГРУЗКИ
    # ════════════════════════════════════════════════════════════

    DEFAULT_USERS = int(os.getenv("DEFAULT_USERS", "100"))
    DEFAULT_SPAWN_RATE = int(os.getenv("DEFAULT_SPAWN_RATE", "1000"))
    DEFAULT_RUN_TIME = os.getenv("DEFAULT_RUN_TIME", "5m")

    # ════════════════════════════════════════════════════════════
    # ПОРОГИ ПРОИЗВОДИТЕЛЬНОСТИ (в миллисекундах)
    # ════════════════════════════════════════════════════════════

    THRESHOLDS = {
        "critical": int(os.getenv("THRESHOLD_CRITICAL", "2000")),
        "warning": int(os.getenv("THRESHOLD_WARNING", "1000")),
        "acceptable": int(os.getenv("THRESHOLD_ACCEPTABLE", "500"))
    }

    # ════════════════════════════════════════════════════════════
    # ВЕС ДЛЯ ЗАДАЧ
    # ════════════════════════════════════════════════════════════

    WEIGHTS = {
        # HTTP задачи
        "get_events": 3,
        "get_templates": 3,
        "get_new_events_form": 1,
        "get_new_templates_form": 1,
        "get_events_sorted": 4,
        "get_templates_sorted": 3,
    }

    # ════════════════════════════════════════════════════════════
    # ДАННЫЕ ДЛЯ ТЕСТОВ С АВТОРИЗАЦИЕЙ
    # ════════════════════════════════════════════════════════════

    TEST_USERS = [
        {"username": "username", "password": "password1"},
        {"username": "username2", "password": "password2"}
    ]
