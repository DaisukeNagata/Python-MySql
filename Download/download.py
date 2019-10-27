#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib.request
import sys

def download():

    url = sys.argv[1]
    title = sys.argv[2]
    urllib.request.urlretrieve(url,"{0}".format(title))

if __name__ == "__main__":
    download()
