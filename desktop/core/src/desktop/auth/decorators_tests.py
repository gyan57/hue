#!/usr/bin/env python
## -*- coding: utf-8 -*-
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import unittest

from nose.tools import assert_equal, assert_true, assert_false, assert_raises

from desktop.auth.decorators import admin_required
from desktop.lib.django_test_util import make_logged_in_client
from desktop.lib.exceptions_renderable import PopupException

from useradmin.models import User, Group, Organization, orm_user_lookup

if sys.version_info[0] > 2:
  from unittest.mock import patch, Mock
else:
  from mock import patch, Mock


class TestDecorator(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.client1 = make_logged_in_client(username='admin', recreate=True, is_superuser=True)
    cls.client2 = make_logged_in_client(username='joe', recreate=True, is_superuser=False)


  def test_user_group(self):
    request = Mock(user=User.objects.get(**{orm_user_lookup(): 'admin'}))
    hello(request)

    request = Mock(user=User.objects.get(**{orm_user_lookup(): 'joe'}))
    assert_raises(PopupException, hello, request)


@admin_required
def hello(request, *args, **kwargs):
  return 'Hello'
