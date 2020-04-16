<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/temp.svg?longCache=True)](https://pypi.org/project/temp/)
[![](https://img.shields.io/pypi/v/temp.svg?maxAge=3600)](https://pypi.org/project/temp/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/temp.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/temp.py/)

#### Installation
```bash
$ [sudo] pip install temp
```

#### Functions
function|`__doc__`
-|-
`temp.tempdir()` |create temp dir and return path
`temp.tempfile()` |create temp file and return path

#### Examples
```python
>>> import temp
>>> temp.tempdir() # dir
'/var/folders/rv/gy6_gnfs1d7_pd1518p27tsr0000gn/T/tmpqlLDxb'

>>> temp.tempfile() # file
'/var/folders/rv/gy6_gnfs1d7_pd1518p27tsr0000gn/T/tmpsctFHJ'

>>> temp.TMPDIR
'/var/folders/rv/gy6_gnfs1d7_pd1518p27tsr0000gn/T'
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>