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

from handlers.card_list_handler import CardListHandler
from handlers.card_add_form_handler import CardAddFormHandler
from handlers.card_add_handler import CardAddHandler
from handlers.card_edit_handler import CardEditHandler
from handlers.card_preview_handler import CardPreviewHandler
from handlers.category_add_form_handler import CategoryAddFormHandler
from handlers.category_add_handler import CategoryAddHandler
from handlers.category_edit_form_handler import CategoryEditFormHandler
from handlers.category_edit_handler import CategoryEditHandler
from handlers.category_delete_form_handler import CategoryDeleteFormHandler
from handlers.category_delete_handler import CategoryDeleteHandler
from handlers.category_move_up_handler import CategoryMoveUpHandler
from handlers.category_move_down_handler import CategoryMoveDownHandler
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
    webapp2.Route(r'/card/list', handler=CardListHandler, name='card-list'),
    webapp2.Route(r'/card/add_form', handler=CardAddFormHandler, name='card-add-form'),
    webapp2.Route(r'/card/add', handler=CardAddHandler, name='card-add'),
    webapp2.Route(r'/card/<card_id:\d+>/edit', handler=CardEditHandler, name='card-edit'),
    webapp2.Route(r'/card/<card_id:\d+>/preview', handler=CardPreviewHandler, name='card-preview'),
    webapp2.Route(r'/card/<card_id:\d+>/category/add_form', handler=CategoryAddFormHandler),
    webapp2.Route(r'/card/<card_id:\d+>/category/add', handler=CategoryAddHandler),
    webapp2.Route(r'/item/<item_id:\d+>/edit_form', handler=ItemEditFormHandler),
    webapp2.Route(r'/item/<item_id:\d+>/edit', handler=ItemEditHandler),
    webapp2.Route(r'/item/<item_id:\d+>/delete_form', handler=ItemDeleteFormHandler),
    webapp2.Route(r'/item/<item_id:\d+>/delete', handler=ItemDeleteHandler),
    webapp2.Route(r'/item/<item_id:\d+>/move_up', handler=ItemMoveUpHandler),
    webapp2.Route(r'/item/<item_id:\d+>/move_down', handler=ItemMoveDownHandler),
    webapp2.Route(r'/category/<category_id:\d+>/edit_form', handler=CategoryEditFormHandler),
    webapp2.Route(r'/category/<category_id:\d+>/edit', handler=CategoryEditHandler),
    webapp2.Route(r'/category/<category_id:\d+>/delete_form', handler=CategoryDeleteFormHandler),
    webapp2.Route(r'/category/<category_id:\d+>/delete', handler=CategoryDeleteHandler),
    webapp2.Route(r'/category/<category_id:\d+>/move_up', handler=CategoryMoveUpHandler),
    webapp2.Route(r'/category/<category_id:\d+>/move_down', handler=CategoryMoveDownHandler),
    webapp2.Route(r'/category/<category_id:\d+>/item/add_form', handler=ItemAddFormHandler),
    webapp2.Route(r'/category/<category_id:\d+>/item/add', handler=ItemAddHandler)
], debug=True)
