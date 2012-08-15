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
from handlers.item_handler import ItemHandler
from handlers.key_handler import KeyHandler
from handlers.text_line_handler import TextLineHandler
from handlers.signature_handler import SignatureHandler
from utils.jinja_env import JinjaEnv
from utils.auth import Auth

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
jinja_environment.globals.update({'uri_for': webapp2.uri_for, 'logout_url': Auth.logout_url})
JinjaEnv.set(jinja_environment)

app = webapp2.WSGIApplication([
    webapp2.Route(r'/card/list', handler=CardHandler, handler_method='list', name='card-list'),
    webapp2.Route(r'/card/add_form', handler=CardHandler, handler_method='add_form', name='card-add-form'),
    webapp2.Route(r'/card/<card_id:\d+>/add_owner', handler=CardHandler, handler_method='add_owner', name='card-add'),
    webapp2.Route(r'/card/<card_id:\d+>/add_owner_form', handler=CardHandler, handler_method='add_owner_form', name='card-add-form'),
    webapp2.Route(r'/card/add', handler=CardHandler, handler_method='add', name='card-add'),
    webapp2.Route(r'/card/<card_id:\d+>/edit', handler=CardHandler, handler_method='edit', name='card-edit'),
    webapp2.Route(r'/card/<card_id:\d+>/preview', handler=CardHandler, handler_method='preview', name='card-preview'),
    webapp2.Route(r'/card/<card_id:\d+>/text_line/add_form', handler=TextLineHandler, handler_method='add_form'),
    webapp2.Route(r'/card/<card_id:\d+>/text_line/add', handler=TextLineHandler, handler_method='add'),
    webapp2.Route(r'/card/<card_id:\d+>/signature/add_form', handler=SignatureHandler, handler_method='add_form'),
    webapp2.Route(r'/card/<card_id:\d+>/signature/add', handler=SignatureHandler, handler_method='add'),
    webapp2.Route(r'/card/<card_id:\d+>/category/add_form', handler=CategoryHandler, handler_method='add_form'),
    webapp2.Route(r'/card/<card_id:\d+>/key_level/add', handler=KeyHandler, handler_method='add'),
    webapp2.Route(r'/card/<card_id:\d+>/key_level/add_form', handler=KeyHandler, handler_method='add_form'),
    webapp2.Route(r'/card/<card_id:\d+>/category/add', handler=CategoryHandler, handler_method='add'),
    webapp2.Route(r'/item/<item_id:\d+>/edit_form', handler=ItemHandler, handler_method='edit_form'),
    webapp2.Route(r'/item/<item_id:\d+>/edit', handler=ItemHandler, handler_method='edit'),
    webapp2.Route(r'/item/<item_id:\d+>/delete_form', handler=ItemHandler, handler_method='delete_form'),
    webapp2.Route(r'/item/<item_id:\d+>/delete', handler=ItemHandler, handler_method='delete'),
    webapp2.Route(r'/item/<item_id:\d+>/move_up', handler=ItemHandler, handler_method='move_up'),
    webapp2.Route(r'/item/<item_id:\d+>/move_down', handler=ItemHandler, handler_method='move_down'),
    webapp2.Route(r'/category/<category_id:\d+>/edit_form', handler=CategoryHandler, handler_method='edit_form'),
    webapp2.Route(r'/category/<category_id:\d+>/edit', handler=CategoryHandler, handler_method='edit'),
    webapp2.Route(r'/category/<category_id:\d+>/delete_form', handler=CategoryHandler, handler_method='delete_form'),
    webapp2.Route(r'/category/<category_id:\d+>/delete', handler=CategoryHandler, handler_method='delete'),
    webapp2.Route(r'/category/<category_id:\d+>/move_up', handler=CategoryHandler, handler_method='move_up'),
    webapp2.Route(r'/category/<category_id:\d+>/move_down', handler=CategoryHandler, handler_method='move_down'),
    webapp2.Route(r'/text_line/<text_line_id:\d+>/edit_form', handler=TextLineHandler, handler_method='edit_form'),
    webapp2.Route(r'/text_line/<text_line_id:\d+>/edit', handler=TextLineHandler, handler_method='edit'),
    webapp2.Route(r'/text_line/<text_line_id:\d+>/delete_form', handler=TextLineHandler, handler_method='delete_form'),
    webapp2.Route(r'/text_line/<text_line_id:\d+>/delete', handler=TextLineHandler, handler_method='delete'),
    webapp2.Route(r'/text_line/<text_line_id:\d+>/move_up', handler=TextLineHandler, handler_method='move_up'),
    webapp2.Route(r'/text_line/<text_line_id:\d+>/move_down', handler=TextLineHandler, handler_method='move_down'),
    webapp2.Route(r'/signature/<signature_id:\d+>/edit_form', handler=SignatureHandler, handler_method='edit_form'),
    webapp2.Route(r'/signature/<signature_id:\d+>/edit', handler=SignatureHandler, handler_method='edit'),
    webapp2.Route(r'/signature/<signature_id:\d+>/delete_form', handler=SignatureHandler, handler_method='delete_form'),
    webapp2.Route(r'/signature/<signature_id:\d+>/delete', handler=SignatureHandler, handler_method='delete'),
    webapp2.Route(r'/signature/<signature_id:\d+>/move_up', handler=SignatureHandler, handler_method='move_up'),
    webapp2.Route(r'/signature/<signature_id:\d+>/move_down', handler=SignatureHandler, handler_method='move_down'),
    webapp2.Route(r'/key_level/<key_level_id:\d+>/edit_form', handler=KeyHandler, handler_method='edit_form'),
    webapp2.Route(r'/key_level/<key_level_id:\d+>/edit', handler=KeyHandler, handler_method='edit'),
    webapp2.Route(r'/key_level/<key_level_id:\d+>/delete_form', handler=KeyHandler, handler_method='delete_form'),
    webapp2.Route(r'/key_level/<key_level_id:\d+>/delete', handler=KeyHandler, handler_method='delete'),
    webapp2.Route(r'/category/<category_id:\d+>/item/add_form', handler=ItemHandler, handler_method='add_form'),
    webapp2.Route(r'/category/<category_id:\d+>/item/add', handler=ItemHandler, handler_method='add'),
    webapp2.Route(r'/', handler=CardHandler, handler_method='main'),
], debug=True)
