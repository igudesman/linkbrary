import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from analyzers import LinkAnalyzer


def test_simple_analyzer():
    analyzer = LinkAnalyzer()
    text = analyzer.get_link_text('https://google.com')
    estimated_time = analyzer.time_estimator(text)
    assert estimated_time == 1
