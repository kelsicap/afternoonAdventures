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
import random

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/form.html')
        self.response.out.write(template.render())

    def post(self):
        restaurant = ['Cheesecake Factory', 'McDonalds', 'Red Robin',
                        'Hard Wok Cafe', 'Five Guys', 'Panera', 'Chipotle']
        movie = ['Dunkirk', 'Spider Man: Homecoming', 'Atomic Blonde',
                    'Despicable Me 3', 'Cars 3', 'Wonder Woman']
        boba = ['Drive Thru Boba', 'Oasis', 'Young Tea', 'ShareTea',
                'Tapioca Express']
        books = ['Barnes and Noble', 'Half Price Books', 'University Book Store',
                'Kirkland Library', 'Bellevue Library']


        park = ['Robinswood Park', 'Gas Works Park', 'Kerry Park',
                'Volunteer Park', 'Bellevue Botanical Garden']
        beach = ['Alki Beach', 'Juanita Beach Park', 'Golden Gardens Park',
                    'Gene Coulon Beach Park', 'Newcastle Beach Park']
        hike = ['Rattlesnake Lake', 'Poo Poo Point', 'Cougar Mountain', 'Lake 22']
        tourist = ['Space Needle', 'Pike Place Market', 'Seattle Waterfront',
                    'Gum Wall', 'Fremont Troll']

        activities = {}

        if self.request.get('movie'):
            activities['Movie'] = random.choice(movie)
        if self.request.get('restaurant'):
            activities['Restaurant'] = random.choice(restaurant)
        if self.request.get('boba'):
            activities['Boba'] = random.choice(boba)
        if self.request.get('books'):
            activities['Books'] = random.choice(books)

        if self.request.get('park'):
            activities['Park'] = random.choice(park)
        if self.request.get('beach'):
            activities['Beach'] = random.choice(beach)
        if self.request.get('hike'):
            activities['Hike'] = random.choice(hike)
        if self.request.get('tourist'):
            activities['Tourist'] = random.choice(tourist)

        template = jinja_environment.get_template('templates/returns.html')
        self.response.out.write(template.render(activities = activities))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/about.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
], debug=True)
