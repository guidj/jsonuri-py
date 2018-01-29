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


import unittest

from jsonuri import jsonuri

samples = [
    {
        "name": "John",
        "age": 31,
        "profile": "http://profiles/professionals/who.cgi?id=269260&full=yes",
        "schools": [
            "School A & B", "School B & D", "School C &amp; AFG"
        ],
        "friends": [
            {
                "name": "Mary",
                "age": '27'
            }, {
                "name": "Susan",
                "age": '35'
            }
        ],
        "family": {
            "parents": [
                {
                    "relation": "father",
                    "name": "Doe"
                },
                {
                    "relation": "mother",
                    "name": "Jane"
                }
            ],
            "siblings": [
                {
                    "sister1": {
                        "name": "Ana",
                        "age": '26',
                        "children": [
                            "Eric", "Lane"
                        ]
                    }
                }
            ]
        }
    },
    {
        'age': 31,
        'name': 'John',
        'account': {
            'regions': ['US.East', 'SG']
        },
        'profiles': [
            {
                'numeric.single': 42,
                'numeric.list': ['1', '2', '42'],
                'string.single': 'one-world',
                'string.list': ['a', 'set', 'of', 'values']
            }
        ]
    },
    {"base": "EUR", "date": "2018-01-26",
     "rates": {"AUD": 1.538, "BGN": 1.9558, "BRL": 3.9149, "CAD": 1.5325, "CHF": 1.1632, "CNY": 7.8693,
               "CZK": 25.357, "DKK": 7.4428, "GBP": 0.87335, "HKD": 9.7222, "HRK": 7.419, "HUF": 309.8,
               "IDR": 16559.0, "ILS": 4.215, "INR": 79.106, "JPY": 135.95, "KRW": 1323.7, "MXN": 23.067,
               "MYR": 4.8179, "NOK": 9.5655, "NZD": 1.6943, "PHP": 63.492, "PLN": 4.1422, "RON": 4.6663,
               "RUB": 69.525, "SEK": 9.8005, "SGD": 1.6259, "THB": 39.037, "TRY": 4.6635, "USD": 1.2436,
               "ZAR": 14.788}}

]


class TestJsonUri(unittest.TestCase):

    def test_should_serder_data(self):
        data = {
            'age': 31,
            'name': 'John',
            'account': {
                'regions': ['US.East', 'SG']
            },
            'profiles': [
                {
                    'numeric.single': 42,
                    'numeric.list': [1, 2, 3],
                    'string.single': 'one-world',
                    'string.list': ['a', 'set', 'of', 'values']
                }
            ]
        }

        for sample in samples:
            self.assertEqual(jsonuri.deserialize(jsonuri.serialize(sample)), sample)


if __name__ == "__main__":
    unittest.main()
