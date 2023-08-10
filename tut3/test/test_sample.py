from logging import raiseExceptions
import sys
import pytest
from tut3.app.sample import add

# Skipping TEST

@pytest.mark.skip
def test_add(reason="Howa KEDA"):
    assert add(1,2) == 3

# SKIP IF
# this Test case will be skipped beacause of using 3.11.1 Python Version 
@pytest.mark.skipif(sys.version_info > (3,7),reason="using 3.11.1 Python Version ")
def test_sting_add():
    assert add("a","b") == "ab"

@pytest.mark.xfail(sys.platform=="win32",reason="do not run in win32")
def test_add_list():
    assert add([1],[2]) == [1,2]
    raise Exception()

"""
'win32' for Windows
'darwin' for macOS
'linux' for Linux
'aix' for IBM AIX
'sunos' for Sun Solaris
'freebsd' for FreeBSD
'netbsd' for NetBSD
'openbsd' for OpenBSD
'cygwin' for Cygwin (a Unix-like environment for Windows) 
"""

