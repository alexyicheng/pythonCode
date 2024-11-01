# 30.10.2024

import requests
from bs4 import BeautifulSoup
import json
import re

class StepStone(object):

    # initial search information, which job -> you want to know about it and how many pages are required
    def __init__(self):
        self.job_title = input('Geben Sie bitte den Job, der Sie mehr wissen wollen :) :')
        self.pages = int(input('Geben Sie bitte an, wie viel Seite an Informationen benötigen Sie für die Visualisierung:'))



if __name__ == '__main__':
    ss = StepStone()