"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:

    def __init__(self):
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        value = message.value()
        self.temperature = value["temperature"]
        self.status = value["status"]
