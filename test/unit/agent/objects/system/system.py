# -*- coding: utf-8 -*-
from hamcrest import *

from test.base import BaseTestCase

from amplify.agent.objects.system.system import SystemObject


__author__ = "Grant Hulegaard"
__copyright__ = "Copyright (C) Nginx, Inc. All rights reserved."
__credits__ = ["Mike Belov", "Andrei Belov", "Ivan Poluyanov", "Oleg Mamontov", "Andrew Alexeev", "Grant Hulegaard"]
__license__ = ""
__maintainer__ = "Grant Hulegaard"
__email__ = "grant.hulegaard@nginx.com"


class SystemObjectTestCase(BaseTestCase):
    def test_basic(self):
        system_object = SystemObject(hostname=None, uuid=None)

        assert_that(system_object, not_(equal_to(None)))
        assert_that(system_object.definition, equal_to({'type': 'system', 'hostname': None, 'uuid': None}))
        assert_that(system_object.definition_healthy, equal_to(False))
        assert_that(system_object.definition_hash, has_length(64))
        assert_that(system_object.hash(system_object.definition), equal_to(system_object.definition_hash))
        assert_that(system_object.hash_local(1, 2, 3), has_length(64))
        assert_that(system_object.local_id, equal_to(None))

    def test_definition_healthy(self):
        system_object = SystemObject(hostname='foo', uuid='bar')

        assert_that(system_object, not_(equal_to(None)))
        assert_that(system_object.definition, equal_to({'type': 'system', 'hostname': 'foo', 'uuid': 'bar'}))
        assert_that(system_object.definition_healthy, equal_to(True))
