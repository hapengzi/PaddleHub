#coding:utf-8
# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class BaseProcessor(object):
    def __init__(self, module):
        pass

    def preprocess(self, sign_name, data_dict):
        raise NotImplementedError(
            "BaseProcessor' preprocess should not be called!")

    def postprocess(self, sign_name, data_out, data_info, **kwargs):
        raise NotImplementedError(
            "BaseProcessor' postprocess should not be called!")

    def data_format(self, sign_name):
        raise NotImplementedError(
            "BaseProcessor' data_format should not be called!")
