#!/usr/bin/env python3
""" starting point """

from flask import Flask, render_template
from flask.views import View


app = Flask(__name__)
class Home(View):
        init_every_request = False

        def __init__(self, ugo, sam, sue, template):
            self.ugo = ugo
            self.sam = sam
            self.sue = sue
            self.template = template

        def dispatch_request(self):
            contributors="SAMKE, SUE609, UgoMUSK, iBlossom"
            logo="Dochine"
            return render_template(self.template, logo=logo, contributors=contributors, ugo=self.ugo, sam=self.sam, sue=self.sue)

app.add_url_rule("/", view_func=Home.as_view("View", "peer1", "peer2", "peer3", "class.html"))
