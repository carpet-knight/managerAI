from time import sleep
import requests
from utils.silvertongue import Silvertongue


class BaseNotifier:
    """A template for Notifier."""

    def send_message(self, message, parse_mode):
        pass

    def start_notification(self):
        pass

    def dummy(self):
        pass

    def end_notification(self):
        pass


class CodexTelegramNotifier(BaseNotifier):
    """A class for sending messages using Codex Bot (see https://github.com/codex-bot/notify)."""

    def __init__(self, notify_url, wordpool):
        # notification url
        self.notify_url = notify_url
        # used for generating text for messages
        self.silvertongue = Silvertongue(wordpool)

    def send_message(self, message, parse_mode=None):
        """Sends a message to the specified url."""

        params = {
            "message": message,
            "parse_mode": parse_mode
        }
        # if parse_mode:
        #     params["parse_mode"] = parse_mode
        try:
            requests.post(self.notify_url, data=params)
        except requests.RequestException as e:
            # TODO: exception handling
            return

    def start_notification(self):
        """Sends a greeting message."""

        self.send_message(self.silvertongue.greet())

    def send_message_with_delay(self, timeout):
        """Sends a message and waits for {timeout} seconds."""

        self.send_message(self.silvertongue.insist())
        sleep(timeout)

    def end_notification(self):
        """Sends a farewell message."""

        self.send_message(self.silvertongue.farewell())
