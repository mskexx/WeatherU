#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim : set fileencoding=utf8 :
import sys
import urllib2

api_key = None

class WeatherClient(object):
    """Client for weather undergroind"""
    url_base = "http://api.wunderground.com/api/"
    url_service = {"almanac":"/almanac/q/CA/",
                    "hourly":"/hourly/q/CA/"}


    def __init__(self, api_key):
        self.api_key = api_key


    def almanac(self, location):
        # obtener URL
        url = WeatherClient.url_base+ self.api_key + \
              WeatherClient.url_service["almanac"] + \
              location + "." + "xml"

        web = urllib2.urlopen(url)
        page = web.read()
        web.close()
        print page
        # procesar datos
        # devolver datos

if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "La API a la linea de comandos"

    wc = WeatherClient(api_key)
    wc.almanac("Lleida")
