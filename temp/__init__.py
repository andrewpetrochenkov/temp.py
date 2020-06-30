__all__ = ["tempdir", "tempfile"]


import os
import tempfile


def tempdir():
    """create temp dir and return path"""
    return tempfile.mkdtemp()


def tempfile():
    """create temp file and return path"""
    f, path = tempfile.mkstemp()
    os.close(f)
    return path
