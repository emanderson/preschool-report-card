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
import jinja2
import os
import webapp2

from handlers.form_edit_handler import FormEditHandler
from handlers.category_add_form_handler import CategoryAddFormHandler
from handlers.category_add_handler import CategoryAddHandler
from handlers.item_add_form_handler import ItemAddFormHandler
from handlers.item_add_handler import ItemAddHandler
from handlers.item_edit_form_handler import ItemEditFormHandler
from handlers.item_edit_handler import ItemEditHandler
from utils.jinja_env import JinjaEnv

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
jinja_environment.globals.update({'uri_for': webapp2.uri_for})
JinjaEnv.set(jinja_environment)

app = webapp2.WSGIApplication([
    webapp2.Route(r'/form/edit', handler=FormEditHandler, name='form-edit'),
    webapp2.Route(r'/category/add_form', handler=CategoryAddFormHandler),
    webapp2.Route(r'/category/add', handler=CategoryAddHandler),
    webapp2.Route(r'/item/<item_id:\d+>/edit_form', handler=ItemEditFormHandler),
    webapp2.Route(r'/item/<item_id:\d+>/edit', handler=ItemEditHandler),
    webapp2.Route(r'/category/<category_id:\d+>/item/add_form', handler=ItemAddFormHandler),
    webapp2.Route(r'/category/<category_id:\d+>/item/add', handler=ItemAddHandler)
], debug=True)
