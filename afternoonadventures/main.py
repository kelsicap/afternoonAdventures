#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
            template = jinja_environment.get_template('templates/form.html')
            self.response.out.write(template.render())

    def post(self):
        activities = {
        'restaurant': self.request('restaurant'),
        'movie': self.request.get('movie'),
        'weather': self.request.get('weather')}

<<<<<<< HEAD
        template = jinja_environment.get_template('templates/returns.html')
            self.response.out.write(template.render(my_vars))
=======
        template = jinja_environment.get_template('templates/form.html')
        self.response.out.write(template.render(my_vars))
>>>>>>> 4ee84648b7dd2a6118f6375fbae9ca56622988a2

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
