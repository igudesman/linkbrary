from monkeylearn import MonkeyLearn
from configs import TOPIC_CLASSIFIER, MONKEY_TOKEN
import requests
from bs4 import BeautifulSoup
import errors


class Analyzer:
    def __init__(self):
        self.monkey = MonkeyLearn(MONKEY_TOKEN)

    def get_topic(self, text):
        raise NotImplementedError()

    def time_estimator(self, text):
        raise NotImplementedError()


class LinkAnalyzer(Analyzer):
    def __init__(self):
        super().__init__()
        self.resource_type = 'link'

    def get_link_text(self, link):
        try:
            html = requests.get(link).text
        except Exception:
            raise errors.InvalidUrl()

        soup = BeautifulSoup(html, features="html.parser")
        return ' '.join(soup.get_text().split())

    def time_estimator(self, text):
        time = (len(text) // 800) + 1
        return time

    def get_topic(self, text):
        return self.monkey.classifiers.classify(
            model_id=TOPIC_CLASSIFIER,
            data=[text]
        )


class VideoAnalyzer(Analyzer):
    def __init__(self):
        super().__init__()
        self.resource_type = 'video'

    def time_estimator(self, text):
        pass

    def get_topic(self, text):
        pass
