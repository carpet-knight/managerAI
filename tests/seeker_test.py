from utils.seeker import Seeker
from lxml import html

if __name__ == "__main__":

    httpsProxy = "https://118.97.151.130:9090"
    httpProxy = "http://210.212.73.61:80"
    proxy = {
        "http": httpProxy,
        "https": httpsProxy
    }

    URL = "https://t.me/s/codex_team"
    XPATH = "/html/body/main/div/section/div[20]/div[1]/div[2]/div[3]/div/span[3]/a/time"

    elem = Seeker.find_html_element_by_xpath(URL, XPATH, proxies=proxy)

    print(html.tostring(elem[0]).decode('utf-8'))
