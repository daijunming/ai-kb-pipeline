"""Retry and exponential backoff helpers."""


def should_retry(error: Exception) -> bool:
    return True
