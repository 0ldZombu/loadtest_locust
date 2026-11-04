import logging
import json

logger = logging.getLogger(__name__)


def validate_response(response, operation_name: str, thresholds: dict):
    """Валидация ответа"""
    elapsed_ms = response.elapsed.total_seconds() * 1000

    # Проверка статуса
    if response.status_code >= 400:
        response.failure(f"{operation_name} - HTTP {response.status_code}")
        logger.error(f"❌ {operation_name} failed: {response.status_code}")
        return

    # Проверка времени
    critical_threshold = thresholds.get("critical", 2000)
    if elapsed_ms > critical_threshold:
        response.failure(
            f"{operation_name} - Slow response: " +
            f"{elapsed_ms:.0f}ms (threshold: {critical_threshold}ms)")
        logger.warning(
            f"⚠️ {operation_name} - {elapsed_ms:.0f}ms >" +
            f" {critical_threshold}ms")
        return

    # Проверка JSON
    try:
        data = response.json()
        if isinstance(data, list) and len(data) == 0:
            response.failure(f"{operation_name} - Empty response")
            logger.warning(f"⚠️ {operation_name} - Empty list")
            return
    except json.JSONDecodeError:
        pass

    response.success()
    logger.info(f"✅ {operation_name} - OK ({elapsed_ms:.0f}ms)")
