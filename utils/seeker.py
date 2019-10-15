import logging
import requests
from lxml import html


class Seeker:

    @staticmethod
    def find_html_element_by_xpath(url, xpath, proxies=None):
        """Makes a GET request to the {url}. Searches for an html element(s) by its xpath."""

        try:
            response = requests.get(url, proxies=proxies).text
        except requests.RequestException as e:
            logging.error("Request error: {}".format(e))
            # TODO: exception handling
            return None

        tree = html.fromstring(response)
        try:
            elem = tree.xpath(xpath)
        except Exception as e:
            # logging.error("XPathError: {}".format(e))
            # TODO: exception handling
            return None

        return elem
