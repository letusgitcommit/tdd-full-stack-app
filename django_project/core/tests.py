"""Contains tests and other utilities for the project settings module.

Here, we can build our own test runner to be able to mock settings variables, so that we
can decouple other pieces of architecture from Django.
"""

from __future__ import annotations

from typing import Any

from django.test.runner import DiscoverRunner
from django.test.utils import override_settings

# Override different settings contained in the settings module by filling in this
# dictionary.
OVERIDE_SETTINGS: dict[str, str | int | bool] = {}


class CustomTestRunner(DiscoverRunner):
    """Provide an overridable testing environment for the test runner."""

    def run_tests(self, *args: Any, **kwargs: Any) -> int:
        with override_settings(**OVERIDE_SETTINGS):
            return super().run_tests(*args, **kwargs)
