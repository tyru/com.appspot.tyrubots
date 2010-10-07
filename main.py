#!/usr/bin/env python
# coding: utf-8


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("hi")


if __name__ == "__main__":
    application = webapp.WSGIApplication([
        ('/', MainPage),
    ], debug=True)
    run_wsgi_app(application)
