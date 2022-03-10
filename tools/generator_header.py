#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2021 anqi.huang@outlook.com
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


import os
from utils import TYPE_INT, TYPE_BOOLEAN, TYPE_STRING


class GeneratorHeader:
    OUT_FILE_NAME = "JosFeature.h"
    mOutConfDir = ''
    mOutConfPath = ''

    def __init__(self, outdir_root_dir):
        self.mOutConfDir = os.path.join(outdir_root_dir, "include/product")
        self.mOutConfPath = os.path.join(self.mOutConfDir, self.OUT_FILE_NAME)
        pass

    def generate(self, features):
        if not os.path.exists(self.mOutConfDir):
            os.makedirs(self.mOutConfDir)

        with open(self.mOutConfPath, 'w+') as f:
            f.write("# This is auto generated by feature.py, don't modify.\n")
            f.write("#ifndef __PLATFORM_FEATURE__\n")
            f.write("#define __PLATFORM_FEATURE__\n\n")

            for key in features:
                value = features[key][0]
                type = features[key][1]
                comments = features[key][2].split("\n")
                for comment in comments:
                    if comment == "":
                        continue
                    f.write("# " + comment + "\n")

                if TYPE_INT == type:
                    f.write("#define " + str(key) + " " + str(value) + "\n\n")
                elif TYPE_BOOLEAN == type:
                    val = 0
                    if value == 'true':
                        val = 1
                    f.write("#define " + str(key) + " " + str(val) + "\n\n")
                elif TYPE_STRING == type:
                    val = value.replace('"', "").replace('\'', "")
                    f.write("#define " + str(key) + " " + str(val) + "\n\n")

            f.write("#endif // __PLATFORM_FEATURE__\n")

            f.close()
