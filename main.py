#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import os
import webapp2

from handlers.card_handler import CardHandler
from handlers.category_handler import CategoryHandler
from handlers.item_add_form_handler import ItemAddFormHandler
from handlers.item_add_handler import ItemAddHandler
from handlers.item_edit_form_handler import ItemEditFormHandler
from handlers.item_edit_handler import ItemEditHandler
from handlers.item_delete_form_handler import ItemDeleteFormHandler
from handlers.item_delete_handler import ItemDeleteHandler
from handlers.item_move_up_handler import ItemMoveUpHandler
from handlers.item_move_down_handler import ItemMoveDownHandler
from utils.jinja_env import JinjaEnv
from utils.auth import Auth

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
jinja_environment.globals.update({'uri_for': webapp2.uri_for, 'logout_url': Auth.logout_url})
JinjaEnv.set(jinja_environment)

app = webapp2.WSGIApplication([
    webapp2.Route(r'/card/list', handler=CardHandler, handler_method='list', name='card-list'),
    webapp2.Route(r'/card/add_form', handler=CardHandler, handler_method='add_form', name='card-add-form'),
    webapp2.Route(r'/card/add', handler=CardHandler, handler_method='add', name='card-add'),
    webapp2.Route(r'/card/<card_id:\d+>/edit', handler=CardHandler, handler_method='edit', name='card-edit'),
    webapp2.Route(r'/card/<card_id:\d+>/preview', handler=CardHandler, handler_method='preview', name='card-preview'),
    webapp2.Route(r'/card/<card_id:\d+>/category/add_form', handler=CategoryHandler, handler_method='add_form'),
    webapp2.Route(r'/card/<card_id:\d+>/category/add', handler=CategoryHandler, handler_method='add'),
    webapp2.Route(r'/item/<item_id:\d+>/edit_form', handler=ItemEditFormHandler),
    webapp2.Route(r'/item/<item_id:\d+>/edit', handler=ItemEditHandler),
    webapp2.Route(r'/item/<item_id:\d+>/delete_form', handler=ItemDeleteFormHandler),
    webapp2.Route(r'/item/<item_id:\d+>/delete', handler=ItemDeleteHandler),
    webapp2.Route(r'/item/<item_id:\d+>/move_up', handler=ItemMoveUpHandler),
    webapp2.Route(r'/item/<item_id:\d+>/move_down', handler=ItemMoveDownHandler),
    webapp2.Route(r'/category/<category_id:\d+>/edit_form', handler=CategoryHandler, handler_method='edit_form'),
    webapp2.Route(r'/category/<category_id:\d+>/edit', handler=CategoryHandler, handler_method='edit'),
    webapp2.Route(r'/category/<category_id:\d+>/delete_form', handler=CategoryHandler, handler_method='delete_form'),
    webapp2.Route(r'/category/<category_id:\d+>/delete', handler=CategoryHandler, handler_method='delete'),
    webapp2.Route(r'/category/<category_id:\d+>/move_up', handler=CategoryHandler, handler_method='move_up'),
    webapp2.Route(r'/category/<category_id:\d+>/move_down', handler=CategoryHandler, handler_method='move_down'),
    webapp2.Route(r'/category/<category_id:\d+>/item/add_form', handler=ItemAddFormHandler),
    webapp2.Route(r'/category/<category_id:\d+>/item/add', handler=ItemAddHandler)
], debug=True)
