#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gunicorn.util
from gunicorn.app.wsgiapp import WSGIApplication


class TWSGIAPP(WSGIApplication):

    def init(self, parser, opts, args):
        print(self.cfg)
        self.app_uri = ".app:app"
        args = [self.app_uri]
        super(TWSGIAPP, self).init(parser, opts, args)

    def load_wsgiapp(self):
        self.chdir()
        return gunicorn.util.import_app(self.app_uri)

    def run(self):
        super(TWSGIAPP, self).run()


def run_app():
    TWSGIAPP().run()
