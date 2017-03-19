import re
import os
import json
from datetime import datetime

import requests


ARCHIVE_URL = 'http://devopsreactions.tumblr.com/archive/%(year)s/%(month)s'
REGEX = 'class="post_title">([^<]+)</div>.*?src="([^"]+)".*?data-notes="(\d+)"'


def scrap_month(month, year):
    print 'Fetching %s/%s' % (month, year)
    html = requests.get(ARCHIVE_URL % {'year': year, 'month': month})
    if html.status_code != 200:
        print 'Response %s - skipping.' % html.status_code
        return []
    res = re.findall(REGEX, html.text, re.DOTALL)
    return res


def scrap():
    data = []

    for year in range(2012, datetime.now().year + 1):
        for month in range(1, 13):
            data.extend(scrap_month(month, year))

    path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(path, 'gifs.json'), 'w') as outfile:
        json.dump(data, outfile, indent=4)


scrap()
