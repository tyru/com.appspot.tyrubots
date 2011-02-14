#!/usr/bin/env python
# coding: utf-8


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import re
from urlparse import urlparse
from django.utils import simplejson


class ZimbuBots(webapp.RequestHandler):
    def get(self, path):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<img src="http://www.a-a-p.org/images/zimbu_cutout.jpg" />')

    def post(self, path):
        r_right_brace = re.compile(r"^[ \t]*}[ \t]*$")
        r_left_brace = re.compile(r"^[ \t]*{[ \t]*$")
        json = simplejson.loads(self.request.body)
        self.response.headers['Content-Type'] = 'text/plain'

        for e in json['events']:
            if r_left_brace.match(e['message']['text']):
                msg = "We don't need { to see where the block starts."
                self.response.out.write(msg)
            elif r_right_brace.match(e['message']['text']):
                msg = 'http://www.a-a-p.org/images/zimbu_cutout.jpg'
                self.response.out.write(msg)



if __name__ == "__main__":
    application = webapp.WSGIApplication([
        ('/zimbubots/(.*)', ZimbuBots),
    ], debug=True)
    run_wsgi_app(application)
