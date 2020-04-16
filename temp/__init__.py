#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from tempfile import mkstemp, mkdtemp
import public

__all__ = ["TMPDIR"]


@public.add
def tempfile():
    """create temp file and return path"""
    f, path = mkstemp()
    os.close(f)
    return path


@public.add
def tempdir():
    """create temp dir and return path"""
    return mkdtemp()
