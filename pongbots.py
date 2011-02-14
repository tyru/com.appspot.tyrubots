#!/usr/bin/env python
# coding: utf-8


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import re
from urlparse import urlparse
from django.utils import simplejson


class PongBots(webapp.RequestHandler):
    def get(self, path):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("PongBots: hi")

    def post(self, path):
        r = re.compile(r"^\s*ping\s*$", re.IGNORECASE)
        json = simplejson.loads(self.request.body)
        self.response.headers['Content-Type'] = 'text/plain'

        for e in json['events']:
            if r.match(e['message']['text']):
                msg = e['message']['nickname'] + ': pong'
                self.response.out.write(msg)



if __name__ == "__main__":
    application = webapp.WSGIApplication([
        ('/pongbots/(.*)', PongBots),
    ], debug=True)
    run_wsgi_app(application)
