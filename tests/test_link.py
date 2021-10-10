import os
import sys
from unittest import TestCase

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from src.link import Link


def test_link_init_custom():
    link = Link(
        title='Cool',
        url='google.com',
        estimated_time=10,
        topics=['a', 'b']
    )
    TestCase().assertDictEqual(
        {'title': 'Cool',
         'url': 'google.com',
         'estimated_time': 10,
         'topics': ['a', 'b'],
         'viewed': False
         },
        link.__dict__
    )


def test_link_init_dict():
    dict1 = {'url': 'google.com',
             'topics': ['a', 'b'],
             'viewed': False
             }
    link = Link(dict_params=dict1)
    dict1['estimated_time'] = 'N/A'
    dict1['title'] = 'sample title'
    TestCase().assertDictEqual(
        dict1,
        link.__dict__
    )
