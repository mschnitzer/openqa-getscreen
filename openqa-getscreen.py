#!/usr/bin/python3

import re
import sys
import urllib.request
from subprocess import call

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: openqa-getscreen [URL]")
    else:
        response = urllib.request.urlopen(sys.argv[1])
        data = response.read()
        text = data.decode('utf-8')
        
        testid = re.findall('tests\/([0-9]{1,})/', sys.argv[1])[0]
        matches = re.findall('\/tests\/[0-9]{1,}\/images\/(.*)\'\)\;', text)
        if len(matches) < 1:
            print("Could not find any screens on that page.")
        else:
            print("Downloading {} images from test {}:".format(len(matches), testid))
            for i in matches:
                call("wget https://openqa.opensuse.org/tests/{}/images/{}".format(testid, i).split())
