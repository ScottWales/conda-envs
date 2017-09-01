#!/usr/bin/env python
# Copyright 2017 ARC Centre of Excellence for Climate Systems Science
# author: Scott Wales <scott.wales@unimelb.edu.au>
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
from __future__ import print_function

def test_python_version():
    import sys
    assert sys.version_info >= (2,7)
    assert sys.version_info <= (3,0)

def test_numpy_import():
    import numpy

def test_scipy_import():
    import scipy

def test_pandas_import():
    import pandas

def test_xarray_import():
    import xarray

def test_dask_import():
    import dask
    import dask.bag

