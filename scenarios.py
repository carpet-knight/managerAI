from random import choice
from datetime import datetime
from utils.seeker import Seeker
from utils.notifiers import CodexTelegramNotifier


class XPathScenario:
    @staticmethod
    def telegram_post_date_check(params):
        """A trigger function for XPathScenario.

        Checks last telegram post date.
        Returns True if there haven't been any posts for too long.
        """
        # TODO: rewrite (make more universal)

        date_pattern = "%Y-%m-%dT%H:%M:%S"

        # search for telegram_post_date_block using xpath
        search_result = Seeker.find_html_element_by_xpath(params['url'], params['xpath'],
                                                          params.get('proxies'))
        if search_result:
            # get string representation of date of the last post in UTC (e.g. 2019-08-16T13:36:03+00:00)
            date_str = search_result[0].attrib.get('datetime')
        else:
            # TODO: logging
            return False

        # create datetime object using last telegram post date
        post_date = datetime.strptime(date_str.split("+")[0], date_pattern)
        # calculate difference between current time in UTC and the date of the last post
        delta = datetime.utcnow() - post_date

        return delta.total_seconds() >= params['max-secs-without-changes']

    @staticmethod
    def telegram_post_date_handler(params):
        """A handler function for XPathScenario.

        Sends notifications to the specified url until new telegram post is published.
        """

        notifier = CodexTelegramNotifier(params['notify-url'], params['messages'])
        # send greeting message
        notifier.start_notification()
        # send notifications until new post is published
        while XPathScenario.telegram_post_date_check(params):
            notifier.send_message_with_delay(choice([2, 5, 10, 15, 60, 120, 180, 300]))
        # end notification seance
        notifier.end_notification()

    @staticmethod
    def xpath_trigger(params):
        pass
