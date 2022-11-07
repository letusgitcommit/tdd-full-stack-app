from __future__ import annotations

from django.test import LiveServerTestCase
from selenium import webdriver


class BrowseTheWebsite(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_visit_the_website(self) -> None:
        self.browser.get(self.live_server_url)
        self.assertIn("Todo App", self.browser.title)
