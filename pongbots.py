#!/usr/bin/env python
# coding: utf-8


from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import re

import sys
sys.path.append('lib')
from gaeLingr import Lingr

class PongBots(webapp.RequestHandler):
    def get(self):
        self.response.out.write("PongBots: hi")
    def post(self):
        lingr_id = 'pong_bots'
        lingr_pass = 'h9WezlKz6GFow' # XXX: ???
        lingr = Lingr(lingr_id, lingr_pass)
        lingr.create_session()
        r = re.compile(r"^\s*ping\s*$", re.IGNORECASE)
        for e in lingr.stream():
            if 'message' in e and r.match(e['message']['text']):
                # TODO: Sanitize
                lingr.say('@' + e['message']['nickname'] + ' pong')



if __name__ == "__main__":
    application = webapp.WSGIApplication([
        ('/pongbots/.*', PongBots),
    ], debug=True)
    run_wsgi_app(application)
