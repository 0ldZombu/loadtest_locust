from locust import HttpUser, task, between
from config import Config
from tools.validators import validate_response
import random
import logging


logger = logging.getLogger(__name__)


class TemplatesUser(HttpUser):
    """
    Основной класс пользователя для нагрузочного тестирования Шаблонизатора
    """
    host = Config.BASE_URL
    wait_time = between(0.5, 1)

    def on_start(self):
        self.user_id = None
        self.auth_token = None
        self.created_post_id = None

    @task(Config.WEIGHTS["get_events"])
    def get_events(self):
        with self.client.get(
            "/events",
            catch_response=True,
            name="Get Events List"
        ) as response:
            validate_response(response, "Events List", Config.THRESHOLDS)

    @task(Config.WEIGHTS["get_templates"])
    def get_templates(self):
        with self.client.get(
            "/templates",
            catch_response=True,
            name="Get Templates List"
        ) as response:
            validate_response(response, "Templates List", Config.THRESHOLDS)

    @task(Config.WEIGHTS["get_new_templates_form"])
    def get_new_templates_form(self):
        with self.client.get(
            "/templates/new",
            catch_response=True,
            name="Get New Templates Form"
        ) as response:
            validate_response(
                response, "New Templates Form", Config.THRESHOLDS)

    @task(Config.WEIGHTS["get_new_events_form"])
    def get_new_event_form(self):
        with self.client.get(
            "/events/new",
            catch_response=True,
            name="Get New Events Form"
        ) as response:
            validate_response(response, "New Events Form", Config.THRESHOLDS)

    @task(Config.WEIGHTS["get_events_sorted"])
    def get_events_sorted(self):
        sort_options = [
            "name",
            "-name",
            "code",
            "-code",
            "updatedAt",
            "-updatedAt"
        ]
        sort_by = random.choice(sort_options)

        params = {"page": 0, "size": 10, "sort": sort_by}

        with self.client.get(
            "/events",
            params=params,
            catch_response=True,
            name=f"Events Sort: {sort_by}"
        ) as response:
            validate_response(
                response,
                f"Events Sorted by {sort_by}",
                Config.THRESHOLDS
            )

    @task(Config.WEIGHTS["get_templates_sorted"])
    def get_templates_sorted(self):
        sort_options = [
            "name",
            "-name",
            "code",
            "-code",
            "events",
            "-events",
            "updatedAt",
            "-updatedAt"
        ]
        sort_by = random.choice(sort_options)

        params = {"page": 0, "size": 10, "sort": sort_by}

        with self.client.get(
            "/templates",
            params=params,
            catch_response=True,
            name=f"Templates Sort: {sort_by}"
        ) as response:
            validate_response(
                response,
                f"Templates Sorted by {sort_by}",
                Config.THRESHOLDS
            )
# Запуск с выборок класса locust --class-picker
