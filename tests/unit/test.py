#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2015, Guilherme Dinis J
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


import json
import unittest

from jsonuri import jsonuri


class TestJsonUri(unittest.TestCase):

    def test_001_should_serialize_data(self):

        data = {
            'age': '31',
            'name': 'John',
            'account': {
                'regions': ['US.East', 'SG']
            }
        }

        data_as_str = json.dumps(data)
        serialized_data = jsonuri.serialize(json.loads(data_as_str))
        deserialized_data = jsonuri.deserialize(serialized_data)

        for k, v in data.items():

            self.assertTrue(k in deserialized_data.keys())

            if k in ['age', 'name']:
                self.assertEqual(v, deserialized_data[k])

            elif k == 'account':
                self.assertTrue('regions' in deserialized_data[k].keys())
                for region in data[k]['regions']:
                    self.assertTrue(region in deserialized_data[k]['regions'])


if __name__ == "__main__":

    unittest.main()
